import http.server
import json

class WebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        print("Получены данные вебхука:")
        print(json.dumps(data, indent=4))

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps({"status": "success"}), 'utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, WebhookHandler)
    print("Сервер запущен. Жду запросов...")
    httpd.serve_forever()