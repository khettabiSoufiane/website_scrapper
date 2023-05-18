# import modules

import requests
from bs4 import BeautifulSoup

# Select a website to scraper

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article")

for book in books:
    # Extract book details
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    price = book.find("p", class_="price_color").text
    instock = book.find("p", class_="availability").text.strip()
    print(f"The title of the book is {title}, it has a rating of {rating} stars, the price is {price}, and it is {instock}.")