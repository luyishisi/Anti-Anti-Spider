#coding:utf-8

#from ghost import Ghost
#ghost = Ghost()

#with ghost.start() as session:
#	page, extra_resources = session.open("http://jeanphix.me")
#	assert page.http_status == 200 and 'jeanphix' in page.content
#	print '111'

def Movepath(session, dist_src, x, y):

    try:
        result, ex_result = session.evaluate(
            '''
                var event  = document.getElementsByClassName("gt_slider_knob gt_show")[0];
                var evt = document.createEvent('MouseEvent');
                evt.initMouseEvent('mousedown',true, true, window, 0,
                0, 0, %s, %s, false, false, false, false, 0, null);
                event.dispatchEvent(evt);
            '''% (x, y + random.uniform(1, 2)), expect_loading=False)
        # print result
    except Exception, e:
        print "Click Error:", e

    session.sleep(random.uniform(0, 0.0001))
    dist_all = 0.0
    step = random.randint(4, 10)
    flag = 1
    while True:
        print dist_all, step
        dist_all += step
        try:
            result, ex_result = session.evaluate(
                '''
                    var event  = document.getElementsByClassName("gt_slider_knob gt_show moving")[0];
                    var evt = document.createEvent('MouseEvent');
                    //event.style.left = '100px'
                    evt.initMouseEvent('mousemove',true, true, window, 0,
                    0, 0, %s, %s, false, false, false, false, 0, null);
                    event.dispatchEvent(evt);
                '''% (x + dist_all, y + random.uniform(1, 4)), expect_loading=False)
            # print result
        except Exception, e:
            print e

        if dist_all > dist_src :
            session.sleep(random.uniform(0, 0.001))
            break
        elif (dist_src-dist_all) <3:
            step = 6
            time.sleep(random.uniform(0.2, 0.4))
        elif dist_all > 9*dist_src/10:
            step = random.randint(1*dist_src/30, 4*dist_src/30)
            time.sleep(random.uniform(0.1, 0.4))
        elif (dist_all > 7.5*dist_src/10) and (dist_all < 8*dist_src/10):
            if flag < 2:
                step = -random.randint(1*dist_src/20, 3*dist_src/10)
                flag += 1
            else:
                step = random.randint(dist_src/20, 2*dist_src/10)
            time.sleep(random.uniform(0.2, 0.8))
        else:
            step = random.randint(1*dist_src/10, 3*dist_src/10)
            time.sleep(random.uniform(0.06, 0.5))
        session.sleep(random.uniform(0, 0.001))
