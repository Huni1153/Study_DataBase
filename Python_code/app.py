import os
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import render_template
from ledController import ledControl
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm
from models import db


app=Flask(__name__)



@app.route('/led/<color>/<mode>')
def led(color,mode):

    if 'r' in color  or 'g' in color  or 'y' in color:
        ledControl(color,int(mode))
    else:
        print()
        #return redirect('/errorPage')


    return redirect('/')

@app.route('/errorPage')
def errorPage():

    return reder_template('/errorPage')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')
        print("login_sumit")
        return redirect('/')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

# /127.0.0.1 '/register' URI address
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()

    if request.method=='POST':
        if form.validate_on_submit():
            myuser = Myuser()
            myuser.userid = form.data.get('userid')
            myuser.username = form.data.get('username')
            myuser.password = form.data.get('password')

            db.session.add(myuser)
            db.session.commit()

            return redirect('/')
        else:
            print('retry')

    return render_template('register.html', form=form)


# /127.0.0.1 '/'
@app.route('/')
def hello():
    userid = session.get('userid', None)
    print(userid)
    return render_template('hello.html',userid=userid)


if __name__ == "__main__":

    basedir=os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))
    dbfile=os.path.join(basedir,'../DB_code/db.sqlite')
    print('file:{}'.format(dbfile))

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SECRET_KEY']='dkjghdfakgjhdfkg'  

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='0.0.0.0', port=5007, debug=True)
