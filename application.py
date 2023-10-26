from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("index.html")

@application.route("/index", methods=['POST']) 
def reg_item_submit_post():
    # data=request.form
    # return render_template("result.html", data=data)                      
# @application.route("/index", methods=['POST'])
# def reg_item_submit_post():
    image_file=request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    data=request.form
    print(data)
    return render_template("result.html", data=data)


@application.route("/submit_item_post", methods=['POST'])
def reg_item_submit_post2():
    if request.method == 'POST':
        data = request.form
        return render_template("result.html", data=data)

if __name__ == "__main__":
 application.run(debug=True)
