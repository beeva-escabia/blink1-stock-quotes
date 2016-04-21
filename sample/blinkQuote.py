#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import getopt
import subprocess
from sample.models.notification import Notification
from sample.models.operation import Operation
from sample.models.quote import Quote

__author__ = 'escabia'


def input(argv):
    symbol = ''
    timetorefresh = 0
    limitpercent = 0
    try:
        opts, args = getopt.getopt(argv, "hs:r:p:", ["isymbol=", "irefresh=", "limitPercent="])
    except getopt.GetoptError:
        print 'mainBlinkQuote.py -s <symbol> -r <refreshTime> -p <limitPercent>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'mainBlinkQuote.py -s <symbol> -r <refreshTime> -p <limitPercent>'
            sys.exit()
        elif opt in ("-s", "--isymbol"):
            symbol = arg
        elif opt in ("-r", "--irefresh"):
            timetorefresh = arg
        elif opt in ("-p", "--ipercent"):
            limitpercent = arg

    return Operation(timetorefresh, Quote(symbol), Notification(limitpercent))


def main(argv):
    """
    :blinkQuote argv: -s <symbol> -r <refreshTime> -p <limitPercent>
    """
    operation = input(argv)

    if not operation.isdataavailable():
        print 'Quote ' + operation.quote + ' not available'
        sys.exit()
    else:
        operation.run()

if __name__ == "__main__":
    main(sys.argv[1:])
