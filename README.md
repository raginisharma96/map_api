# Map Api

## Objective 
1. To parse the geojson data of a place(Here, Delhi) to structure format to ease the further calculation.
2. Build api which takes input as latitude + longitude,which depicts which place it falls within, and, given a location,
fetch all the nearby pin codes within a radius.

## Solution
A Geojson is a json file which defines shapes of locations - for example the shape of Delhi, Gurgaon, etc.
The geojson used here defines Delhi and its areas.

The solution code parses this json, and loads the boundaries latitude and longitude (geometry -> coordinates) into postgresql in a new table.The API "/detect" takes input as latitude + longitude, that depicts which place it falls within.
 
The testcase checks the functionality where all the nearby pin codes, within a radius of a given location, are fetched. For example, to fetch all points within 5km radius of (45.12, 71.12) .
 
To do this, mathematical computation of radius needs to be done. There are two ways to do this. So two different api have been created:
1.  /get_using_postgres - Using postgres "earthdistance" to compute all points in 5km radius.
2. /get_using_self - Implementing the mathematical computation.  

## Data Collection
The data source for this project has been referred through https://gist.github.com/ramsingla/6202001?short_path=7d9a995

## Tech Stack Used
Environment : Python3
1. Keras
2. Numpy
3. Tensorflow
4. Pandas
5. Nltk
6. String
