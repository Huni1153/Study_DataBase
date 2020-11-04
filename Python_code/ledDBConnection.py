from models import LedTest,db
import datetime


def dbConnect(red, green, yellow):

    time = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    ledTable = LedTest()
    ledTable.red = red
    ledTable.green = green
    ledTable.yellow = yellow
    ledTable.time = time

    db.session.add(ledTable)
    db.session.commit()
