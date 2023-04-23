from flask import Flask, request, render_template 
import requests , re
from config import Config 
from .site.routes import site
 


app=Flask(__name__)


app.config.from_object(Config)

api_key = app.config['API_KEY']

app.register_blueprint(site)



@app.route('/directions')
def get_directions():
    starting_point = request.args.get('start')
    destination = request.args.get('destination')
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={starting_point}&destinations={destination}&key={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
     # Extract the distance in kilometers from the JSON data, convert it to an integer, and store it
    distance_km = data['rows'][0]['elements'][0]['distance']['text']
    distance_km= int(re.sub('[^0-9]','', distance_km))
    # Convert the distance from kilometers to miles, round it to the nearest whole number, and convert it to a string
    distance_miles = str(round(distance_km * 0.621371))
    # Extract the duration of the trip from the JSON data and store it
    duration = data['rows'][0]['elements'][0]['duration']['text']
    
    # Render the results.html template with the distance and duration variables passed as arguments
    return render_template('results.html', distance=distance_miles, duration=duration)