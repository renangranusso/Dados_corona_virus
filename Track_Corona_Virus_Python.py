from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from time import sleep

url = "https://www.coronatracker.com/pt-br/"

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
sleep(3)

#Traz os dados de forma seca, sem limpar as tags
cases = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')
curados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
mortes = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')



#Transforma o dado em texto
casestext = cases.text
curadostext = curados.text
mortestext = mortes.text
print('total de casos de covid: ', casestext)
print('total de casos curados : ', curadostext)
print('total de mortes        : ', mortestext)

mortestext = mortestext.replace(".", "")
casestext = casestext.replace(".", "")

letalidade = int(mortestext) / int(casestext)

letalidade = letalidade * 100

print('Letalidade do virus no mundo: %.2f' % letalidade, '%')
print("")

rows = driver.find_elements_by_tag_name("tbody")

for row in rows:
    col = row.find_elements_by_tag_name("tr")
    for val in col:
        if val.text != "":
            print(val.text)

driver.close()
driver.quit()
