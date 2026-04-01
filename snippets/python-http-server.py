from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
