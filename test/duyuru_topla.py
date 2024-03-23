from selenium import webdriver
from selenium.webdriver.firefox.options import Options as fo
from bs4 import BeautifulSoup
import pandas as pd


ayarlar = fo()
surucu = webdriver.Firefox(options=ayarlar,executable_path="geckodriver")

surucu.get("http://www.meb.gov.tr/meb_duyuruindex.php")

kaynak = surucu.page_source
# surucu.close()

print(kaynak)

duyurular = BeautifulSoup(kaynak,"lxml")

duyurular = duyurular.find_all("tr",attrs={"role":"row"})

tarih=[]
baslik=[]
for duyuru in duyurular:
    try:
        duyuru_tarihi = duyuru.find_all("td")[2].text
        duyuru_baslik = duyuru.find_all("td")[1].text
        print(duyuru_tarihi,duyuru_baslik)
        tarih.append(duyuru_tarihi)
        baslik.append(duyuru_baslik)
    except:
        pass

surucu.find_element_by_id("/html/body/section[2]/div/div/div/div/div/div/div[3]/div[2]/div/ul/li[9]/a").click()
veri = {"tarih":tarih,"başlık":baslik}

df = pd.DataFrame(veri)
df.to_csv("duyurular.csv")