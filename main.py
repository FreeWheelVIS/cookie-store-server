from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies

class TestServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')

        # set a cookie with a name and value
        cookie = cookies.SimpleCookie()
        cookie['name'] = 'value'

        # serve a response with cookies
        self.send_header('Set-Cookie', cookie.output(header=''))
        self.end_headers()

        # For Python 3, prefix the string literals with a b:
        self.wfile.write(b'<html><body>')
        self.wfile.write(b'<h1>Hello World!</h1>')
        self.wfile.write(b'</body></html>')

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, TestServer)
    print('Server listening on port 8000...')
    httpd.serve_forever()
	