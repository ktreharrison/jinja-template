# Project Title

## Table of Contents

- [About](#about)
- [Example Code](#ExampleCode)

## About <a name = "about"></a>

I used Jinja to make a small flask app. Jinja is a feature-rich templating engine packaged with the Flask web framework. But you can also use Jinja independently of Flask to create templates that you can programmatically fill with content.

With this project, I learned how to:

- Install the Jinja template engine
- Create your first Jinja template
- Render a Jinja template in Flask
- Use for loops and conditional statements with Jinja
- Nest Jinja templates
- Modify variables in Jinja with filters
- Use macros to add functionality to your front end

## Example Code

What things you need to install the software and how to install them.

```py
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
```
