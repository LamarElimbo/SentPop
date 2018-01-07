from flask import Flask, request, render_template, make_response
import urllib
import getGraphScript
import sys
sys.path.append("../")
import datetime

app = Flask(__name__)
requiredInfo=[]

@app.route('/')
def graphIt():
        
    negScores, negHeight = getGraphScript.getNegScript()
    posScores, posHeight = getGraphScript.getPosScript()
    x_keys = getGraphScript.getXCats()

    currentDate = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    return render_template('graph.html', 
                           css_source='static/app.css',
                           date=currentDate, 
                           neg_latestScores_ordered=negScores, 
                           neg_graphHeight=negHeight,
                           pos_latestScores_ordered=posScores, 
                           pos_graphHeight=posHeight,
                           x_cats=x_keys
                          )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    
