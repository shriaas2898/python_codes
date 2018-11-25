import bs4, requests,os

def download_image(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.select('#comic > img:nth-of-type(1)')
    if elems == []:
        print("No Images found")
    else:
         try:
             url = 'http:' + elems[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (url))
             res = requests.get(url)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             download_image(url)
         imageFile = open(os.path.join('xkcd',os.path.basename(url)),"wb")
         for chunk in res.iter_content(100000):
            imageFile.write(chunk)
         imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    download_image(url)

download_image("https://xkcd.com/2066")
