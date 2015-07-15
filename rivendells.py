import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_blog():
    return redirect('http://rivendellsbloggen.blogspot.com', code=302)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(host=host, port=port)    