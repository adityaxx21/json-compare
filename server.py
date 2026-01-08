import http.server
import socketserver
import json
import os
from compare_json import compare_json, generate_markdown_report

PORT = 8000

class ApplicationRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/compare':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                
                request_data = json.loads(post_data.decode('utf-8'))
                
                json_a_str = request_data.get('json_a', '{}')
                json_b_str = request_data.get('json_b', '{}')
                
                try:
                    data_a = json.loads(json_a_str)
                except json.JSONDecodeError:
                    raise ValueError("Invalid JSON in Input A")
                    
                try:
                    data_b = json.loads(json_b_str)
                except json.JSONDecodeError:
                    raise ValueError("Invalid JSON in Input B")
                
                diffs, only_a, only_b = compare_json(data_a, data_b)
                
                report = generate_markdown_report(diffs, only_a, only_b, data_a, data_b, outfile=None)
                
                self.send_response(200)
                self.send_header('Content-Type', 'text/markdown')
                self.end_headers()
                self.wfile.write(report.encode('utf-8'))
                
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_error(404, "Endpoint not found")

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

print(f"Serving at http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), ApplicationRequestHandler) as httpd:
    httpd.serve_forever()
