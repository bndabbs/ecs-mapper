import csv
import sys
from ssl import create_default_context
import argparse
import six
from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser(description='User input parser')
parser.add_argument("--url", default="http://localhost:9200", type=str, help="Elasticsearch host")
parser.add_argument("--cacert", type=str, help="CA certificate for ES host")
parser.add_argument("--auth", help="ES auth information as either ':' separated string or a tuple")
parser.add_argument("--index", type=str, help="ES index or index pattern")
parser.add_argument("--csv", type=str, help="CSV file containing fields to convert")

args = parser.parse_args()


def es_connection() -> object:
    if args.cacert is not None:
        context = create_default_context(cafile=args.cacert)
    else:
        context = None

    es_auth = None
    if args.auth is not None:
        if isinstance(args.auth, (tuple, list)):
            es_auth = tuple(args.auth)
        elif isinstance(args.auth, six.string_types):
            es_auth = tuple(args.auth.split(":", 1))

    try:
        es = Elasticsearch(args.url, ssl_context=context, http_auth=es_auth)
        field_mapping = es.indices.get_field_mapping(fields="*", index=args.index, include_defaults="false")
        return list(field_mapping.values())[0]["mappings"].keys()
    except:
        sys.exit('Something went wrong connecting to Elasticsearch')


def import_csv(file):
    f = open(file, newline='')
    return csv.reader(f)


def match_fields(ecs):
    for row in ecs:
        for field in fields:
            if field in row[4]:
                print(field, row[0])


if args.index is not None:
    fields = es_connection()
elif args.csv is not None:
    fields = import_csv(args.csv)

schema = import_csv("./ecs_schema.csv")

match_fields(schema)
