import requests
import yaml

with open(r'config.yml') as file:
    config = yaml.safe_load(file)
    head = {'Authorization': 'Bearer ' + config['access_token']}

    data = {
      "dataStreamName": "healthmate-to-google-fit",
      "type": "derived",
      "application": {
        "detailsUrl": "https://github.com/chris838/healthmate-to-google-fit",
        "name": "Healthmate to Google Fit",
        "version": "1"
      },
      "dataType": {
        "field": [
          {
            "name": "weight",
            "format": "floatPoint"
          }
        ],
        "name": "com.google.weight"
      }
    }

    url = 'https://www.googleapis.com/fitness/v1/users/me/dataSources'

    r = requests.post(url, json=data, headers=head)

    print(r.text)
    print(r.json())
