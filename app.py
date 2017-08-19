import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainmenu():

    return """
    <html>
    <body>
    <center><h1>Hello World!</h1><br/>
    </body>
    </html>"""

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))