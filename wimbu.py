import os, sys, bs4, time, random, threading, urllib.request

cnt = (0)
url = [ ]

try:
    nukelink = (f'https://nhentai.net/g/{sys.argv[1]}')
except IndexError:
    sys.exit('[?] Wibu tolol, mana kode nuklirnya bgsd')

def downloader(url):
    global cnt
    cnt += (1)
    url = url.replace('t.','i.').replace(f'{cnt}i.',f'{cnt}.')
    urllib.request.urlretrieve(url, f'{sys.argv[1]}/{cnt}.png')

def get_link(urls):
    global url
    agent = open('user_agent.txt').readlines()
    headr = {'user-agent':random.choice(agent).strip()}
    r = urllib.request.Request(urls, headers=headr)
    s = bs4.BeautifulSoup(urllib.request.urlopen(r), 'html.parser')
    for div in s.find_all('div', class_='thumb-container'):
        for a in div.find_all('a', class_='gallerythumb'):
            for img in a.find_all('img', class_='lazyload'):
                url.append(img.get('data-src'))

getlink = threading.Thread(target=get_link,args=(nukelink,))
getlink.start()
while getlink.is_alive():
   for load in ['.','..','...']:
       print (f'\r[*] Getting link{load}',end='   ',flush=True)
       time.sleep(0.3)
print (f'\n[*] Success get {len(url)} link')
try:
    os.mkdir(sys.argv[1])
except:pass
for link in url:
    download = threading.Thread(target=downloader, args=(link,))
    download.start()
    while download.is_alive():
        for load in '-\|/-\|/':
            print (f'\r[*] Downloading {cnt}/{len(url)} {load} ',end='',flush=True)
            time.sleep(0.1)
print ('\n[*] Done, wibu tolol btw')