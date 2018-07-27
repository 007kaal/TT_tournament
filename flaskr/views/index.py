from flask import current_app as app, render_template, session, url_for, redirect

@app.route("/")
def main():
  return render_template('index.html')


@app.route("/index.html")
def index():
    return redirect(url_for("main"))

