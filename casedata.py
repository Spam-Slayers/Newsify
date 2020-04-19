import requests




india=requests.get('https://api.covid19india.org/data.json')
globaldata=requests.get('https://corona.lmao.ninja/v2/all?yesterday=true')
current_data=india.json()
globaldatas=globaldata.json()
alldata=current_data["statewise"][0]


#date=current_data["date"]
# dat =]
#for i in range(0,len(current_data)):
 #   dat = dat.append(current_data[i]["date"])
#print(dat)
# 1 2 3 45 6