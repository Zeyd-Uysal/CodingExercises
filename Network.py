#!/usr/bin/env python3
import requests
import socket
import re


def check_localhost():
    return str(socket.gethostbyname('localhost')) == "127.0.0.1"


def check_connectivity():
    return len(re.findall(r"200", str(requests.get("http://www.google.com")))) == 1
