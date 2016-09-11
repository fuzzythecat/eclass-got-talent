#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
from modules import conf


def check_network_connection(host="8.8.8.8", port=53, timeout=3):
    import socket
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        return False


def authorize_session(data, headers):
    req = requests.post(conf.root_url+conf.auth,
                                      data=data,
                                      headers=headers)
    return req.cookies


def request_lecture(cookies, interval):
    req = requests.get(conf.his_url,
                       cookies=cookies)
    time.sleep(interval)
