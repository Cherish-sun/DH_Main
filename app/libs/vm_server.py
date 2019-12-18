# -*- coding:utf-8 -*-
import base64


def getVMinfo():
    #ipaddr = "172.16.10.102"
    ipaddr = "172.16.6.100"
    port = "3389"
    userid = "worker"
    passwd = "Pass!234"
    str = ipaddr + "|" + port + "|" + userid + "|" + passwd
    ref = [ipaddr, base64.b64encode(str.encode('utf-8'))]
    return ref[0], ref[1].decode('utf-8')
