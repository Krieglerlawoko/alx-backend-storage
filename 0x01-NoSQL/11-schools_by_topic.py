#!/usr/bin/env python3
"""11-schools_by_topic.py"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """Returns the list of
    schools having a specific topic"""
    return list(mongo_collection.find({ "topics": topic }))
