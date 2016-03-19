#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'escabia'

unionbunchtags = "&f="
tagopenprice = "p"
tagname = "n"
tagpercent = "p2"
taglasttrade = "l1"
urldata = "http://finance.yahoo.com/d/quotes.csv?s="


class Yahoofinance:
    def __init__(self):
        self.unionbunchtags = unionbunchtags
        self.tagopenprice = tagopenprice
        self.tagpercent = tagpercent
        self.taglasttrade = taglasttrade
        self.urldata = urldata
        self.tagname = tagname
