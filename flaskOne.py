from datetime import datetime

from flask import Flask , render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app=Flask(__name__,template_folder='template')
Bootstrap(app)
Moment(app)


@app.route("/")
def index():
    date = datetime.now()
    return render_template('index.html',current_time=datetime.now)

if __name__=="__main__":
    app.run(debug=True)
