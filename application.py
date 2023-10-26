from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("index.html")

@application.route("/etc")
def etc():
    return render_template("etc.html")

@application.route("/ewha")
def ewha():
    return render_template("ewha.html")

@application.route("/fashion")
def fashion():
    return render_template("fashion.html")

@application.route("/food")
def food():
    return render_template("food.html")

@application.route("/home")
def home():
    return render_template("home.html")

@application.route("/necessary")
def necessary():
    return render_template("necessary.html")

@application.route("/pencil")
def pencil():
    return render_template("pencil.html")



@application.route("/submit_item_post", methods=['POST'])
def reg_item_submit_post2():
    if request.method == 'POST':
        image_file=request.files["file"]
        image_file.save("static/images/{}".format(image_file.filename))
        data=request.form
        return render_template("result.html", data=data, img_path="static/images/{}".format(image_file.filename))

if __name__ == "__main__":
 application.run(debug=True)
