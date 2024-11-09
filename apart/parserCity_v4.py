
import sqlite3

from bs4 import BeautifulSoup
import requests
import decimal


class Apartment:
    def __init__(self, imageUrl, title, description, address, price, priceNumber):
        self.imageUrl = imageUrl
        self.title = title
        self.description = description
        self.address = address
        self.price = price
        self.priceNumber = priceNumber

    def __str__(self):
        return f"imageUrl: {self.imageUrl}, title: {self.title}, description: {self.description}, address: {self.address}, price: {self.price}, priceNumber: {self.priceNumber}"


def get_html(url):
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = session.get(url, headers=headers)
    return response.text


def parse_apartment(card):
    imageUrl = card.find('div', class_='card__img').find('div', class_='sc-sliderlight__track').find('a').find('img')[
        'data-src']
    # title = not card.find('div', class_='card-content').find('span', class_='object-hotel__type')
    title = card.find('div', class_='card-content').find('div').find('span').text
    description = card.find('div', class_='card-content').find('a', class_='card-content__object-type').text
    address = card.find('div', class_='card-content').find('div', class_='card-content__address').find('span',
                                                                                                       class_='text-muted js-pseudo-link').get_text().replace(
        '\n', ' ').replace('\r', '').replace('\t', '').strip()
    price_text = card.find('div', class_='card-prices').find('div', class_='card-prices__bottom').find('div',
                                                                                                       class_='price').find_all(
        'span')[1].text
    price = "".join(price_text.split('\xa0'))[:-1]
    if price == '':
        price = '0'
    return Apartment(imageUrl, title, description, address, price_text, price)


def parse_apartments(html):
    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all('div', class_='card')
    apartments = [parse_apartment(card) for card in cards]
    return apartments


def main(сi=None):
    cityUrls = {
        'Геленжик': 'https://gelendzhik.sutochno.ru/?from=mainpage',
        'Сириус': 'https://adler.sutochno.ru/sirius?from=mainpage',
        'Анапа': 'https://anapa.sutochno.ru/?from=mainpage',
        'Владивосток': 'https://vl.sutochno.ru/?from=mainpage',
        'Кисловодск': 'https://kislovodsk.sutochno.ru/?from=mainpage',
        'Краснодар': 'https://krasnodar.sutochno.ru/?from=mainpage',
        'Дагестан': 'https://mahachkala.sutochno.ru/region?from=mainpage',
        'Екатеринбург': 'https://ekaterinburg.sutochno.ru/?from=mainpage'}

    for city, url in cityUrls.items():
        html = get_html(url)
        apartments = parse_apartments(html)
        for apartment in apartments:
            print(f'city:{city}, {apartment}')

            conn = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()

            im = apartment.imageUrl
            address = apartment.address
            t = apartment.title
            d = apartment.description
            p = apartment.price
            pr = apartment.priceNumber 

            cursor.execute(
                """INSERT INTO cityApart_apartpars (imageUrl, city, address, name, descriptions, price, priceNumber) VALUES(?,?,?,?,?,?,?)""",
                (im, city, address, t, d, p, pr))
            conn.commit()


if __name__ == "__main__":
    main()
