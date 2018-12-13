# -*- coding: utf-8 -*-
from websocket import ABNF

__author__ = 'luoqian'

import websocket


class WebSocketClient(object):
    """
    WebSocket客户端
    """

    _ws = None

    def __init__(self, ip: str, port: int,
                 on_message_handle: function = lambda message: print('Receive Message:%s' % message),
                 on_open_handle: function = lambda: print('WebSocket Open'),
                 on_error_handle: function = lambda _ws, error: print('WebSocket Error' + error),
                 on_close_handle: function = lambda: print('WebSocket Closed')):
        self.ip = ip
        self.port = port
        self.on_message_handle = on_message_handle
        self.on_open_handle = on_open_handle
        self.on_error_handle = on_error_handle
        self.on_close_handle = on_close_handle

    def start_connect(self):
        """
        发起WebSocket连接
        :return:
        """
        websocket.enableTrace(True)
        self._ws = websocket.WebSocketApp("ws://%s:%d" % self.ip, self.port,
                                          on_message=self.on_message_handle,
                                          on_error=self.on_error_handle,
                                          on_close=self.on_close_handle)
        self._ws.on_open = self.on_open_handle
        self._ws.run_forever()
        print('WebSocket connect at ws://%s:%d' % self.ip, self.port)

    def send_message(self, content: str, opcode: int = ABNF.OPCODE_TEXT):
        """
        发送消息
        :param content: 消息内容
        :param opcode:
            OPCODE_CONT
            OPCODE_TEXT
            OPCODE_BINARY
            OPCODE_CLOSE
            OPCODE_PING
            OPCODE_PONG
        :return:
        """
        self._ws.send(content, opcode)

    def close(self):
        """
        关闭WebSocket连接
        :return:
        """
        self._ws.close()
