#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime
import settings

def logstr(string):
    today = datetime.datetime.now() 
    dirname = settings.options["LogPath"]
    logfile_name = dirname+"review_log" + today.strftime("%Y%m%d") +".log"
    f = open(logfile_name, "a")
    #os.chmod(logfile_name, 0o777)
    #uid = settings.options["Loguid"]
    #gid = settings.options["Loggid"]
    #os.chown(logfile_name, uid, gid)
    
    
    if isinstance(string, list):
        str1 = ','.join(str(e) for e in string)
        string = str1

    log_string=os.environ.get('USER')+" ["+today.strftime('%Y-%m-%d %H:%M:%S')+"] "+string
    f.write(log_string + "\n")
    f.close()
    return False
