from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_response():
    data = {
        "status": "success",
        "message": "OK",
        "data": {
            "locations": [
                {
                    "id": 1,
                    "name": "Salalah",
                    "state": "Muhafazat Zufar",
                    "country": "Oman",
                    "country_code": "OM",
                    "locode": "OMSLL",
                    "lat": 17.01505,
                    "lng": 54.09237,
                },
                {
                    "id": 2,
                    "name": "Houston",
                    "state": "Texas",
                    "country": "United States",
                    "country_code": "US",
                    "locode": "USHOU",
                    "lat": 29.76328,
                    "lng": -95.36327,
                },
            ],
            "route": {
                "prepol": {
                    "location": 1,
                    "date": "2021-02-07 11:03:00",
                    "actual": True,
                },
                "pol": {"location": 1, "date": "2021-02-09 13:56:00", "actual": True},
                "pod": {"location": 2, "date": "2021-03-20 08:00:00", "actual": False},
                "postpod": {"location": 2, "date": None, "actual": None},
            },
            "vessels": [
                {
                    "id": 1,
                    "name": "MAERSK ATLANTA",
                    "imo": 9348649,
                    "call_sign": "WNTL",
                    "mmsi": 338078000,
                    "flag": "US",
                }
            ],
            "container": {
                "number": "TGBU6795701",
                "iso_code": "42G0",
                "events": [
                    {
                        "location": 1,
                        "description": "Gate out Empty",
                        "status": "CEP",
                        "date": "2021-02-07 11:03:00",
                        "actual": True,
                        "type": "land",
                        "vessel": None,
                        "voyage": None,
                    },
                    {
                        "location": 1,
                        "description": "Gate in",
                        "status": "CGI",
                        "date": "2021-02-09 13:56:00",
                        "actual": True,
                        "type": "land",
                        "vessel": None,
                        "voyage": None,
                    },
                    {
                        "location": 1,
                        "description": "Load",
                        "status": "CLL",
                        "date": "2021-02-18 07:33:00",
                        "actual": True,
                        "type": "sea",
                        "vessel": 1,
                        "voyage": "105W",
                    },
                    {
                        "location": 2,
                        "description": "Discharge",
                        "status": "CDD",
                        "date": "2021-03-20 08:00:00",
                        "actual": False,
                        "type": "sea",
                        "vessel": 1,
                        "voyage": "105W",
                    },
                    {
                        "location": 2,
                        "description": "Gate out",
                        "status": "CGO",
                        "date": "2021-03-20 08:00:05",
                        "actual": False,
                        "type": "land",
                        "vessel": None,
                        "voyage": None,
                    },
                ],
            },
        },
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

