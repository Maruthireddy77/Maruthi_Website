import requests
from bs4 import BeautifulSoup
import sqlite3
import re




def clear_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products")
    conn.commit()
    conn.close()
    print("Old data cleared!")


def save_product(title, price, link, image_link):
    try:
        price_num = float(re.sub(r'[^0-9.]', '', price))
    except:
        price_num = 0.0

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products (title, price, link, image_link, price_num)
        VALUES (?, ?, ?, ?, ?)
    """, (title, price, link, image_link, price_num))

    conn.commit()
    conn.close()


def scrape_electronics():
    url = "https://books.toscrape.com/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".product_pod")

    for item in items:
        title = item.h3.a["title"]
        price = item.select_one(".price_color").text
        link = "https://books.toscrape.com/" + item.h3.a["href"]

        # ⭐ ADD IMAGE SCRAPING
        image_link = "https://books.toscrape.com/" + item.img["src"].replace("../", "")

        save_product(title, price, link, image_link)

    print("Electronics scraped!")


if __name__ == "__main__":
    clear_database()
    scrape_electronics()

