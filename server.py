from flask import Flask, render_template, redirect, request, session
import csv
app = Flask(__name__)


@app.route('/')
def route_index():
    return route_edit()


@app.route('/story')
def route_edit():
    return render_template("form.html")


@app.route('/save-story', methods=['POST'])
def save():
    print("POST request recieved!")
    title = request.form['title']
    story = request.form['story']
    acceptance = request.form['criteria']
    business_value = request.form['business_value']
    print("Business value working")
    estimation = request.form['estimation']
    print("estimation working")
    status = request.form['status']
    return "Oh hi, hello. Looks like everything works. But for how long?"


if __name__ == "__main__":
    app.secret_key = "Welcome_to_the_league_of_Draven"
    app.run(
        debug=True,
        port=5000
    )
