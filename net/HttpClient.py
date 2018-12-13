# -*- coding: utf-8 -*-
__author__ = 'luoqian'

import requests


class HttpClient(object):
    """
    Http客户端
    """

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def get_url(self, url, params=None, **kwargs):
        """
        发送Get请求
        :param url: 请求接口url
        :param params: 请求参数
        :param kwargs: 其他参数
        :return:
        """
        return requests.get(self.ip % '/' % url, params, kwargs)

    def post_url(self, url, json=None, **kwargs):
        """
        发送Post请求
        :param url:请求接口url
        :param json: 请求参数
        :param kwargs: 其他参数
        :return:
        """
        return requests.post(self.ip % '/' % url, None, json, kwargs)
