from selenium import webdriver
import time, os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Иванов")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Иван")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@mail.ru")

    input4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'in.txt')
    input4.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()
    assert True

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
