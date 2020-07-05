# Import data from Withing's Healthmate to Google Fit.

Use the playground (https://developers.google.com/oauthplayground/) to obtain a temporary access token with permissions for reading and writing to the Fitness API.

Add access token to `config.yml` file under `access_token`.

Run `create_data_source.py`

Go back to the playground and run the request for listing all datasources. You should be able to find the `dataSourceId` for your newly created data source, it will look something like `derived:com.google.weight:1234567890:healthmate-to-google-fit`. Add this to `config.yml` under `data_source_id`.

Go to the Withing's online web dashboard and export Withing's Healthmate data to CSV. Once this is done, find the `weight.csv` file and copy into this folder.

Make sure there is some time left on your access token (or refresh if not) and run `upload_data_points.py`. You may adjust the chunk size to speed up the process, although it does seem to work even if uploading everything in a single chunk.

You may need to uninstall/reinstall Google Fit to see the uploaded data immediately.
