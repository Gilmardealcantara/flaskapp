import urlparse
import datetime
from selenium import webdriver

def main():
    page = 'http://localhost:5000/'
    print "Crawling:", page
    crawl_page(page)

def crawl_page(page):
    i = datetime.datetime.now()
    driver = webdriver.PhantomJS()
    driver.get(page)
    driver.set_window_size(1024, 768)
    driver.save_screenshot('/home/fred/dev/projects/flaskapp/tmp/access_test - %s.png' % i)
    driver.quit()

if __name__ == "__main__":
    main()