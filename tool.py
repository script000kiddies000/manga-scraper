import requests, random, sys, os
from bs4 import BeautifulSoup as bs

cnt = (0)
url = []

try:
    link = (f'https://nhentai.net/g/{sys.argv[1]}')
except IndexError:
    sys.exit('[!] python tool.py 313337')

def get_link(urls, s):
    global url
    agent = open('user_agent.txt').readlines()
    # headr = {'User-Agent':random.choice(agent).strip()}
    # weeb = s.get(urls,headers=headr)
    weeb = s.get(urls).text
    s = bs(weeb, 'html.parser')
    for div in s.find_all('div', class_='thumb-container'):
        for a in div.find_all('a', class_='gallerythumb'):
            for img in a.find_all('img', class_='lazyload'):
                url.append(img.get('data-src'))

def downloader(url):
    global cnt, s
    cnt += (1)
    url = url.replace('t.','i.').replace(f'{cnt}i.',f'{cnt}.')
    file = s.get(url).content
    open(f'{sys.argv[1]}/{cnt}.png', 'wb').write(file)

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies

def get_session(proxy):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    # proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

def cek_proxy(proxies):
    for i in range(len(proxies)):
       session = get_session(proxies[i])
       print(f'\rmencoba proxy ke : [{i}] {proxies[i]}', end='      ', flush=True)
       # print(f'mencoba proxy ke : [{i}] {proxies[i]}',flush=True)
       try:
          #icanhazip.com
          session.get("https://i.nhentai.net", timeout=1.5).text.strip()
       except:
          continue
       break
    print(f'\nproxy di temukan: {proxies[i]}')
    return session


proxies = get_free_proxies()
s = cek_proxy(proxies)
get_link(link,s)


os.mkdir(sys.argv[1])
for l in url:
  downloader(l)
  print(f'\rsedang mendownload... [{cnt}]',end='',flush=True)

# gambar = s.get('https://t.nhentai.net/galleries/1604263/thumb.jpg').content
# with open('test_kukuku.jpg', 'wb') as handler:
#     handler.write(gambar)
