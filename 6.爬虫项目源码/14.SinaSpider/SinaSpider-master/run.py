# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 01:23:18 2016

@author: weiya
"""

#import os
import companyList
import sinaCrawlforADSL
ferror = open('error.log', 'w')

for i in xrange(len(companyList)):
#    os.popen('python.exe sinaCrawlforADSL.py ' + str(i))
    sinaCrawlforADSL.main(i, ferror)
ferror.close()

    