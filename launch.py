# -*- coding: utf-8 -*-
__author__ = 'luoqian'

import json

if __name__ == '__main__':
    config = {}

    print('读取config配置')
    print('==============================================')
    with open('config.json', 'r') as f:
        config = json.load(f)

    print(config)
    print('==============================================')
