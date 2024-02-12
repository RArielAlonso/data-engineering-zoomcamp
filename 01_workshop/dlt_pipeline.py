import dlt
import requests
import json


def paginated_getter():
    BASE_API_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"
    page_number = 1

    while True:
        # Set the query parameters
        params = {'page': page_number}

        # Make the GET request to the API
        response = requests.get(BASE_API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        page_json = response.json()
        print(f'got page number {page_number} with {len(page_json)} records')

        # if the page has no records, stop iterating
        if page_json:
            yield page_json
            page_number += 1
        else:
            # No more data, break the loop
            break


url = "https://storage.googleapis.com/dtc_zoomcamp_api/yellow_tripdata_2009-06.jsonl"

def stream_download_jsonl(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    for line in response.iter_lines():
        if line:
            yield json.loads(line)

# time the download
import time
start = time.time()

# Use the generator to iterate over rows with minimal memory usage
row_counter = 0
for row in stream_download_jsonl(url):
    print(row)
    row_counter += 1
    if row_counter >= 5:
        break

# time the download
end = time.time()
print(end - start)

# define the connection to load to.
# We now use duckdb, but you can switch to Bigquery later
generators_pipeline = dlt.pipeline(destination='duckdb', dataset_name='generators')


# we can load any generator to a table at the pipeline destnation as follows:
info = generators_pipeline.run(paginated_getter(),
										table_name="http_download",
										write_disposition="replace")

# the outcome metadata is returned by the load and we can inspect it by printing it.
print(info)

# we can load the next generator to the same or to a different table.
info = generators_pipeline.run(stream_download_jsonl(url),
										table_name="stream_download",
										write_disposition="replace")

print(info)


# show outcome

import duckdb

conn = duckdb.connect(f"{generators_pipeline.pipeline_name}.duckdb")

# let's see the tables
conn.sql(f"SET search_path = '{generators_pipeline.dataset_name}'")
print('Loaded tables: ')
display(conn.sql("show tables"))

# and the data

print("\n\n\n http_download table below:")

rides = conn.sql("SELECT * FROM http_download").df()
display(rides)

print("\n\n\n stream_download table below:")

passengers = conn.sql("SELECT * FROM stream_download").df()
display(passengers)

# As you can see, the same data was loaded in both cases.