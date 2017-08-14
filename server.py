from flask import Flask, render_template, redirect, request, session, url_for
import csv
import random
app = Flask(__name__)
save_id = 0


@app.route("/list")
@app.route("/")
def route_list():
    stories = get_table_from_file("stories.csv")
    return render_template("list.html", stories=stories)


@app.route("/story")
def route_story():
    return render_template("form.html")


@app.route("/save-story", methods=["POST"])
def save():
    global save_id
    story_out = []
    story = []
    table = get_table_from_file("stories.csv")
    print("POST request recieved!")
    if save_id == 0:
        story.append(str(random.randint(1, 1000000000)))
    else:
        story.append(save_id)
        save_id = 0
    story.append(str(request.form["title"]))
    story.append(str(request.form["story"]))
    story.append(str(request.form["criteria"]))
    story.append(str(request.form["business_value"]))
    story.append(str(request.form["estimation"]))
    story.append(str(request.form["status"]))
    table.append(story)
    write_table_to_file("stories.csv", table)
    return redirect("/")


@app.route("/update/<id_of_story>", methods=["POST"])
def update_record(id_of_story):
    table = get_table_from_file("stories.csv")
    global save_id
    save_id = id_of_story
    for record in range(len(table)):
        if table[record][0] == id_of_story:
            table.remove(record)
            print("ID found")
            render_template("form.html")
    return route_list()


@app.route("/delete", methods=["POST"])
def delete():
    print(request.form)
    table = get_table_from_file("stories.csv")
    id_ = request.form
    id_of_story = list(id_.keys())
    print(id_of_story)
    for record in table:
        print(record)
        if str(record[0]) == id_of_story[0]:
            table.remove(record)
            print("ID found")
    write_table_to_file("stories.csv", table)
    return redirect("/")


def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def write_table_to_file(file_name, table):
    print(table)
    with open(file_name, "w") as file:
        for record in table:
            row = ";".join(str(r) for r in record)
            file.write(row + "\n")

if __name__ == "__main__":
    app.secret_key = "Welcome_to_the_league_of_Draven"
    app.run(
        debug=True,
        port=5000
    )
