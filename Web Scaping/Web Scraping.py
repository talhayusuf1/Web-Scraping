import requests #Bu kutuphane baska bir siteden istek yapmamizi sagliyor    
from bs4 import BeautifulSoup #Bu kutuphane ise html kodlarini bize duzgun bir sekilde veriyor

Url= "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm" #veri cekecegimiz site
R=requests.post(Url)
Soup = BeautifulSoup(R.text,"html5lib")#Burda html kodlarini bs4 e ceviriyoruz
List=Soup.find("tbody",{"class":"lister-list"}).find_all("tr")#Filmlerin bulundugu listeyi bulup buraya yaziyoruz
for Film in List:
    Name =Film.find("td",{"class":"titleColumn"}).a.text#Isimlerini cekiyoruz
    Tarih = Film.find("td",{"class":"titleColumn"}).span.text.strip("()")#Tarihleri cekiyoruz   
    Rating = Film.find("td",{"class":"ratingColumn imdbRating"}).text.strip()#Ratingler cekiyoruz
    print("Film Adi>>"+Name+" Film Tarihi>> "+Tarih+" Film Ratingi>> "+Rating)