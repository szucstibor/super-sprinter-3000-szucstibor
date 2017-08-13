from flask import Flask, render_template, redirect, request, session
import csv
import random
app = Flask(__name__)


@app.route("/list")
@app.route("/")
def route_list():
    with open("stories.csv", "r") as story:
        reader = csv.reader(story)
        stories = [row for row in reader]
    return render_template("list.html", stories=stories)


@app.route("/story")
def route_story():
    return render_template("form.html")


@app.route("/save-story", methods=["POST"])
def save():
    story = []
    table = get_table_from_file("stories.csv")
    print("POST request recieved!")
    story.append(random.randint(1, 1000000000))
    story.append(request.form["title"])
    story.append(request.form["story"])
    story.append(request.form["criteria"])
    story.append(request.form["business_value"])
    story.append(request.form["estimation"])
    story.append(request.form["status"])
    with open("stories.csv", "a") as stories:
        writer = csv.writer(stories, delimiter=",")
        writer.writerow(story)
    return redirect("/")


@app.route("/update/<id_of_story>", methods=["POST", "GET"])
def update(id_of_story):
    table = get_table_from_file("stories.csv")
    save_id = id_of_story
    for record in range(len(table)):
        if table[record][0] == id_of_story:
            table.pop(record)
            print("ID found")
    return redirect("/")


@app.route("/delete/<id_of_story>", methods=["POST"])
def delete(id_of_story):
    table = get_table_from_file("stories.csv")
    for record in range(len(table)):
        if table[record][0] == id_of_story:
            table.pop(record)
            print("ID found")
    write_table_to_file("stories.csv", table)
    return redirect("/")


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
    return table


def write_table_to_file(file_name, table):
    with open(file_name, "wr") as file:
        for record in table:
            row = ";".join(record)
            file.write(row + "\n")

if __name__ == "__main__":
    app.secret_key = "Welcome_to_the_league_of_Draven"
    app.run(
        debug=True,
        port=5000
    )
