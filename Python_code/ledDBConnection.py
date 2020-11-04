from Python_code.models import *
import datetime


def dbConnect(red, green, yellow):

    temp = datetime.datetime.now()
    time = temp.strftime("%Y-%m-%d-%H:%M:%S")

    ledTable = LedTest()
    ledTable.red = red
    ledTable.green = green
    ledTable.yellow = yellow
    ledTable.time = time

    db.session.add(ledTable)
    db.session.commit()