#!/usr/bin/env python3
"""Provide some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


if __name__ == '__main__':
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count the number of documents in the collection
    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    # Count the number of documents with each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    # Count the number of documents with method=GET and path=/status
    num_status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{num_status} status check")

