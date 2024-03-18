from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, Flask!"

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/hongbooking')
# # def hongbooking():
# #     return render_template('hongbooking.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
    
#     #app.run(host='0.0.0.0', port=5000, debug=True)