"""Checks for the curated dashboard totals and allowance period conversion."""
import json
import math
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AggregateMetricsTest(unittest.TestCase):
    def test_curated_values_reference_existing_providers(self):
        manifest = json.loads((ROOT / 'data/providers.json').read_text())['providers']
        providers = {p['id']: p for p in (
            json.loads((ROOT / 'data' / filename).read_text()) for filename in manifest
        )}
        data = json.loads((ROOT / 'data/aggregate_metrics.json').read_text())
        for group in ('trial_credit_usd', 'requests_per_minute'):
            self.assertTrue(data[group])
            for provider_id, value in data[group].items():
                self.assertIn(provider_id, providers)
                self.assertIsInstance(value, (int, float))
                self.assertNotIsInstance(value, bool)
                self.assertTrue(math.isfinite(value) and value > 0)
                if group == 'trial_credit_usd':
                    self.assertEqual(providers[provider_id]['offer']['type'], 'trials')

    def test_foreign_credit_metadata_and_conversion(self):
        data = json.loads((ROOT / 'data/aggregate_metrics.json').read_text())
        ids = {f[:-5] for f in json.loads((ROOT / 'data/providers.json').read_text())['providers']}
        fx = data['fx_reference']['rates_per_eur']
        self.assertEqual(data['fx_reference']['date'], '2026-11-17')
        self.assertGreater(fx['USD'], 0)
        foreign_total = 0
        for provider, grant in data['trial_credit_foreign'].items():
            self.assertIn(provider, ids)
            self.assertNotIn(provider, data['trial_credit_usd'])
            self.assertGreater(grant['amount'], 0)
            self.assertGreater(fx[grant['currency']], 0)
            foreign_total += grant['amount'] / fx[grant['currency']] * fx['USD']
        self.assertEqual(round(sum(data['trial_credit_usd'].values()) + foreign_total, 2), 1545.65)
        self.assertFalse({'sarvam', 'sarvam-ai'} <= set(data['trial_credit_foreign']))

    def test_shared_weekly_and_one_time_pools(self):
        # Exercise the same function shipped in the browser; Node supplies the
        # minimal state so this test needs no npm dependencies or web server.
        html = (ROOT / 'app/index.html').read_text()
        match = re.search(r'        function providerAllowanceRows\(\) \{.*?\n        \}\n\n        function leaderboardRows', html, re.S)
        self.assertIsNotNone(match)
        function = match.group().rsplit('\n\n        function leaderboardRows', 1)[0]
        script = '''
const state = {providers: [
  {id:'shared', name:'Shared', free_token_allowance:100, allowance_period:'week', models:[{token_allowance:999}]},
  {id:'grant', name:'Grant', free_token_allowance:50, allowance_period:'one-time', models:[]},
  {id:'daily', name:'Daily', models:[{token_allowance:2}, {token_allowance:3}]},
  {id:'unknown', name:'Unknown', models:[{}]}
]};
''' + function + '''
const rows = providerAllowanceRows();
if (rows.length !== 3) throw new Error('unknown quota included');
const byId = Object.fromEntries(rows.map(r => [r.provider.id, r]));
if (Math.abs(byId.shared.monthly - 100 * 30 / 7) > 0.00001) throw new Error('weekly conversion or shared pool');
if (byId.grant.monthly !== 50) throw new Error('one-time grant');
if (byId.daily.monthly !== 150) throw new Error('daily model total');
'''
        subprocess.run(['node', '-e', script], check=True, cwd=ROOT)


if __name__ == '__main__':
    unittest.main()
