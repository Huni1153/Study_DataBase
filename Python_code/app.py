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
    basedir = os.path.abspath(os.path.dirname(__file__))  #현재 파일이 실행되는 경로
    print('basedir:{}'.format(basedir))
    dbfile = os.path.join(basedir,'../DB_code/db.sqlite') # db파일이 저장되어있는 경로
    print('file:[]'.format(dbfile))
    # SQLITE Database uri address
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    # True로 설정하면 각 리퀘스트의 끝에 데이터베이스 변동사항을 자동 커밋한다.
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    # 개체 수정을 추적하고 신호를 방출한다. 일반적으로 잘 사용하지 않고 추가 메모리가 필요하여 False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='0.0.0.0', port = 5007, debug= True)
