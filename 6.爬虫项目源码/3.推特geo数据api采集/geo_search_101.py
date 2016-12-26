#coding:utf-8
#!/usr/bin/python
from twitter import *
import sys
import csv
import os,re,time,MySQLdb,MySQLdb.cursors,urllib2,random

MYSQL_HOST = 'ip'
MYSQL_DBNAME = 'CollectTwitter'
MYSQL_USER = '**'
MYSQL_PASSWD = '**'
MYSQL_PORT= **
#台北101
#25.033611, 121.564444
latitude =25.033611 # geographical centre of search
longitude =121.564444 # geographical centre of search
max_range = 2		# search range in kilometres
num_results = 500		# minimum results to obtain

config = {}
execfile("config_government.py", config)
#execfile("config.py", config)

twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

result_count = 0
#last_id = 786564859882196998

conn = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DBNAME,port=MYSQL_PORT,charset='utf8')
cur = conn.cursor()

def insert_ll(address_ll,conn,cur):
	mysql_str = '''
		INSERT INTO twitter_101(`user`,`text`,`latitude`,`longitude`,`full_name`,`result_type`,`created_at`,
		`profile_background_image_url`,`description`,`user_id`,`expanded_url`,`profile_image_url_https`,
		`user_name`,`followers_count`,`user_created_at`,`author`,`iso_language_code`,`verified`,`twitter_id`)
		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
	try:
		conn.ping()
		print 'ping ing '
	except Exception,e:
		print Exception,e
		conn = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DBNAME,port=MYSQL_PORT,charset='utf8')
		cur = conn.cursor()
    #print self.mysql_str % address_ll
	try:
		cur.execute(mysql_str,address_ll)
	except Exception,e:
		print Exception,e
	return None

def get_last_id(conn,cur):
	mysql_str = '''SELECT twitter_id FROM CollectTwitter.`twitter_101` order by twitter_id limit 1;'''
	try:
		conn.ping()
	except:
		conn = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DBNAME,port=MYSQL_PORT,charset='utf8')
		cur = conn.cursor()
	cur.execute(mysql_str)
	for data in cur.fetchall():
	    return data[0]
	return None

def get_now_id(conn,cur):
	mysql_str = '''SELECT twitter_id,created_at FROM CollectTwitter.`twitter_101` order by twitter_id desc limit 1;'''
	try:
		conn.ping()
	except:
		conn = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASSWD,db=MYSQL_DBNAME,port=MYSQL_PORT,charset='utf8')
		cur = conn.cursor()
	cur.execute(mysql_str)
	for data in cur.fetchall():
	    return data[0],data[1]
	return None,None

def main():
	global MYSQL_HOST, MYSQL_DBNAME, MYSQL_USER, MYSQL_PASSWD , MYSQL_PORT , latitude , longitude , max_range , config , twitter , result_count, conn , cur
	#last_id = get_last_id(conn,cur)
	#print last_id
	#twitter_id_max,twitter_time_max = get_now_id(conn,cur) # 标记点1
	#print "twitter_id_max",twitter_id_max
	last_id = None

	k = 0 #标志位计算是否是第一个的
	while 1:
		# perform a search based on latitude and longitude
		# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
		k += 1
		try:
			print "begin",time.ctime()
			query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id,timeout =10)
			print last_id,time.ctime()
		except Exception,e:
			print Exception,e
			time.sleep(10)
			continue

		for result in query["statuses"]:
			#print result
			#time.sleep(100)
			# only process a result if it has a geolocation
			if result["geo"]:
				try:
					if(k == 1):
						begin_time = result['created_at']
					user = result["user"]["screen_name"]
					text = result["text"]
					#text = text.encode('ascii', 'replace')
					twitter_id = result['id']
					latitude = result["geo"]["coordinates"][0]
					longitude = result["geo"]["coordinates"][1]

					full_name = result['place']['full_name'] # 地点全名
					result_type = result['metadata']['result_type'] #返回类型，例如最新的
					created_at = result['created_at'] # 推文创建时间
					#user = result["user"]["screen_name"] # 屏幕名字。。这个待定似乎和用户名一致
					profile_background_image_url = result["user"]["profile_background_image_url"]#配置背景图片
					description = result["user"]["description"]#用户描述

					user_id = str(result["user"]["id"])#用户id
					verified = result["user"]["verified"]#用户是否认证

					expanded_url = str(result["user"]["entities"]) #该部分内容多，难以详细区分
					profile_image_url_https = result["user"]["profile_image_url_https"]#配置文件图片
					user_name = result['user']['name']#作者名
					followers_count = result['user']['followers_count']#粉丝数量
					user_created_at = result['user']['created_at']  # 用户创建时间
					iso_language_code = result['metadata']['iso_language_code']
					# now write this row to our CSV file
					author = 'ly'
					row = [
						user, text, latitude, longitude ,full_name,result_type ,created_at ,
						profile_background_image_url,description ,user_id,expanded_url,profile_image_url_https,
						user_name, followers_count, user_created_at,verified,author,iso_language_code,twitter_id
					]
				except Exception,e:
					print Exception,e

				#for e in row:
				#	print type(e),e
				print "created_at:",created_at
				print "twitter_id:",twitter_id
				print "user:",user
				print "latitude,longitude:",latitude,longitude

				print '\n********************************\n'

				try:
					insert_ll((user, text, latitude, longitude ,full_name,result_type ,created_at ,
					profile_background_image_url,description ,user_id,expanded_url,profile_image_url_https,
					user_name, followers_count, user_created_at,author,iso_language_code,verified,twitter_id),conn,cur)

				except MySQLdb.Error,e:
				    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

				result_count += 1

			last_id = result["id"] #获取id用于下一次爬去
			#if(int(last_id) <= int(twitter_id_max)):#此部分和标记点1是联动的,两边同时去掉注释可以让每次采集的不重复
				#print "*"*60
				#now_craeate_time = result['created_at']
				#print "当前推文id小于表中最大id，可能发生重复采集 程序停止",last_id,twitter_id_max,time.ctime()
				#print "当前采集区间为：",begin_time,"  to  ",now_craeate_time

				#time.sleep(20)
				#return 0

		print "got %d results" % result_count

		time.sleep(10)

if __name__ == '__main__':
	main()
