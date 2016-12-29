#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geetest import BaseGeetestCrack
from selenium import webdriver


class ExpNormalGeetestCrack(BaseGeetestCrack):

    """工商滑动验证码破解类"""

    def __init__(self, driver):
        super(ExpNormalGeetestCrack, self).__init__(driver)

    def crack(self):
        """执行破解程序

        """
        self.move_to_element()
        x_offset = self.calculate_slider_offset()
        self.drag_and_drop(x_offset=x_offset)


def main():
    driver = webdriver.Chrome()
    driver.get("http://www.geetest.com/exp_normal")
    cracker = ExpNormalGeetestCrack(driver)
    cracker.crack()


if __name__ == "__main__":
    main()
