from flask import Flask, request, jsonify

from csv import writer
import csv

app = Flask(__name__)


@app.route("/")
def index():
  with open('./covid_data.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    places = []
    for row in data:
      if not first_line:
        places.append({
          "country": row[0],
          "totalConfirmed": row[1],
          "totalDeaths": row[2],
          "totalRecovered": row[3],
          "dailyConfirmed": row[4],
          "dailyDeaths": row[5],
          "activeCases": row[6],
          "totalCritical": row[7],
          "lastUpdated": row[8]
        })
      else:
        first_line = False
    return jsonify(places)



#start the server       
if __name__ == '__main__':
    app.run(debug=True)
