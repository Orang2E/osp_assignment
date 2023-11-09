from flask import Flask, jsonify, render_template


@app.route("/") #얘 주소로 가면 index.html 나오는 거
def index():
    return render_template('index.html')

@app.route("/mypage") #얘 주소로 가면 index.html 나오는 거
def mypage():
    return render_template('mypage.html')

@app.route("/product-add") 
def productAdd():
    return render_template('product_add.html')

@app.route("/product-detail")
def productDetail():
    return render_template('product-detail.html')

@app.route("/products-list")
def productsList():
    return render_template('products_list.html')

@app.route("/review-add") 
def reviewAdd():
    return render_template('review_add.html')

@app.route("/review-detail")
def reviewDetail():
    return render_template('review_detail.html')

@app.route("/reviews-list")
def reviewList():
    return render_template('reviews_list.html')


