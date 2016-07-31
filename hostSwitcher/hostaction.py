#! /usr/bin/python
# coding = UTF-8

import util


def do(query):
    action = query.split()[0]
    if util.command(action) == util.COMMAND_LS:
        name = query.split()[1]
        util.useHost(name)
        showMsg('Use host: '+name)
    elif util.command(action) == util.COMMAND_DELETE:
        name  = query.split()[1]
        util.deleteHost(name)
        showMsg('Delete host: '+name)
    else:
        showMsg('Unknow command')

def showMsg(msg):
    print msg
    

if __name__ == '__main__':
    print do("query")