from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hongbooking')
def hongbooking():
    return render_template('hongbooking.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
    #app.run(host='0.0.0.0', port=5000, debug=True)