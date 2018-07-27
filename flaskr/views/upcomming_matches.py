from flask import current_app as app, render_template, session, url_for, redirect
from .data import get_upcomming_matches

@app.route("/upc")
def upcomming_matches():
  return render_template("schedule.html", type="upcomming_matches_schedule", page = "Upcomming Matches  ")

@app.route("/upc/<category>")
def upcomming_matches_schedule(category):
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

  matches = get_upcomming_matches(category)
  return render_template("schedule.html", type="upcomming_matches_schedule", page = "Upcomming Matches  ", matches=matches, category = CatValue)
