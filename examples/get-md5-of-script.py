#!/usr/bin/env python

# get the md5 of this script

import smartpath

bLocal = smartpath.SmartBase("file://.")
fc = smartpath.LocalFileSystemConnector()
md5c = smartpath.LocalMd5Connector()

bLocal.connectors.append(fc)
bLocal.connectors.append(md5c)
fl1 = bLocal.getFile("get-md5-of-script.py")
print fl1.md5

