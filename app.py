from flask import Flask,render_template,request,redirect
import sourceTemp as sr
import casedata as cd

app = Flask(__name__)


@app.route('/home')
def Newsify_DashBoard():
    totalconfirmed=cd.current_data["totalconfirmed"]
    totaldeceased=cd.current_data["totaldeceased"]
    totalrecovered=cd.current_data["totalrecovered"]
    dailyconfirmed=cd.current_data["dailyconfirmed"]
    dailydeceased = cd.current_data["dailydeceased"]
    dailyrecovered = cd.current_data["dailyrecovered"]
    return render_template('home.html',totalconfirmed=totalconfirmed,totaldeceased=totaldeceased,totalrecovered=totalrecovered,dailyconfirmed=dailyconfirmed,dailydeceased=dailydeceased,dailyrecovered=dailyrecovered)

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
