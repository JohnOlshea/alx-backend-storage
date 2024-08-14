#!/usr/bin/env python3
"""
file: 11-schools_by_topic.py
"""


def schools_by_topic(mongo_collection, topic):
    """Python function that returns the list of school having a specific topic
    """

    schools = mongo_collection.find({"topics":topic})

    return list(schools)