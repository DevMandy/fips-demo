import hashlib, os
from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        hash = hashlib.md5(post_data).hexdigest()
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(hash.encode('utf-8'))

port = int(os.environ.get('PORT', 8080))
httpd = HTTPServer(('', port), RequestHandler)
httpd.serve_forever()
