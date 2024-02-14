# de-challenge-sfdataset

Create a Python program to read data from [SF Fire Incidents](https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric/about_data) Dataset

### How it's done:

1. Ingestion

All data ingestions were built using [Mage-AI](https://www.mage.ai/), an open source data pipeline and schedule builder

2. Storage

All data were stored using postgres on a docker container

3. Data Visualization

Datavis were built using Metabase, a open source data analisys tool that can execute queries and create dashboards

### How to run:

It's all built using [docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/)

To get all containers running, simple run

```sh
docker compose up
```

WIth all containers running, access them using your best browser:

- [Mage-AI UI](http://localhost:6789/overview)
    - To trigger the pipeline run, navigate to Pipelines -> bronze_etl_sf_fi -> Triggers -> daily_bronze_etl_sf_fi -> Enable Trigger. After that the pipeline will start.

- [Metabase UI](http://localhost:3000/)
    - Create a new user and connect to the postgre instance using the following credentials
        - POSTGRES DBNAME: datawarehouse
        - POSTGRES USER: dechallenge
        - POSTGRES PASSWORD: dechallenge
        - POSTGRES HOST: datawarehouse
        - POSTGRES PORT: 5432