import datetime
now=datetime.datetime.now()
print(now)
print(type(now))
#we can look at the indiviual part of the date
print(now.year)
#We can use the time datadelta class to calculate the date in the future or the past 
print(now + datetime.timedelta(days=28))