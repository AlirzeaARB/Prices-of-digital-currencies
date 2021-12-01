import requests 
from bs4 import BeautifulSoup
import os

while True:
    os.system('cls')
    
    crypto=input('\nPlease enter the name of your digital currency : \n')

    url='https://coinmarketcap.com/currencies/{}/'.format(crypto)

    test_url=requests.get(url).status_code

    if test_url == 200:

        page=requests.get(url=url)

        soup=BeautifulSoup(page.content,'html.parser')

        rec=soup.find('div',{'class':'priceValue'}).text.replace('\n','').strip()

        print(rec+'\n')

    else:
        print('\nThere is no such digital currency\n\n')
    
    key_reload_or_exit = input('Press the R key to continue and the E key to exit : \n')

    if key_reload_or_exit == 'R':
        continue

    elif key_reload_or_exit == 'E':
        break