import requests

# Function to send GET request to /hello endpoint
def send_hello_request():
    response = requests.get('http://localhost:5000/hello/John')
    print(response.json())

if __name__ == "__main__":
    send_hello_request()