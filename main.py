import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
pattern = re.compile("(age)...")


def main(name):
    data_dict = {}
    try:
        driver.get(f"https://www.google.com/search?q={name}")
        elems = driver.find_elements(By.CSS_SELECTOR, ".rVusze")
        occup = driver.find_element(By.CSS_SELECTOR, ".x7XAkb")
        for elem in elems:
            data = elem.text.split(":")
            data_dict[data[0]] = data[1]

        data_dict['occupation'] = occup.text
        print(data_dict)
        m1 = pattern.search(str(data_dict))
        if m1:
            print(m1.group().split(" ")[1])
    except Exception as e:
        print(e)
        print("clossing")
        driver.close()
    finally:
        print("process completed")
        driver.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main("donald trump")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
