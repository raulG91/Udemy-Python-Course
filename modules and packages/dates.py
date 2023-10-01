import datetime
dt = datetime.datetime.now()

print(dt)
#Get year
print(dt.year)

#Format dates
dt2 = datetime.datetime.now()

print(dt2.isoformat())

print(dt2.strftime("%d/%m/%Y %H %M")) #14 hour format


#Sum dates
dt3 = datetime.datetime.now()
t = datetime.timedelta(days = 3)
# Sum 3 days 
print( dt3 + t)