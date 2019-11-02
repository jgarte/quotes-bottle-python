import random
import json

def get_quote():
    with open('quotes.json', 'r', encoding='utf8') as q:
        quotes = json.load(q)

    author = random.choice(list(quotes))
    quote = random.choice(quotes[author])
    return (quote,author)