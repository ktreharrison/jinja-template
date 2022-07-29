from flask import Flask, render_template

from write_messages import max_score, students, test_name

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html", title="Jinja & Flask")

@app.route('/results')
def results():
    context = {
        'title': "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template('results.html', **context)


if __name__ == "__main__":
    app.run(debug=True, port=5100)