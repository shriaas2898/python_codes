import bs4,requests
def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    elems = soup.select("#priceblock_ourprice")
    return elems[0].text.strip()


price = getAmazonPrice("https://www.amazon.in/Racemos-X550C-Asus/dp/B07689J5X8?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_CjwKCAjwpeXeBRA6EiwAyoJPKgTWMI8iX010OtmYS3LsBLDC49UcwMyFRjx2XhZ28twSp-9dPlew-RoCUjIQAvD_BwE_k_&gclid=CjwKCAjwpeXeBRA6EiwAyoJPKgTWMI8iX010OtmYS3LsBLDC49UcwMyFRjx2XhZ28twSp-9dPlew-RoCUjIQAvD_BwE")
print("Price on amazon : "+price)
