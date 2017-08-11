from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)


@app.route('/')
def story():
    return render_template("index.html")


@app.route('/save-note', methods=['POST'])
def route_save():
    print("POST request recieved!")
    session['note'] = request.form['note']
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = "Welcome_to_the_league_of_Draven"
    app.run(
        debug=True,
        port=5000
    )