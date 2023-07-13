from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
  return 'Hello World from Flask!'

@app.route('/search')
def do_search() -> str:
  return str(search4letters('Life and Everything'))

app.run()
