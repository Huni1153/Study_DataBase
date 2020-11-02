import os
from flask import Flask
from flask import render_template
from models import db

app = Flask(__name__)

# @app.route('/register')
# def register():
#     return render_template('register.html')

@app.route('/')
def hello():
    return render_template('login.html')

if __name__ == "__main__":
    print('hello')
    basedir = os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))
    dbfile = os.path.join(basedir,'../DB_code/db.sqlite')
    print('file:[]'.format(dbfile))
    # SQLITE Database uri address
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile

    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='0.0.0.0', port = 5007, debug= True)
