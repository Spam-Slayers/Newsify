from flask import Flask,render_template,request,redirect
import sourceTemp as sr
import casedata as cd

app = Flask(__name__)


@app.route('/home')
def Newsify_DashBoard():
    cases=cd.alldata["cases"]
    deaths=cd.alldata["deaths"]
    recovered=cd.alldata["recovered"]
    active=cd.alldata["active"]

    globalcases = cd.globaldatas["cases"]
    globaldeaths = cd.globaldatas["deaths"]
    globalrecovered = cd.globaldatas["recovered"]
    globalactive = cd.globaldatas["active"]

    return render_template('home.html',cases=cases,deaths=deaths,recovered=recovered,active=active,globalcases=globalcases,globaldeaths=globaldeaths,globalrecovered=globalrecovered,globalactive=globalactive)

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
        latest_news=a["latest_news"]



    return render_template('result.html', truth = truth,intersection=intersection,links=links,latest_news=latest_news)


if __name__ == '__main__':
    app.debug = True
    app.run()
