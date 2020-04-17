from bs4 import BeautifulSoup
import requests, re

s = requests.session()
web = s.get('https://nhentai.net/g/308973/').text
html = BeautifulSoup(web,'html.parser')
elemen = html.find('div',{'id':'info'})

judul = elemen.find('h1').text
subjudul = elemen.find('h2').text

print(f"{judul}\n{subjudul}")

for section in elemen.findAll('div',{'class':'tag-container field-name'}):
  print(re.sub('\s+', '',section.findAll(text=True, recursive=False)[0]))
  for a in section.findAll('a'):
    print(f"- {a.text}")

print(elemen.find(text=re.compile(r'page')))
print(elemen.find('time').text)
