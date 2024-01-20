# Data Engineer Zoomcamp

- download the csv file

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz 

- Command to run docker compose

 ``` docker compose up ```

- Command to create tables inside the container of the database or recreate the tables

```docker exec -it postgres-db bash /usr/local/bin/data_tables.sh```

- Command to get inside the container

```docker exec -it postgres-db psql -d database_nyc -U aalonso```

- command to build the image of python (get inside the folder first)

``` cd /ingesition ```

``` docker build -t ingestion . ```

- command to run python ingestion inside the container

First you must download the file with the comand ```wget``` inside the folder ``` /tmp/ ``` and after that make ```gunzip``` from the file to extract the csv from the ```.gz file ```

```docker run -it --rm --network nt-nyc -v /tmp:/tmp ingestion ``` 

