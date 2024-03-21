# #!/usr/bin/python3

from http.server import SimpleHTTPRequestHandler, HTTPServer
import ssl

class DownloadRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            filepath = '/home/ubuntu/2booking/cgi-bin/downloadfiles/hongbooking19_student'

            if os.path.isfile(filepath):
                with open(filepath, 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/octet-stream')
                    self.send_header('Content-Disposition', 'attachment; filename="hongbooking19_student"')
                    self.end_headers()
                    self.wfile.write(file.read())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'File not found.')

        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Internal Server Error')

if __name__ == "__main__":
    server_address = ('localhost', 5000)
    httpd = HTTPServer(server_address, DownloadRequestHandler)

    # Load SSL certificate and key
    certfile = '/home/ubuntu/public.pem'
    keyfile = '/home/ubuntu/private.pem'

    try:
        # Create SSL context
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile, keyfile)

        # Start HTTPS server
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print("Server started on localhost port 8000 (HTTPS)...")
        httpd.serve_forever()
    
    except Exception as e:
        print("An error occurred while starting the server:", e)
