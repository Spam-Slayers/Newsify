import requests

r=requests.get('https://api.covid19india.org/data.json')
alldata=r.json()
current_data=alldata["cases_time_series"][-1]
#print(current_data)
#date=current_data["date"]
# dat =]
#for i in range(0,len(current_data)):
 #   dat = dat.append(current_data[i]["date"])
#print(dat)
# 1 2 3 45 6