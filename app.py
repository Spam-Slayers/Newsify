from flask import Flask,render_template,request,redirect
import sourceTemp as sr
import casedata as cd

app = Flask(__name__)


@app.route('/home')
def Newsify_DashBoard():
    cases=cd.alldata["confirmed"]
    deaths=cd.alldata["deaths"]
    recovered=cd.alldata["recovered"]
    active=cd.alldata["active"]



    return render_template('home.html',cases=cases,deaths=deaths,recovered=recovered,active=active)

@app.route('/')
def redirection():
    return redirect('/home')

@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        newsTitle=request.form['newsTitle']


        a=sr.supreme(newsTitle)
        truth=a["truthfulness"]
        links=a["links"]
        intersection=a["intersection"]
        latest_links=a["latest_links"]



    return render_template('result.html', truth = truth,intersection=intersection,links=links,latest_links=latest_links)
@app.route('/visualization',methods=['POST'])
def graph():
    return render_template('graph.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
