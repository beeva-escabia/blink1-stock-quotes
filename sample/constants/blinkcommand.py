__author__ = 'escabia'

commandexec = "./blink1-tool"
commandoption = "--blink"
commandcolorgreen = "--green"
commandcolorred = "--red"
commandcolorlightgreen = "--rgb=0,50,0"
commandcolorlightred = "--rgb=50,0,0"
commandcolorwhite = "--rgb=255,255,255"
commandcolornight = "--rgb=51,0,231"

numblinks = "3"


class Blinkcommand:
    def __init__(self):
        self.commandexec = commandexec
        self.commandoption = commandoption
        self.commandcolorgreen = commandcolorgreen
        self.commandcolorred = commandcolorred
        self.commandcolorlightgreen = commandcolorlightgreen
        self.commandcolorlightred = commandcolorlightred
        self.commandcolorwhite = commandcolorwhite
        self.commandcolornight = commandcolornight
        self.numblinks = numblinks
