#!/usr/bin/env python3
"""Static preview server for the FreeToken repo.

Serves the repository root, so app/index.html can fetch ../data/*.json directly,
and redirects / to the catalogue page.

Every response is sent with ``Cache-Control: no-store``. The app is a single
83 KB HTML file whose content changes with each pass, and the data JSON changes
more often still; a heuristically cached copy of either makes the preview look
like the work was never deployed.
"""

import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        if self.path.split("?")[0] in ("/", "/index.html"):
            self.send_response(302)
            self.send_header("Location", "/app/index.html")
            self.end_headers()
            return
        super().do_GET()

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
