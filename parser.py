import requests
from bs4 import BeautifulSoup as bs

print("Введите ссылку")
c = input()
url = c
f = open('data/'+c+'.txt', 'w')
r = requests.get(url)

soup = bs(r.text, "html.parser")
names = soup.find_all('li', class_ = 'listing-item')
print(len(names))
for name in names:
    url_s = name.a.get('href')
    r_s = requests.get(url_s)
    soup_s = bs(r_s.text, "html.parser")
    text = soup_s.find('div', class_ = 'entry-content poem-text')
    strings = text.find_all('p')
    s = ''
    for i in strings:
        for br in i('br'):
            br.replace_with('')
        if len(i.get_text())<1000:
            s+=i.get_text()
            s+='\n'
            print(s)
    
    try:
        f.write('\n')
        f.write(s)
    except:
        pass
f.close()
