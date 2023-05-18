import requests
from bs4 import BeautifulSoup

def scrape_books():
    """
    Scrapes book information from a website and prints the details.

    Returns:
        None
    """

    # Select a website to scrape
    url = "https://books.toscrape.com/"

    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all books
    books = soup.find_all("article")

    for book in books:
        # Extract book details
        title = book.select_one("h3 a")["title"]
        rating = book.select_one("p.star-rating")["class"][1]
        price = book.select_one("p.price_color").text
        availability = book.select_one("p.availability").text.strip()

        # Print book information
        print(f"The title of the book is {title}, it has a rating of {rating} stars, the price is {price}, and it is {availability}.")


# Main execution
if __name__ == "__main__":
    scrape_books()
