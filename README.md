# ECS Mapper

This is a proof of concept project for mapping existing datasets to [ECS](https://github.com/elastic/ecs) compliant field names.

This extends the existing ECS CSV to include a **Sources** column, which is a list of common sources names for a given ECS field.


## Usage

```
usage: ecs-mapper.py [-h] [--url URL] [--cacert CACERT] [--auth AUTH]
                     [--index INDEX] [--csv CSV]

User input parser

optional arguments:
  -h, --help       show this help message and exit
  --url URL        Elasticsearch host
  --cacert CACERT  CA certificate for ES host
  --auth AUTH      ES auth information as either ':' separated string or a
                   tuple
  --index INDEX    ES index or index pattern
  --csv CSV        CSV file containing fields to convert
  ```
  
Check against existing index:

```
python ecs-mapper.py --url https://localhost:9200 --auth 'elastic:changeme' --cacert ./ca.pem --index "bro-network-2019.11.18"
```
