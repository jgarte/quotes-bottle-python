from bottle import route, run
from quotes import get_quote

@route('/')
def home():
    quote = get_quote()
    return f"{quote[0]} -- {quote[1]}"

@route('/json')
def json_quote():
    quote = get_quote()
    return {
        'quote': quote[0],
        'author': quote[1]
    }


run(host='localhost', port=8080, debug=True, reloader=True)