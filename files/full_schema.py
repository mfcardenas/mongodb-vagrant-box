#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import check_output, CalledProcessError
from json import loads

MONGO = "mongo"
SCHEMA_TOOL = "/srv/files/variety.js"


def show_schema(database):
    schema_cmd = [MONGO, database, "--quiet", "--eval",
                  "var collection = '%(collection)s'", SCHEMA_TOOL]

    # load collections
    ret = check_output(
        [MONGO, database, "--quiet", "--eval", "db.getCollectionNames()"])
    collections = ret.strip("\n").split(",")

    # get schemas
    for collection in collections:
        if collection.startswith("system."):
            continue

        try:
            print collection
            ret = check_output([part % {"collection": collection}
                               for part in schema_cmd])
            columns = [loads(col) for col in ret.split("\n") if col]
            for col in columns:
                print col["_id"]["key"] + ": " + ", ".join(col["value"]["types"]), "*" if col["percentContaining"] < 100 else ""

        except CalledProcessError as e:
            print "No info"

        print

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("Show MongoDB database schema")
    parser.add_argument(
        "database", help="Name of database to analyze.", default="test")
    args = parser.parse_args()

    show_schema(args.database)
