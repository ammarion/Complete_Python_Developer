from selenium import webdriver


chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name("btn-default")
print(show_message_button.get_attribute("innerHTML"))

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_button2 = chrome_browser.find_element_by_css_selector("#get-input > .btn")
print(user_button2)
user_message.clear()
user_message.send_keys("I am EXTRA COOOL")

show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")
print(output_message)

assert "I am EXTRA COOOL" in output_message.text

chrome_browser.close()
