import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        """
        Handle GET requests for different endpoints
        """
        # Set response headers
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Handle different endpoints
        if self.path == '/':
            # Root endpoint
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode())
            
        elif self.path == '/data':
            # /data endpoint - serve JSON data
            data = {
                "name": "John", 
                "age": 30, 
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
            
        elif self.path == '/status':
            # /status endpoint - API status check
            response = "OK"
            self.wfile.write(response.encode())
            
        elif self.path == '/info':
            # /info endpoint - API information
            info = {
                "version": "1.0", 
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())
            
        else:
            # Handle undefined endpoints - 404 Not Found
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            error_message = "Endpoint not found"
            self.wfile.write(error_message.encode())

def run_server():
    """
    Start the HTTP server on port 8000
    """
    PORT = 8000
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server running on port {PORT}")
        print("Available endpoints:")
        print("  http://localhost:8000/")
        print("  http://localhost:8000/data")
        print("  http://localhost:8000/status")
        print("  http://localhost:8000/info")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
