from flask import Flask, render_template, redirect, request, session
import csv
app = Flask(__name__)


@app.route('/')
def route_list():
    with open('stories.csv', 'r') as story:
        reader = csv.reader(story)
        stories = [row for row in reader]
    return render_template('list.html', stories=stories)


@app.route('/story')
def route_story():
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
        writer = csv.writer(stories, delimiter=',')
        writer.writerow(story)
    return "Oh hi, hello. Looks like everything works. But for how long?"


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
    return table


if __name__ == "__main__":
    app.secret_key = "Welcome_to_the_league_of_Draven"
    app.run(
        debug=True,
        port=5000
    )
