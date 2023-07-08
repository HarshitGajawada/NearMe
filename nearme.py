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
    with open('hospitals.json','r') as hospitals:
        t = json.load(hospitals)
    return render_template('hospitals.html',t_dict=t)

@nearme.route('/eateries')
def eateries():
    with open('eateries.json','r') as eateries:
        t = json.load(eateries)
    return render_template('eateries.html',t_dict=t)

@nearme.route('/petrol')
def petrol():
    with open('petrolstations.json','r') as petrol:
        t = json.load(petrol)
    return render_template('petrol.html',t_dict=t)

@nearme.route('/banks')
def banks():
    with open('banks.json','r') as banks:
        t = json.load(banks)
    return render_template('banks.html',t_dict=t)

if __name__ == "__main__":
    nearme.run(debug=True)






        
        
    
    

    
