from flask import current_app as app, render_template, session, url_for, redirect
from .data import get_results

@app.route("/Admin123")
def results():
  return render_template("admin.html", type="results_schedule", page="Results ")

@app.route("/results/<category>")
def results_schedule(category):
  if category == 'WS':
     CatValue = "Women's Singles"
  elif category == 'MS':
     CatValue = "Men's Singles"
  elif category == 'MD':
     CatValue = "Men's Doubles"
  elif category == 'WD':
     CatValue = "Women's Doubles"
  elif category == 'XD':
     CatValue = "Mixed Doubles"
  else :
     return "Invalid Category", 404

  matches = get_results(category)
  return render_template("schedule.html", type="results_schedule", page = "Results  ", matches=matches, category = CatValue)
