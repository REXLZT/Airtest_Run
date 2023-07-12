import http.server
import socketserver
import base64

PORT = 9430
USERNAME = "admin"
PASSWORD = "password"

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Login"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.headers.get("Authorization") is None:
            self.do_AUTHHEAD()
            self.wfile.write(b"Unauthorized")
        elif self.headers.get("Authorization") == "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode():
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.do_AUTHHEAD()
            self.wfile.write(b"Unauthorized")
            
    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = dict(x.split('=') for x in post_data.split('&'))
            username = params['username']
            password = params['password']
            if username == USERNAME and password == PASSWORD:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Login successful")
            else:
                self.send_response(401)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Login failed")
        else:
            self.send_response(501)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Unsupported method")

Handler = AuthHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("服务器已启动，监听端口", PORT)
    httpd.serve_forever()
