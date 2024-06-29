import os
import sys
from io import BytesIO
from urllib.parse import urlencode

sys.path.append('../')

from blog.wsgi import application

def simulate_wsgi_environment():
    environ = {
        'REQUEST_METHOD': 'GET',  
        'SCRIPT_NAME': '',         
        'PATH_INFO': '/',         
        'QUERY_STRING': '',      
        'SERVER_NAME': 'localhost',
        'SERVER_PORT': '8000',  
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'http',
        'wsgi.input': BytesIO(), 
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    return environ

# Function to start the application
def start_response(status, response_headers, exc_info=None):
    print(f"Status: {status}")
    print("Response Headers:")
    for header in response_headers:
        print(f"{header[0]}: {header[1]}")

# Construct the environment
environ = simulate_wsgi_environment()

# Call the application with simulated request
response = application(environ, start_response)
for data in response:
    sys.stdout.write(data.decode('utf-8'))

