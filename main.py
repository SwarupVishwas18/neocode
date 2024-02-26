from distutils.log import debug
from fileinput import filename
from time import sleep
from flask import *
from utility.functions import findAlgo
from os.path import join

app = Flask(__name__, template_folder="templates")
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        print("POST")
        f = request.files["file"]
        f.save(join(app.config["UPLOAD_FOLDER"], f.filename))
        js_path = join(app.config["UPLOAD_FOLDER"], f.filename)
        with open(js_path) as f:
            code = f.read()
        print(code)
        try:
            code_name = findAlgo(code)
        except:
            print("Hola ")
        print("Code name : " + code_name)

        # sleep(300)
        code = code.split("\n")
        return render_template("better.html", code=code, code_name=code_name)
    return render_template("better.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
