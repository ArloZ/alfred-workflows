#! /usr/bin/python
# coding = UTF-8

import os, sys

# command define
COMMAND_HELP = 0
COMMAND_LS = 1
COMMAND_NEW = 2
COMMAND_DELETE = 3
COMMAND_OPEN = 4

HOST_ORIG = "hostOrig"
HOST_DIR = "hosts/"
HOST_FILE = "/etc/hosts"
HOST_CONFIG = "config.json"


ICON_DISABLE = "switchArrowsDis.png"
ICON_ENABLE = "switchArrowsAct.png"
ICON_ADD_HOST = "addhostA.png"
ICON_DELETE = "deletehost.png"
ICON_OPEN = "openhost.png"

def useHost(name):
    config = readConfig()
    if config['activeHost'] == name:
        return

    cmd = 'cp ' + HOST_DIR + name +' ' + HOST_FILE
    os.system(cmd)

    config['activeHost'] = name
    updateConfig(config)


def deleteHost(name):
    cmd = 'rm ' + HOST_DIR + name
    os.system(cmd)

    config = readConfig()
    if config['activeHost'] == name:
        cmd = 'cp ' + HOST_DIR + HOST_ORIG +' ' + HOST_FILE
        os.system(cmd)

        config['activeHost'] = HOST_ORIG
        updateConfig(config)


def getAllHosts():
    config = readConfig()
    files = os.listdir(HOST_DIR)
    hostFiles = []
    for fname in files:
        if fname == HOST_ORIG:
            continue
        f = {'name':fname}
        if fname == config['activeHost']:
            f['active'] = 1
        else:
            f['active'] = 0
        hostFiles.append(f)
    return hostFiles

def command(comm):
    if comm in ['ls','l']:
        return COMMAND_LS
    elif comm in ['new','n']:
        return COMMAND_NEW
    elif comm in ['del','d']:
        return COMMAND_DELETE
    elif comm in ['open','o']:
        return COMMAND_OPEN
    else:
        return COMMAND_HELP

def hostsDir():
    return os.getcwd()+ '/' + HOST_DIR

def readConfig():
    configFile = open(HOST_CONFIG)
    confStr = ''
    for line in configFile.readlines():
        confStr += line
    configFile.close()
    if len(confStr) > 0:
        return eval(confStr)
    else:
        return {'activeHost':''}

def updateConfig(config):
    configFile = open(HOST_CONFIG,'w')
    configFile.write(str(config))
    configFile.close()

if __name__ == '__main__':

    print hostsDir()
    print getAllHosts()