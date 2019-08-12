from flask import Flask,request,render_template
import pickle as pkl
from math import radians, cos, sin, asin, sqrt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from geopy.geocoders import Nominatim
import json
geolocator = Nominatim()




app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('input.html')

@app.route("/detect",methods=["GET"])
def hello():
    lat = float(request.args["lat"])
    long = float(request.args["long"])
    flag = 'null'
    with open("data.pkl","rb") as f:
        df = pkl.load(f)
    for place in df.columns:
        polygon = Polygon(df[place].values[0]) # create polygon
        point = Point(long,lat) # create point
        print(point.within(polygon))
        if(point.within(polygon)):
            flag = place
    if flag != 'null':
        return flag
    else:
        return 'No place found'



#calculating the distance between two Point
def distance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


@app.route("/get_using_self")
def postcode():
    long, lat = [float(request.args.get('long')), float(request.args.get('lat'))]
    with open("data.pkl","rb") as f:
            df = pkl.load(f)
    details = {}
    for city_belong in df.columns:
        test_point = df[city_belong][0]
    #     print(city_belong,test_point)


        for i in test_point:
            distance_in_km = distance(long,lat,i[0],i[1])
    #         print('Distance (km):',a)
            if distance_in_km <= 5:
                location  = geolocator.reverse([i[1],i[0]])
                if location != None:
                    details[location.raw['address']['postcode']] = location.raw['display_name']
                    print(location.raw['address']['postcode'])
                    print(location.raw['display_name'])
                    
    return json.dumps(details)
            

if __name__ == '__main__':
    app.run(debug=True)
