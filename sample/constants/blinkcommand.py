__author__ = 'escabia'

commandexec = "./blink1-tool"
commandoption = "--blink"
commandcolorgreen = "--green"
commandcolorred = "--red"
commandcolorlightgreen = "--rgb=0,50,0"
commandcolorlightred = "--rgb=50,0,0"
numblinks = "3"


class Blinkcommand:
    def __init__(self):
        self.commandexec = commandexec
        self.commandoption = commandoption
        self.commandcolorgreen = commandcolorgreen
        self.commandcolorred = commandcolorred
        self.commandcolorlightgreen = commandcolorlightgreen
        self.commandcolorlightred = commandcolorlightred
        self.numblinks = numblinks
