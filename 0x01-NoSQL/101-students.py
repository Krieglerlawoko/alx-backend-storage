#!/usr/bin/env python3
"""
Return all students
sorted by average score.
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Return all students sorted by average score.
    Parameters:
    mongo_collection (Collection): The
    MongoDB collection containing student records.
    Returns:
    list: A list of students sorted by
    their average score in descending order.
    """
    return list(mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]))
