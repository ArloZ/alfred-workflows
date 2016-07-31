#! /usr/bin/python
# coding = UTF-8

import util

class Item(object):
    """alfred xml item"""

    uid = "123"

    arg = ""
    
    autocomplete = ""

    title = ""

    subtitle = ""

    icon = util.ICON_DISABLE

    def __init__(self):
        super(Item, self).__init__()


def genElement(lists):
    assert(len(lists)%3==0)
    name = lists[0]
    params = lists[1]
    content = lists[2]
    string = ''
    string +="<%s"%name + " "

    for k,v in params.items():
        string+='%s = "%s" '%(k,v)

    if(isinstance(content, str)):
        text = content
    else:
        text = genElement(content)
    string +=">" + text + "</%s>\n"%name

    if(len(lists)<=3):
        return string
    else:
        return string + genElement(lists[3:])

def genAlfredXML(rowList):
    item = []
    for row in rowList:
        tsi = ['title',{},row.title,'subtitle',{},row.subtitle,'icon',{},row.icon]
        item.extend(['item',{'uid':row.uid,'arg':row.arg,'autocomplete':row.autocomplete},tsi])
    items = ['items',{},item]
    return genElement(items)

if __name__=='__main__':
    item = Item()
    item.uid = '293939'
    item.arg = 'args'
    item.autocomplete = 'autocomplete'
    item.icon = 'icon'
    item.subtitle = 'subtitle'
    item.title = 'title'

    itemList = [item]
    element = genAlfredXML(itemList)

    print(element)