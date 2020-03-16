import csv
import json

from requests import *


def process_data():
    with open('temp', newline='') as fin:
        dat = csv.reader(fin, delimiter=',')
        x = 0
        obj = {}
        for row in dat:
            try:
                if int(row[-1]) < 20:
                    continue
            except ValueError as e:
                print(e)
            if row[0] != '':
                name = row[0] + ' ' + row[1]
            else:
                name = row[1]
            lat = row[2]
            long = row[3]
            infected = row[4:]
            obj[name] = {}
            obj[name]["lat"] = lat
            obj[name]["long"] = long
            obj[name]["data"] = infected
        with open("static/data.json", "w") as fp:
            json.dump(obj, fp)


def get_data():
    d = get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"
            "master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv").content
    open("temp", "w").write(d.decode("utf-8"))


get_data()
process_data()
