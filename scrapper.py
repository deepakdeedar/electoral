import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from captcha import captcha_solver
import time


class Scrapper:

    def start(self, epic_id):

        url = "https://electoralsearch.in/"

        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get(url)

        driver.find_element_by_id('continue').click()

        tab1 = driver.find_element_by_css_selector("li[role='tab']")
        driver.execute_script("arguments[0].setAttribute('class','')", tab1)
        driver.execute_script("arguments[0].setAttribute('role','')", tab1)

        tab2 = driver.find_element_by_css_selector("li[role='tab']")
        driver.execute_script(
            "arguments[0].setAttribute('class','active')", tab2)
        tab2.click()

        driver.find_element_by_id('name').send_keys(epic_id)

        captcha_text = self.captchaSolver(driver)

        driver.find_element_by_id('txtEpicCaptcha').send_keys(captcha_text)
        time.sleep(2)

        driver.find_element_by_id('btnEpicSubmit').send_keys(Keys.ENTER)

        time.sleep(10)

        return self.extractData(driver)

    def captchaSolver(self, driver):
        driver.find_element_by_id("captchaEpicImg").screenshot('captcha.png')
        captcha_text = captcha_solver.get_captcha_text().replace(" \r\n",
                                                                 "").replace(" ", "")
        time.sleep(2)

        print(captcha_text)

        return captcha_text.replace('\n', '')

    def extractData(self, driver):

        result = []

        columns = ['c_id', 'epic_no', 'name', 'gender', 'age', 'rln_name', 'last_update', 'state', 'district',
                   'ac_name', 'ac_no', 'pc_name', 'ps_name', 'slno_inpart', 'st_code', 'ps_lat_long', 'part_no', 'part_name']

        c_id = driver.find_element_by_css_selector(
            "input[class='idInRow'][type='hidden']").get_attribute('value')
        epic_no = driver.find_element_by_css_selector(
            "input[class='epicNoInRow'][type='hidden']").get_attribute('value')
        result = [c_id, epic_no]

        for i in columns[2:]:
            x = driver.find_element_by_css_selector(
                f"input[name={i}][type='hidden']").get_attribute('value')
            result.append(x)

        return result
