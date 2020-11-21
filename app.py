from flask import Flask, request, jsonify
from flask_cors import CORS

from csv import writer
import csv

app = Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])
def index():
  with open('./covid_data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    places = []
    for row in data:
      if not first_line:
        places.append({
          "country": row[0],
          "countryCode": row[1],
          "totalConfirmed": row[2],
          "totalDeaths": row[3],
          "totalRecovered": row[4],
          "dailyConfirmed": row[5],
          "dailyDeaths": row[6],
          "activeCases": row[7],
          "totalCritical": row[8],
          "lastUpdated": row[9]
        })
      else:
        first_line = False
    return jsonify(places)
    


@app.route("/specific/<country>",methods=["GET"])
def get_by_country(country):
  with open('./covid_data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    places = []
    for row in data:
      if not first_line and row[1] == country:
        places.append({
          "country": row[0],
          "countryCode": row[1],
          "totalConfirmed": row[2],
          "totalDeaths": row[3],
          "totalRecovered": row[4],
          "dailyConfirmed": row[5],
          "dailyDeaths": row[6],
          "activeCases": row[7],
          "totalCritical": row[8],
          "lastUpdated": row[9]
        })
      else:
        first_line = False
    return jsonify(places)

@app.route("/countrycodes", methods=["GET"])
def get_country_codes():
   with open('./covid_data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    places = []
    country_codes = []
    for row in data:
      if not first_line:
        places.append(row[1])
      else:
        first_line = False
        
    country_codes.append({"country_codes": places})
    return jsonify(country_codes)


@app.route("/countries",methods=["GET"])
def index():
  with open('./covid_data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    places = []
    for row in data:
      if not first_line:
        places.append({
          "country": row[0],
          "countryCode": row[1]
        })
      else:
        first_line = False
    return jsonify(places)
    

#start the server       
if __name__ == '__main__':
    app.run(debug=True)
