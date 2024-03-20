#!/usr/bin/python3

import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
import logging

logging.basicConfig(level=logging.DEBUG)

class DownloadRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Specify the file you want to serve
            filepath = '/home/ubuntu/2booking/cgi-bin/downloadfiles/hongbooking19_student'
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

        except Exception as e:
            logging.exception("An error occurred during request handling")

if __name__ == "__main__":
    server_address = ('127.0.0.1', 5000)
    #server_address = ('www.hongpage.com', 5000)
    httpd = HTTPServer(server_address, DownloadRequestHandler)

    # Load SSL certificate and key
    certfile = '/home/ubuntu/public.pem'
    keyfile = '/home/ubuntu/private.pem'

    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile, keyfile)

    # Start HTTPS server
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print("Server started on localhost port 5000 (HTTPS)...")
    httpd.serve_forever()

