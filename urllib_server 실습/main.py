from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpeleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello World")

server = HTTPServer(("", 8000), SimpeleHTTPRequestHandler)
server.serve_forever()