# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:58:59 2016

@author: weiya
"""

import result

for i in xrange(26):
    sql_file = 'company'+str(i).zfill(4) + '.db'
    result.run(sql_file)