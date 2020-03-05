
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, post, get, template

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/bmi')
def bmiForm():
    return template("bmi.html")

@post('/results')
def results():
    return template("results.html")

@route('/zodiac')
def zodiacForm():
    return template("zodiac.html")

@post('/horoscope')
def horoscope():
    return template("horoscope.html")

application = default_app()

