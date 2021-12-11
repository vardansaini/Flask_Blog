from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Bella',
        'title': 'Blog Post 1',
        'content': 'I am a bad Bitch',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Vardan Saini',
        'title': 'Blog Post 2',
        'content': 'I only came to this website to say this person not even near that LOL!!!',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)