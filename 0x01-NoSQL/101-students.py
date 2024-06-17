#!/usr/bin/env python3
"""14-top_students.py"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    return list(mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]))
