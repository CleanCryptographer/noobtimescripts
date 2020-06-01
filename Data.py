import pandas as pd
import random
from datetime import datetime, time, timedelta



datelist = pd.date_range(start="2019-01-01",end="2020-01-01")

for i in datelist:
    file=open(str(i),"w+")

    check = i
    x = str(check)
    x = x.split(" ", 1)
    new = x[0]
    test = new.split('-', 3)
    year = int(test[0])
    month = int(test[1])
    day = int(test[2])
    ts = datetime(year=year, month=month, day=day, hour=00, minute=00, second=00)

    for j in range(1,719):

       file.write(str(ts)+" Temprature  "+str(random.randrange(15,40))+"  Humidity  "+str(random.randrange(60,100))+"\n")
       ts+=timedelta(minutes=2)

    file.close()
