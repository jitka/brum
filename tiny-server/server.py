import socket
from http.server import HTTPServer

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6
