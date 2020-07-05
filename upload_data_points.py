import requests, yaml, csv, datetime

chunk_size = 3

with open(r'config.yml') as config_file:
    config = yaml.safe_load(config_file)
    head = {'Authorization': 'Bearer ' + config['access_token']}

    # Load all data points from CSV
    datasets = []
    data = []
    with open('weight_sample.csv', newline='') as csv_file:
        weights = csv.reader(csv_file)
        next(weights, None)  # skip the headers
        for row in weights:
            time_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            time = int(time_obj.timestamp() * 1000000000)
            weight = float(row[1])
            data.append((time, weight))
            if len(data) >= chunk_size:
                datasets.append(data)
                data = []


    # Upload data
    for i, dataset in enumerate(datasets):

        start_time = min(dataset, key=lambda x: x[0])[0]
        end_time = max(dataset, key=lambda x: x[0])[0]
        print(f'Uploading dataset {i}: {start_time}-{end_time}')

        # Compile the data points
        points = []
        for (time, weight) in dataset:
            point = {
              "dataTypeName": "com.google.weight",
              "startTimeNanos": time
              ,
              "endTimeNanos": time,
              "value": [{
                "fpVal": weight
              }]
            }
            points.append(point)

        data = {
          "dataSourceId": config['data_source_id'],
          "maxEndTimeNs": end_time,
          "minStartTimeNs": start_time,
          "point": points
        }

        dataset_id = f'{start_time}-{end_time}'
        url = f'https://www.googleapis.com/fitness/v1/users/me/dataSources/{config["data_source_id"]}/datasets/{dataset_id}'

        print(url, data)

        r = requests.patch(url, json=data, headers=head)
        print(r.text)
        print(r.json())
