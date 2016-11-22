#coding:utf-8
from ghost import Ghost
import time
ghost = Ghost()

user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2'
print '*'*100

with ghost.start(user_agent=user_agent,display=True,wait_timeout=30) as session:
    page, extra_resources = session.open("http://www.gatherproxy.com/zh/proxylist/country/?c=China")
    assert page.http_status == 200 and 'China' in page.content
    #print page.content

#    print page,extra_resources

#    body > form > p > input
    session.click('.button',0)
    #session.wait_for_page_loaded(timeout=20)
    session.sleep(9)
#    print page.content
#    session.show()

#    session.click('.button',0)

    #try:
    #    status, page_html = session.evaluate('gp.pageClick(7);')
    #except Exception,e:
    #    print Exception,e

    session.click('.inactive',0)
    session.sleep(6)

#    session.show()
    #print page_html.content
    session.click('.inactive',0)
    session.sleep(6)
    session.capture_to('header.png', )
