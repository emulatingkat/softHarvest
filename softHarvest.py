#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
#   FILE: softHarvest.py
#   DATE: April 20, 2017
#   Author: Katherine Thornton
#

#This is a program written in Python3 that will start from a list of Yale
#University Library (YUL) barcodes and then pull out some fields from the 
#JSON returned by the Voyager API to feed into YUL bot for Wikidata uploading. 

import requests

baseurl = "http://deleon.library.yale.edu:9090/VoySearch/GetMfhdItem?barcode="
url = ""
barcodes = ["39002076606962", "39002046083961", "39002067185075"]
for barcode in barcodes:
    baseurl+= barcode
    print(url)

files ={}


folders = {}



newFolders = {}



MDoutput = ""



tempDir = "tempMFHDDownloadDir"



outDir = "tempoutput"

r = requests.get('http://deleon.library.yale.edu:9090/VoySearch/GetMfhdItem?barcode=39002067185075')

r.status_code

print(r.text)

#now i need to save the bibid? 4282170 for this record?
