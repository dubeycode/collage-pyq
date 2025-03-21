from flask import Flask ,render_template


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
#--------------------------------work on 1 year bsc ------------------------------------#
@app.route("/bsc1")
def bsc():
    return render_template("bsc1.html")
#--------------------------------work on 2 year bsc ------------------------------------#
@app.route("/bsc2")
def bsc_second():
    return render_template("bsc2.html")
#--------------------------------work on 3 year bsc ------------------------------------#
@app.route("/bsc3")
def bsc_3():
    return render_template("bsc.html")
##########################################################################################
#--------------------------------work on 1 year bca ------------------------------------#
@app.route("/bca1")
def bca():
    return render_template("bca1.html")
#--------------------------------work on 2 year bca ------------------------------------#
@app.route("/bca2")
def bca_second():
    return render_template("bca2.html")
#--------------------------------work on 3 year bca ------------------------------------#
@app.route("/bsc3")
def bca_3():
    return render_template("bca3.html")



if __name__=="__main__":
    app.run(debug=True)