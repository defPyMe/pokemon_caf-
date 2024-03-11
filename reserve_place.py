from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import sys, os






def create_booking(day_of_month, num_of_guests):
    '''Create a reservation for Pokemon Cafe in Tokyo
    Keyword arguments:
    day_of_month -- day of the month to book
    num_of_guests -- number of guests to book (1-8)
    '''

    website = "https://reserve.pokemon-cafe.jp/"
    chrome_options = webdriver.EdgeOptions()
    chrome_options.add_experimental_option("detach", True)
    chromedriver = "edgedriver"
    driver = webdriver.Edge( options=chrome_options)
    driver.get(website)

    try:
        # 席の予約 HTML 1 - Make a reservation
        driver.execute_script("window.scrollTo(100,3200);")
   

        # 席の予約 HTML 2 - Agree T&C
        b = driver.find_element(By.XPATH, "//*[@class='agreeChecked']").click()
        c = driver.find_element(By.XPATH, "//*[@class='button']").click()

        # 席の予約 HTML 3 - Select number of guest
        d = select = Select(driver.find_element(By.NAME, 'guest'))
        e = select.select_by_index(num_of_guests)

        # 席の予約 HTML 4 - Select from calendar
        f = driver.find_element(By.XPATH, "//*[contains(text(), '次の月を見る')]").click()
        g = driver.find_element(By.XPATH, "//*[contains(text(), " + str(day_of_month) + ")]").click()
        h = driver.find_element(By.XPATH, "//*[@class='button']").click()
        
    except Exception as e :
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)



num_iterations = 1
day_of_month='11'
num_of_guests=2

[create_booking(day_of_month, num_of_guests) for x in range(num_iterations)]