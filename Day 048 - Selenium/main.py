from selenium import webdriver

chrome_driver_path = "/Users/name/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

driver.quit()