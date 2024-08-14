#!/usr/bin/env python3
"""
file: 8-all.py
"""


def list_all(mongo_collection):
    """ Python function that lists all documents in a collection
        params: mongo_collection - the name of collection
        returns:
            an empty list if no document in the collection
    """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)

    return documents