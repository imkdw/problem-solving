import datetime
now = datetime.datetime.now()
month = "0" + str(now.month) if len(str(now.month)) == 1 else now.month
print(f'{now.year}\n{month}\n{now.day}')