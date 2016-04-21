#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import subprocess
import time
from sample.constants.blinkcommand import Blinkcommand
from sample.constants.yahoofinance import Yahoofinance

__author__ = 'escabia'


class Operation:
    def __init__(self, time, quote, notification):
        self.time = time
        self.quote = quote
        self.notification = notification
        self.yahoo = Yahoofinance()
        self.blink = Blinkcommand()

    def isdataavailable(self):
        name = urllib2.urlopen(str(self.yahoo.urldata) + str(self.quote) + str(self.yahoo.unionbunchtags) + str(self.yahoo.tagname)).read()
        print name
        if name == "N/A\n":
            subprocess.call([self.blink.commandexec, self.blink.commandcolorwhite])
            return False
        else:
            return True

    def run(self):
        openprice = urllib2.urlopen(
                    str(self.yahoo.urldata) +
                    str(self.quote.symbol) +
                    str(self.yahoo.unionbunchtags) +
                    str(self.yahoo.tagopenprice)).read()
        newprice = -1
        while 1:
            data = urllib2.urlopen(
                                      str(self.yahoo.urldata)
                                    + str(self.quote.symbol)
                                    + str(self.yahoo.unionbunchtags)
                                    + str(self.yahoo.tagpercent)
                                    ).read();
            percent = float(data[1:-3])
            if percent > int(self.notification.percent):
                subprocess.call([self.blink.commandexec, self.blink.commandcolorgreen, self.blink.commandoption,
                                 self.blink.numblinks])
            elif percent < -int(self.notification.percent):
                subprocess.call(
                    [self.blink.commandexec, self.blink.commandcolorred, self.blink.commandoption, self.blink.numblinks])
            else:
                price = urllib2.urlopen(
                                        str(self.yahoo.urldata)
                                        + str(self.quote.symbol)
                                        + str(self.yahoo.unionbunchtags)
                                        + str(self.yahoo.taglasttrade)).read()
                if price == newprice:
                        subprocess.call([self.blink.commandexec, self.blink.commandcolornight])
                else:
                    if price > openprice:
                        subprocess.call([self.blink.commandexec, self.blink.commandcolorlightgreen])

                    else:
                        subprocess.call([self.blink.commandexec, self.blink.commandcolorlightred])

                    time.sleep(float(self.time))

                    newprice = urllib2.urlopen(
                        self.yahoo.urldata + self.quote.symbol + self.yahoo.unionbunchtags + self.yahoo.taglasttrade).read()

                    if newprice > price:
                        subprocess.call([self.blink.commandexec, self.blink.commandcolorgreen, self.blink.commandoption,
                                         self.blink.numblinks])
                    else:
                        subprocess.call([self.blink.commandexec, self.blink.commandcolorred, self.blink.commandoption,
                                         self.blink.numblinks])
