import requests #module used to pull html from a website
from bs4 import BeautifulSoup #allows us to work with html in python
from time import sleep #allows us to delay things a little
from random import choice 

BASE_URL = 'http://quotes.toscrape.com'

def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url: 
        response = requests.get(BASE_URL+url)
        print(f"Scraping: {BASE_URL}{url}")
        soup = BeautifulSoup(response.text, "html.parser") #getting the soup version that is nav 

        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").text,
                "author": quote.find(class_="author").text,
                "link": quote.find("a")["href"]
            })

        next_btn = soup.find(class_= "next") 
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(1)
        return all_quotes

def start_game(quotes):
    quote = choice(quotes)
    rem_guesses = 4
    guess = ""

    print("Here is a quote: ")
    print(quote["text"])

    while guess.lower() != quote["author"].lower() and rem_guesses:
        guess = input(f"Who said this? *guesses remaining {rem_guesses}\n")
        if guess.lower() == quote["author"].lower():
            print("Right!")
            break

        rem_guesses -= 1
        if rem_guesses == 3:
            r = requests.get(f'{BASE_URL}{quote["link"]}')
            soup = BeautifulSoup(r.text, 'html.parser')
            dob = soup.find(class_="author-born-date").text
            print(f"They were born on: {dob}")
        elif rem_guesses == 2:
            r = requests.get(f'{BASE_URL}{quote["link"]}')
            soup = BeautifulSoup(r.text, 'html.parser')
            pob = soup.find(class_="author-born-location").text
            print(f"They were born in: {pob}")
        elif rem_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Their name starts with a '{quote['author'][0]}' and a '{last_initial}'")
        else:
            print(f"Sorry, you ran out of guesses. It was: {quote['author']}")

    play = ''
    while play.lower() not in ('y', 'yes', 'n', 'no'):
        play = input("Play Again? ")
    if play.lower() in ('y', 'yes'):
        return start_game(quotes)
    else:
        print("Okay, Bye then.")

quotes = scrape_quotes()
start_game(quotes)