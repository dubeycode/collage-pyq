from flask import Flask ,render_template


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
#--------------------------------work on 1 year ------------------------------------#
@app.route("/bsc1")
def bsc():
    return render_template("bsc1.html")
#--------------------------------work on 2 year ------------------------------------#
@app.route("/bsc2")
def bsc_second():
    return render_template("bsc2.html")
#--------------------------------work on 3 year ------------------------------------#
@app.route("/bsc3")
def bsc_3():
    return render_template("bsc.html")

@app.route("/about")
def about():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)