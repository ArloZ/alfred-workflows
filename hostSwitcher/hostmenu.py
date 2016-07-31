#! /usr/bin/python
# coding = UTF-8

import alfredxml
import util

def helpMsg():
    items = []

    item = alfredxml.Item()
    item.title = 'Usage: host ls'
    item.subtitle = 'list all host files, and select a host to use.'
    item.uid = '00001'
    item.icon = util.ICON_ENABLE
    items.append(item)

    item = alfredxml.Item()
    item.title = 'Usage: host new'
    item.subtitle = 'create a host file to use.'
    item.uid = '00002'
    item.icon = util.ICON_ADD_HOST
    items.append(item)

    item = alfredxml.Item()
    item.title = 'Usage: host del'
    item.subtitle = 'delete a host file, and then use the original host.'
    item.uid = '00003'
    item.icon = util.ICON_DELETE
    items.append(item)

    item = alfredxml.Item()
    item.title = 'Usage: host open'
    item.subtitle = 'list all host files, and select a host to open.'
    item.uid = '00004'
    item.icon = util.ICON_OPEN
    items.append(item)

    return items

def listHosts():
    hosts = util.getAllHosts()
    items = []
    for idx, h in enumerate(hosts):
        item = alfredxml.Item()
        item.title = 'use: ' + h['name']
        item.uid = '%s',idx
        item.arg = 'ls ' + h['name']
        if h['active'] > 0:
            item.icon = util.ICON_ENABLE
        items.append(item)
    return items

def deleteHosts():
    hosts = util.getAllHosts()
    items = []
    for idx, h in enumerate(hosts):
        item = alfredxml.Item()
        item.title = 'Delete: ' + h['name']
        item.uid = '%s',idx
        item.arg = 'del ' + h['name']
        item.icon = util.ICON_DELETE
        items.append(item)
    return items


def openHosts():
    hosts = util.getAllHosts()
    items = []
    for idx, h in enumerate(hosts):
        item = alfredxml.Item()
        item.title = 'Press \'cmd\' to Show: ' + h['name']
        item.uid = '%s',idx
        item.arg = util.hostsDir() + h['name']
        item.icon = util.ICON_OPEN
        items.append(item)
    return items

def newHosts():
    item = alfredxml.Item()
    item.title = 'Press \'cmd\' to Create'
    item.uid = 'new'
    item.icon = util.ICON_ADD_HOST
    item.arg = util.hostsDir()
    return [item]


def do(query):
    if util.command(query) == util.COMMAND_LS:
        items = listHosts()
    elif util.command(query) == util.COMMAND_OPEN:
        items = openHosts()
    elif util.command(query) == util.COMMAND_NEW:
        items = newHosts()
    elif util.command(query) == util.COMMAND_DELETE:
        items = deleteHosts()
    else:
        items = helpMsg()

    return alfredxml.genAlfredXML(items)

if __name__ == '__main__':
    print do("query")