#!/usr/bin/env python

import smartpath


# list files in current folder

bLocal = smartpath.SmartBase("file://.")
fc = smartpath.LocalFileSystemConnector()
bLocal.connectors.append(fc)

p = bLocal.getFolder("/")
for f in p.files:
  print f.path, f.size


