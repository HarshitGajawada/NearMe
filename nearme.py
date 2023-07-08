from flask import Flask, render_template
import json

json_files = ['theatres.json','hospitals.json','eateries.json','petrolstations.json','banks.json']

nearme = Flask(__name__)

@nearme.route('/')
def home_html():
    return render_template('home.html')


@nearme.route('/theatres')
def theatres():
    with open('theatres.json','r') as theatres:
        t = json.load(theatres)
    return render_template('theatres.html',t_dict=t)

@nearme.route('/hospitals')
def hospitals():
    pass

if __name__ == "__main__":
    nearme.run(debug=True)






        
        
    
    

    
