#!/usr/bin/python3

import os
from http.server import BaseHTTPRequestHandler

class DownloadRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Specify the file you want to serve
        filepath = 'downloadfiles/hongbooking19_student'
        filename = os.path.basename(filepath)
        
        # Check if file exists
        if os.path.isfile(filepath):
            # Set headers
            self.send_response(200)
            self.send_header('Content-Type', 'application/octet-stream')
            self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
            self.end_headers()
            
            # Read the file and write it to response
            with open(filepath, 'rb') as file:
                self.wfile.write(file.read())
        else:
            # If file not found, send 404 response
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found.')

if __name__ == "__main__":
    from http.server import HTTPServer
    server_address = ('', 5000)  # Serve at: http://localhost:5000
    httpd = HTTPServer(server_address, DownloadRequestHandler)
    print("Server started on localhost port 5000...")
    httpd.serve_forever()
