#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import time
from modules import conf


def authorize_session(data, headers):
    req = requests.post(conf.root_url+conf.auth,
                                      data=data,
                                      headers=headers)
    return req.cookies


def request_lecture(cookies, interval):
    req = requests.get(conf.his_url,
                       cookies=cookies)
    time.sleep(interval)
