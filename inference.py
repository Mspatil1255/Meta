from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 8000

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_POST(self):
        if self.path == "/reset":
            self._set_headers(200)
            self.wfile.write(json.dumps({"status": "reset successful"}).encode())
        elif self.path == "/validate":
            self._set_headers(200)
            self.wfile.write(json.dumps({"status": "validation successful"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())

    def do_GET(self):
        self._set_headers(200)
        self.wfile.write(json.dumps({"message": "Inference server is running"}).encode())

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()
