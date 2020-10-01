#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import zylogger


def main():
    logging.info('hello zylogger')


if __name__ == '__main__':
    zylogger.init()
    main()

