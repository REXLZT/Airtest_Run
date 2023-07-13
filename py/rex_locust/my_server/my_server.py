import http.server
import socketserver
import base64

# 定义监听的端口号以及用户名和密码
PORT = 9430
USERNAME = "admin"
PASSWORD = "password"

# 定义一个处理器类，继承自http.server.SimpleHTTPRequestHandler
class AuthHandler(http.server.SimpleHTTPRequestHandler):
    # 发送401响应和WWW-Authenticate头，提示客户端进行身份验证
    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Login"')
        self.send_header("Content-type", "text/html")
        self.end_headers()

    # 处理GET请求
    def do_GET(self):
        # 检查请求头中是否包含Authorization字段
        if self.headers.get("Authorization") is None:
            # 如果不包含Authorization字段，说明客户端没有提供身份验证信息，返回401响应
            self.do_AUTHHEAD()
            self.wfile.write(b"Unauthorized")
        # 如果提供的身份验证信息正确，调用父类的do_GET方法处理请求,并且进入欢迎页面
        elif self.headers.get("Authorization") == "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode():
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b'''
            <html>
            <head>
                <title>Welcome Page</title>
            </head>
            <body>
                <h1>Welcome to the home page!</h1>
                <p>You are logged in as admin.</p>
            </body>
            </html>
            ''')
        # 如果提供的身份验证信息不正确，返回401响应
        else:
            self.do_AUTHHEAD()
            self.wfile.write(b"Unauthorized")
            
    # 处理POST请求
    def do_POST(self):
        # 如果请求的路径是/login，尝试验证用户名和密码
        if self.path == "/login":
            # 获取POST请求的数据，并解析为字典
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = dict(x.split('=') for x in post_data.split('&'))
            username = params['username']
            password = params['password']
            # 如果用户名和密码正确，返回200响应
            if username == USERNAME and password == PASSWORD:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Login successful")
            # 如果用户名或密码不正确，返回401响应
            else:
                self.send_response(401)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Login failed")
        # 如果请求的路径不是/login，返回501响应
        else:
            self.send_response(501)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Unsupported method")

# 使用AuthHandler处理器类创建一个HTTP服务器，并开始监听请求
Handler = AuthHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("服务器已启动，监听端口", PORT)
    httpd.serve_forever()
