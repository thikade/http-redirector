import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class Redirect(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        base = os.environ.get("REDIRECT_URL", "https://www.google.com").rstrip("/")
        self.send_header("Location", base + self.path)
        self.end_headers()
    def do_POST(self): self.do_GET()
    def log_message(self, format): pas

HTTPServer(("", int(os.environ.get("PORT", 8080))), Redirect).serve_forever()