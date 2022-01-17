from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/weathere/2.5/data/')
def temp():
   return render_template("Weather.json")
if __name__ == '__main__':
   app.run("0.0.0.0")
   
