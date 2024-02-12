# First step, load the files to the bucket called terrademo-412014-data-lake-bucket
# I have created a folder inside called data

#Exercise 1
CREATE OR REPLACE EXTERNAL TABLE `terrademo_dataset.external_green_taxi_bq_excersive`
OPTIONS
(
  format = 'parquet',
  uris = ['gs://terrademo-412014-data-lake-bucket/data/green_tripdata_2022-*.parquet']
);


CREATE OR REPLACE TABLE `terrademo_dataset.green_taxi_bq_excersive` AS (
select * from `terrademo_dataset.external_green_taxi_bq_excersive`);

select count(*) from `terrademo_dataset.green_taxi_bq_excersive`;
# answer 1 -> 840402

#Exercise 2

select count(distinct PULocationID) from `terrademo_dataset.external_green_taxi_bq_excersive`;

select count(distinct PULocationID) from `terrademo_dataset.green_taxi_bq_excersive`;

#answer 2 -> 0 MB for the External Table and 6.41MB for the Materialized Table

#Exercise 3

select count(*) from `terrademo-412014.terrademo_dataset.green_taxi_bq_excersive`
where fare_amount=0;

#answer 3 -> 1622

#Exercise 4

CREATE OR REPLACE TABLE `terrademo-412014.terrademo_dataset.green_taxi_bq_excersive_partition_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS
select * from `terrademo_dataset.external_green_taxi_bq_excersive`;

#answer 4 -> Partition by lpep_pickup_datetime Cluster on PUlocationID

#Exercise 5

SELECT distinct PULocationID FROM `terrademo-412014.terrademo_dataset.green_taxi_bq_excersive_partition_clustered`
WHERE DATE(lpep_pickup_datetime)>= CAST('2022-06-01' AS DATE)
AND DATE(lpep_pickup_datetime)<= CAST('2022-06-30' AS DATE);

SELECT distinct PULocationID FROM `terrademo-412014.terrademo_dataset.green_taxi_bq_excersive`
WHERE DATE(lpep_pickup_datetime)>= CAST('2022-06-01' AS DATE)
AND DATE(lpep_pickup_datetime)<= CAST('2022-06-30' AS DATE);

#answer 5 -> 12.82 MB for non-partitioned table and 1.12 MB for the partitioned table

#Exercise 6

#answer 6 -> GCP Bucket

#Exercise 7

#answer 7 -> False

#Exercise 8

0 bytes -> it is stored in a temporal table

#BONUS: checking the size of the Partitions
select table_name,partition_id,total_rows
from `terrademo_dataset.INFORMATION_SCHEMA.PARTITIONS`
where table_name='green_taxi_bq_excersive_partition_clustered';
