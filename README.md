# Data Engineer Zoomcamp

- download the csv file

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz 

- Command to run docker compose

docker compose up

- Command to get inside the container

docker exec -it postgres-db psql -d database_nyc -U aalonso

- command to build the image of python

cd /ingesition
docker build -t ingestion . 

- command to run python ingestion inside the container
docker run -it --rm --network nt-nyc -v /tmp:/tmp ingestion

- command to run pgadmin
docker run -it -p 8080:80 -e 'PGADMIN_DEFAULT_EMAIL=admin@admin.com' -e 'PGADMIN_DEFAULT_PASSWORD=root' --network nt-nyc -d dpage/pgadmin4