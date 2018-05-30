from flask import Flask, render_template

app = Flask(__name__)

@app.route("/forloop")
def forloop():
	dates = forloopexample()
	return render_template("index.html", dates=dates)
def forloopexample():
    	result = {}
	for i in range(1,100,1):
        	result[str(i)] = i
	return result
if __name__ == '__main__':
    result = forloopexample()
    app.run(host='127.0.0.1',port=5050)
	
