# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:09:28 2016

@author: weiya
"""

import sqlite3
import newCompanyList
time_sql = [('2011-01-01 00:00', '2011-12-31 23:59'),
            ('2012-01-01 00:00', '2012-12-31 23:59'),
            ('2013-01-01 00:00', '2013-12-31 23:59'),
            ('2014-01-01 00:00', '2014-12-31 23:59'),
            ('2015-01-01 00:00', '2015-12-31 23:59')]
def count(conn, fw):
    try:
        for i in xrange(len(time_sql)):    
            num_total_sql = "select count(*) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
            num_forward_sql = "select sum(forward) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
            num_comment_sql = "select sum(comment) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
            num_praised_sql = "select sum(praised) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
            fw.write(time_sql[i][0].split('-')[0].split('-')[0])
            fw.write(',')
            fw.write(str(conn.execute(num_total_sql).fetchone()[0]))
            fw.write(',')
            fw.write(str(conn.execute(num_forward_sql).fetchone()[0]))
            fw.write(',')
            fw.write(str(conn.execute(num_comment_sql).fetchone()[0]))
            fw.write(',')
            fw.write(str(conn.execute(num_praised_sql).fetchone()[0]))
            fw.write('\n')
        return 1
    except:
        print 'Unknown Error.'
        return 0

def run(companyId,code_dict,fw):
    sqlite_file = 'company' + str(companyId).zfill(4) + '.db'
    try:
        conn = sqlite3.connect(sqlite_file)
    except:
        print 'NO ' + str(companyId)
        return 0
    #csv = 'Result' + sqlite_file.split('.')[0] + '.csv'
    #fw = open(csv,'w')
    #fw.write('code,name,date,num_total,num_forward,num_comment,num_praised\n')
    company_name = newCompanyList.company[companyId]
    company_code = code_dict.get(company_name)
    for i in xrange(len(time_sql)):    
        num_total_sql = "select count(*) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
        num_forward_sql = "select sum(forward) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
        num_comment_sql = "select sum(comment) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
        num_praised_sql = "select sum(praised) from weibo where datetime(time) >= datetime('%s') and datetime(time) <=datetime('%s');" %(time_sql[i][0], time_sql[i][1])
        fw.write(str(company_code))
        fw.write(',')
        fw.write(company_name)
        fw.write(',')
        fw.write(time_sql[i][0].split('-')[0].split('-')[0])
        fw.write(',')
        try:
            fw.write(str(conn.execute(num_total_sql).fetchone()[0]))
        except:
            fw.write('NA')
        fw.write(',')
        try:
            fw.write(str(conn.execute(num_forward_sql).fetchone()[0]))
        except:
            fw.write('NA')
        fw.write(',')
        try:
            fw.write(str(conn.execute(num_comment_sql).fetchone()[0]))
        except:
            fw.write('NA')
        fw.write(',')
        try:
            fw.write(str(conn.execute(num_praised_sql).fetchone()[0]))
        except:
            fw.write('NA')
        fw.write('\n')
    conn.close()
    
if __name__ == '__main__':
    f = open('code.csv')
    code = []
    while 1:
        line = f.readline().strip()
        if not line:
            break
        code.append(line)
    f.close()
    code_dict = {}
    for i in xrange(len(code)):
        [value, key] = code[i].split(',')
        code_dict.update({key:value})
    
    csv = 'Result.csv'
    fw = open(csv,'w')
    fw.write('code,name,date,num_total,num_forward,num_comment,num_praised\n')
    for i in xrange(141,511):
        run(i, code_dict, fw)
    fw.close()
    

    
