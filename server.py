from flask import Flask, render_template, redirect, request, session
import csv
app = Flask(__name__)


@app.route('/')
def route_index():
    with open("stories.csv", "r") as stories:
        reader = csv.reader(stories)
        data_list = list(reader)
    print(data_list)
    return render_template('list.html', data_list=data_list)

@app.route('/story')
def route_edit():
    return render_template("form.html")


if __name__ == "__main__":
    app.secret_key = "Welcome_to_the_league_of_Draven"
    app.run(
        debug=True,
        port=5000
    )
