from flask import Flask, request, render_template, make_response
import urllib
import getGraphScript
from models import AwardShows, Tweets
import datetime
import json

app = Flask(__name__)
requiredInfo=[]

@app.route('/')
def home():
    awardShows = AwardShows.objects
    return render_template('home.html', 
                           css_source='static/app.css',
                           AwardShows=awardShows
                          )
 
    
@app.route('/graph', methods=['POST'])
def graph():
    full_selection = request.form['award']
    show_selection = full_selection.split(':')[0]
    award_selection = full_selection.split(':')[1]

    award_selection_query = AwardShows.objects(name = show_selection).fields(awards=1).to_json()
    award_selection_query = json.loads(award_selection_query)
    
    award_selection_nominees = []
    for award in award_selection_query[0]["awards"]:
        if award['award_type'] == award_selection:
            award_selection_nominees.extend(award['nominees'])
    
    print('noms: ', award_selection_nominees)
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
