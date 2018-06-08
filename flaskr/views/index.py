from flask import current_app as app, render_template, session, url_for, redirect

@app.route("/")
def main():
  if 'username' in session:
    return redirect(url_for("/play")
  else :
    return render_template("index.html")


@app.route("/index")
def index():
  return redirect(url_for("/"))
