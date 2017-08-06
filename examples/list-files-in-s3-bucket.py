#!/usr/bin/env python

import smartpath


# display a list of files in s3://my.s3.bucket/basefolder

bS3 = smartpath.SmartBase("s3://my.s3.bucket/basefolder")
bS3.connectors.append(S3Connector())

p = bS3.getFolder("mysubfolder/")
for f in p.files:
  print f.path




