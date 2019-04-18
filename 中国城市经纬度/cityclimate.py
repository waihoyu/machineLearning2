import time
from selenium import  webdriver
import pandas as pd
import  numpy as np
import os

city = pd.read_csv(r"Cityclimate.csv")

city.head()

cityname = city.iloc[:,0]

df= pd.DataFrame(index=cityname.index)
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver_x64.exe"
os.environ["webdriver.chrome.driver"]=chromedriver

driver = webdriver.Chrome()
time0 = time.time()

for num,city in enumerate(cityname):
    print(city)
    driver.get('https://www.google.co.uk/webhp?hl=en&sa=X&ved=0ahUKEwimtcX24cTfAhUJE7wKHVkWB5AQPAgH')
    # driver.get('https://www.google.com/')
    time.sleep(0.3)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('%s china latitude and longitude' %(city))
    search_box.submit()
    result = driver.find_element_by_xpath('//div[@class="Z0LcW"]').text
    resultsplit = result.split(" ")
    df.loc[num,"City"] = city
    df.loc[num,"Latitude"] = resultsplit[0]

    print("%i webcrawler successful for city %s" %(num,city))

time.sleep(1)
driver.quit()
print(time.time() - time0)




