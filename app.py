from flask import Flask,render_template,request
import source as sr

app = Flask(__name__)


@app.route('/home')
def Newsify_DashBoard():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        newsTitle=request.form['newsTitle']
        keywords=request.form['keywords']

        a=sr.supreme(keywords,newsTitle)
        truth=a["truthfulness"]
        links=a["links"]



    return render_template('result.html', truth = truth,links=links)


if __name__ == '__main__':
    app.debug = True
    app.run()
