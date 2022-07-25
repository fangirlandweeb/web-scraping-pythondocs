from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

CHROME_DRIVER_PATH = Service("C:\Development\chromedriver.exe")
# UPCOMING_EVENTS_XPATH = "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul" xpath doesn't work in this case.. heehee *^-^
CSS_SELECTOR = "css selector"
PYDOCS_URL = "https://www.python.org/"

driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)
driver.get(PYDOCS_URL)

upcoming_news_titles = driver.find_elements(by=CSS_SELECTOR, value=".event-widget .shrubbery .menu li a")
for news in upcoming_news_titles:
    print(news.text)

upcoming_news_times = driver.find_elements(by=CSS_SELECTOR, value=".event-widget .shrubbery time")
for time in upcoming_news_times:
    print(time.text)

upcoming_news = {}
for i in range(len(upcoming_news_times)):
    upcoming_news[i] = {
        "time": upcoming_news_times[i].text,
        "news": upcoming_news_titles[i].text
    }
print(upcoming_news)

driver.quit()
