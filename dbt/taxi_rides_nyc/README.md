Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [dbt community](https://getdbt.com/community) to learn from other analytics engineers
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


1- Load parquet files to GCP Cloud Storage with extra_load_gcp_storage
2- Create external tables in big query by this commands
Create or replace external table `terrademo-412014.terrademo_dataset.green_tripdata`
OPTIONS
(
  format = 'parquet',
  uris = ['gs://terrademo-412014-data-lake-bucket/green/*.parquet']
);


Create or replace external table `terrademo-412014.terrademo_dataset.yellow_tripdata`
OPTIONS
(
  format = 'parquet',
  uris = ['gs://terrademo-412014-data-lake-bucket/yellow/*.parquet']
);

CREATE OR REPLACE TABLE `terrademo_dataset.green_tripdata` AS (
select * from `terrademo_dataset.external_green_tripdata`);

CREATE OR REPLACE TABLE `terrademo_dataset.yellow_tripdata` AS (
select * from `terrademo_dataset.external_yellow_tripdata`);
