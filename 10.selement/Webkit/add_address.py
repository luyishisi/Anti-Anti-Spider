import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QGridLayout, QLineEdit, QWidget


class UrlInput(QLineEdit):
    def __init__(self, browser):
        super(UrlInput, self).__init__()
        self.browser = browser
        # add event listener on "enter" pressed
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        url = QUrl(self.text())
        # load url into browser frame
        browser.load(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create grid layout
    grid = QGridLayout()
    browser = QWebView()
    url_input = UrlInput(browser)
    # url_input at row 1 column 0 of our grid
    grid.addWidget(url_input, 1, 0)
    # browser frame at row 2 column 0 of our grid
    grid.addWidget(browser, 2, 0)

    # main app window
    main_frame = QWidget()
    main_frame.setLayout(grid)
    main_frame.show()

    # close app when user closes window
    sys.exit(app.exec_())

