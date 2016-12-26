# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import requests
import json
import openpyxl
import codecs


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 675)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 511, 601))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 6, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(540, 140, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(540, 60, 51, 31))
        self.label_3.setObjectName("label_3")
        self.province_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.province_comboBox.setGeometry(QtCore.QRect(590, 60, 231, 31))
        self.province_comboBox.setObjectName("province_comboBox")
        self.city_comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.city_comboBox.setGeometry(QtCore.QRect(590, 140, 231, 31))
        self.city_comboBox.setObjectName("city_comboBox")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(530, 220, 61, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(590, 220, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.crawl_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.crawl_pushButton.setGeometry(QtCore.QRect(590, 290, 231, 71))
        #self.crawl_pushButton.setStyleSheet("background:rgb(255, 213, 127)")
        self.crawl_pushButton.setObjectName("crawl_pushButton")
        self.save_pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.save_pushButton_2.setGeometry(QtCore.QRect(590, 400, 231, 71))
        #self.save_pushButton_2.setStyleSheet("background:rgb(255, 213, 127)")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(530, 500,231, 71))
        self.label_5.setObjectName("label_5")
        self.save_pushButton_2.setObjectName("save_pushButton_2")
        self.label_rate=QtWidgets.QLabel(self.centralWidget)
        self.label_rate.setGeometry(QtCore.QRect(590, 500, 231, 71))
        self.label_rate.setObjectName("label_rate")
        self.clear_button = QtWidgets.QPushButton(self.centralWidget)
        self.clear_button.setGeometry(QtCore.QRect(530, 615, 51, 25))
        self.clear_button.setObjectName("clear_button")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 865, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "采集结果："))
        self.label_2.setText(_translate("MainWindow", "城市："))
        self.label_3.setText(_translate("MainWindow", "省份："))
        self.label_4.setText(_translate("MainWindow", "关键词："))
        self.label_5.setText(_translate("MainWindow", "进度："))
        self.crawl_pushButton.setText(_translate("MainWindow", "采集"))
        self.save_pushButton_2.setText(_translate("MainWindow", "导出"))
        self.clear_button.setText(_translate("MainWindow", "清空"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.action.setText(_translate("MainWindow", "退出"))


class BaiduMap(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(BaiduMap,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("百度地图采集器")
        self.cities={}
        self.provinces={}
        self.result=[]
        self.base_init()


    def base_init(self):
        self.action.triggered.connect(self.close)
        self.clear_button.clicked.connect(self.clear)
        self.crawl_pushButton.clicked.connect(self.crawl)
        self.save_pushButton_2.clicked.connect(self.write_to_excel)
        self.province_comboBox.currentIndexChanged.connect(self.comboBox_change)
        self.load_cities()

    def comboBox_change(self):
        self.city_comboBox.clear()
        province=self.province_comboBox.currentText()
        for city in self.provinces[province]:
            self.city_comboBox.addItem(city)

    def load_cities(self):
        for line in codecs.open('cities','r',encoding='utf-8'):
        #for line in open('cities','r','utf-8'):
            items=line.replace('\n','').split('---')
            self.cities[items[1]]=items[2]
            try:
                self.provinces[items[0]].append(items[1])
            except:
                self.provinces[items[0]]=[items[1]]
        for key in self.provinces:
            self.province_comboBox.addItem(key)

    def clear(self):
        self.result.clear()
        self.list_show()

    def list_show(self):
        self.listWidget.clear()
        for item in self.result:
            self.listWidget.addItem(item[2])

    def write_to_excel(self):
        excel=openpyxl.Workbook(write_only=True)
        sheet=excel.create_sheet('table')
        for item in self.result:
            sheet.append(item)
        filename=time.strftime("%Y%m%d_%H%M%S")+'.xlsx'
        excel.save(filename)

    def rate_of_advance(self,string):
        self.label_rate.setText(string)

    def insert2list(self,crawl_result):
        for item in crawl_result:
            self.result.append(item)
        self.list_show()

    def crawl(self):
        keyword=self.lineEdit.text()
        province=self.province_comboBox.currentText()
        city=self.city_comboBox.currentText()
        if keyword.replace(' ','')=='':
            return
        citycode=self.cities[city]
        self.crawler=Crawler(keyword,province,city,citycode)
        self.crawler._finish_signal.connect(self.insert2list)
        self.crawler._page_ok_signal.connect(self.rate_of_advance)
        self.crawler.start()

class Crawler(QtCore.QThread):
    _finish_signal=QtCore.pyqtSignal(list)
    _page_ok_signal=QtCore.pyqtSignal(str)
    def __init__(self,keyword,province,city,code):
        super(Crawler,self).__init__()
        self.keyword=keyword
        self.province=province
        self.city=city
        self.code=code
        self.headers = {
            'Host':"map.baidu.com",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

    def run(self):
        self.result=[]
        page=1
        keys=['name','addr','std_tag','tel']
        while True:
            try:
                data=self.search(self.keyword,self.code,page)
            except:
                break
            if data==[]:
                break
            for line in data:
                item=[self.province,self.city]
                for key in keys:
                    try:
                        item.append(line[key])
                    except:
                        item.append('')
                self.result.append(item)
            self._page_ok_signal.emit(self.city+' --- Page '+str(page)+' --- ok')
            page+=1
            time.sleep(0.5)
        self._page_ok_signal.emit(self.city+' yes')
        self._finish_signal.emit(self.result)

    def search(self,keyword,citycode,page):
        html=requests.get('http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=baidu&pcevaname=pc4.1&qt=con&from=webmap&c='+str(citycode)+'&wd='+keyword+'&wd2=&pn='+str(page)+'&nn='+str(page*10)+'&db=0&sug=0&addr=0&&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=12&tn=B_NORMAL_MAP&u_loc=12736591.152491,3547888.166124&ie=utf-8',headers=self.headers).text
        data=json.loads(html)['content']
        return data

if __name__ == '__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    management=BaiduMap()
    management.show()
    sys.exit(app.exec_())
