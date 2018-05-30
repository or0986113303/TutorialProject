from flask import Flask, render_template
app = Flask(__name__)

agedirection = {'mir':33,'steven':30,'test':18}
groupstring = '[ mir , steven and test are very happy at mir\'s house ]'

@app.route('/findage/<user>')
def findage(user):
    return render_template('index.html', name = user, age = agedirection[user])

@app.route('/findinstring/<user>')
def findingroup(user):
    result = groupstring.find(user)
    return render_template('findstring.html',name = user, stringgroup = groupstring, index = result)

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=5050)