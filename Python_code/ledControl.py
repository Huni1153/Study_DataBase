import os
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from ledModels import ledDB
from ledModels import ledTable

from flask_wtf.csrf import CSRFProtect
from .ledForms import LedForm

app=Flask(__name__)

@app.route('/led', methods=['GET','POST'])
def led():
    form = LedForm()
    if form.validate_on_submit():
        session['led'] = form.data.get('led')
        return redirect('/led')

    return render_template('ledControl.html', form=form)

# html을 컨트롤러에서 만들어서 View로 전달하는데 컨트롤러와 View를 분리


if __name__ == "__main__":

    basedir=os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))
    dbfile=os.path.join(basedir,'../DB_code/ledDB.sqlite')
    print('file:{}'.format(dbfile))

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SECRET_KEY']='dkjghdfakgjhdfkg'  #임의의 문자열 넣는다.

    csrf = CSRFProtect()
    csrf.init_app(app)

    ledDB.init_app(app)
    ledDB.app = app
    ledDB.create_all()
    app.run(host='0.0.0.0', port=5007, debug=True)