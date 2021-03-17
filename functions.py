#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime

def logstr(string):
    today = datetime.datetime.now() 
    logfile_name = "review_log" + today.strftime("%Y%m%d") +".log"
    f = open("logs/"+logfile_name, "a")
    
    if isinstance(string, list):
        str1 = ','.join(str(e) for e in string)
        string = str1

    log_string=os.environ.get('USER')+" ["+today.strftime('%Y-%m-%d %H:%M:%S')+"] "+string
    f.write(log_string + "\n")
    f.close()
    return False