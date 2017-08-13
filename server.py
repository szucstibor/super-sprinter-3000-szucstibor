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
    story = []
    print("POST request recieved!")
    story.append(request.form['title'])
    story.append(request.form['story'])
    story.append(request.form['criteria'])
    story.append(request.form['business_value'])
    story.append(request.form['estimation'])
    story.append(request.form['status'])
    with open('stories.csv', 'a') as stories:
        writer = csv.writer(stories)
        writer.writerow(story)

    return "Oh hi, hello. Looks like everything works. But for how long?"


if __name__ == "__main__":
    app.secret_key = "Welcome_to_the_league_of_Draven"
    app.run(
        debug=True,
        port=5000
    )
