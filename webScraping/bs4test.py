from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from pyvirtualdisplay import Display
display=Display(visible=0,size=(800,600))
display.start()

def make_soup(url):
    req=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0"})
    data=req.content
    return bs(data,'lxml')

def img_download(url):
    soup=make_soup(url)
    images=soup.find_all("div",{"class":"rg_meta notranslate"})
    images=[i.text for i in images]
    images=[json.loads(i) for i in images]
    if not os.path.exists('/home/iamlex/Desktop/webScraping/{}'.format(dataimg)):
        os.mkdir('/home/iamlex/Desktop/webScraping/{}'.format(dataimg))
    
    for i in len(images):
        with open('/home/iamlex/Desktop/webScraping/{}/{}'.format(dataimg,images[i]["ou"].split('/')[-1])) as f:
            f.write(requests.get(images[i]["ou"]).content)
    
def img_selenium(dataimg):
    driver=webdriver.Firefox()
    url='https://images.google.com/?gws_rd=ssl'
    time.sleep(1)
    driver.get(url)
    time.sleep(1)
    element=driver.find_element_by_name('q')
    element.send_keys(dataimg,Keys.RETURN)
    time.sleep(1)
    url=driver.current_url
    last_height=driver.execute_script('return document.body.scrollHeight')
    p=0
    for i in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(0.9)
        new_height=driver.execute_script("return document.body.scrollHeight")
        if new_height==last_height:
            p=p+1
            if(p==2):
                break
            driver.find_element_by_xpath("//input[@type='button']").click()
        last_height=new_height
    img_download(url)

img_selenium(sys.argv[1])