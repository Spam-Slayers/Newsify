import requests
import plotly.graph_objects as go
import plotly.io as pio




india=requests.get('https://api.covid19india.org/data.json')
globaldata=requests.get('https://corona.lmao.ninja/v2/all?yesterday=true')
current_data=india.json()
globaldatas=globaldata.json()
alldata=current_data["statewise"][0]
#list
def getCasesTimeSeries(d):
    date = []
    totalconfirmed = []
    totaldeceased = []
    totalrecovered = []

    for i in d['cases_time_series']:
        date.append(i.get('date'))
        totalconfirmed.append(i.get('totalconfirmed'))
        totaldeceased.append(i.get('totaldeceased'))
        totalrecovered.append(i.get('totalrecovered'))
    return date,totalconfirmed,totaldeceased,totalrecovered



alllist=getCasesTimeSeries(current_data)


#date=current_data["date"]
# dat =]
#for i in range(0,len(current_data)):
 #   dat = dat.append(current_data[i]["date"])
#print(dat)
# 1 2 3 45 6

#graph generation


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=alllist[0],
    y=alllist[1],
    name = '<b>Total Cases</b>', # Style name/legend entry with html tags
    connectgaps=True # override default to connect the gaps
))
fig.add_trace(go.Scatter(
    x=alllist[0],
    y=alllist[2],
    name='Total deaths',
))
fig.add_trace(go.Scatter(
    x=alllist[0],
    y=alllist[3],
    name='Recovered',
))

pio.write_html(fig, file='templates/graph.html', auto_open=False)