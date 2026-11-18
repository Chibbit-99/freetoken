# FreeToken

FreeToken is a static directory of hosted text-generation APIs with a free access offer. Browse providers, compare model listings and limits, and follow links to the provider's own documentation and signup pages.

## Run locally

Requires Python 3. From the repository root:

```sh
python3 tools/serve.py
```

Open `http://localhost:8000/`. The server serves both the app and the JSON data; opening the HTML directly as a file may prevent data from loading. Set `PORT` to change the port. There is no build step or API key required to browse.

## Using the catalogue

Search and filter the catalogue, then select a provider for its offer, models, links, privacy notes and source dates. An ongoing free allowance, a free model and a finite trial are different things: check the badge and details. The no-card filter includes only providers explicitly recorded as not requiring a card; unknown is not the same as no card.

Offers, quotas, regions, model availability and terms change. Listings summarize public sources, not a guarantee of uptime, model identity, eligibility, billing or privacy. Check the linked first-party terms and your account's actual limits before use; do not send sensitive information without reviewing the provider and upstream policies. Some gateways can fall back to paid routes or substitute models.

## Data and maintenance

- `app/index.html`: standalone frontend.
- `data/providers.json`: ordered manifest of provider files.
- `data/<id>.json`: offer, models, requirements, privacy and verification sources for each provider.
- `data/SCHEMA.md`: field definitions, scope and contribution guidance.
- `data/LEAD_VERIFICATION.md`: research decisions, exclusions and caveats.
- `data/announcements.json`: dated catalogue updates.
- `tools/add_new_providers.py` and `tools/new_providers_*.py`: source tuples and generator for many entries. Edit their source as well as regenerating data when changing a generated record. Run `python3 tools/add_new_providers.py --dry-run` to inspect the planned writes; the regular command rewrites generated entries and updates the manifest.
- `tools/add_announcement.py`: add a validated announcement; run `--help` for options.

For additions, verify current first-party evidence of hosted text generation and usable free access, check for duplicates, distinguish trials from recurring offers, document uncertainty, and follow the schema. Self-hosted runtimes and speech, image, video or embedding-only services are outside the catalogue's scope.
