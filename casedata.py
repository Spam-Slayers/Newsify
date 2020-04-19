import requests

india=requests.get('https://corona.lmao.ninja/v2/countries/India?yesterday=true&strict=true')
globaldata=requests.get('https://corona.lmao.ninja/v2/all?yesterday=true')
alldata=india.json()
globaldatas=globaldata.json()


#date=current_data["date"]
# dat =]
#for i in range(0,len(current_data)):
 #   dat = dat.append(current_data[i]["date"])
#print(dat)
# 1 2 3 45 6