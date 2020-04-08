import os
from google.cloud import datastore
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'etc/dbauthen.json'

datastore_client = datastore.Client()
storage_client = storage.Client()

# Datastore kind/table name
kind = 'Prayer'

# storage bucket
bucket_name = "namo-chatbot"
bucket = storage_client.get_bucket(bucket_name)

# Get image URL of prayer
# prayer_name must be exact match
# return None if not found


def get_prayer_image_url(prayer_name):
    query = datastore_client.query(kind='Prayer')
    query.add_filter('name', '=', prayer_name)
    results = list(query.fetch())

    if len(results) == 0:
        return None
    blob = bucket.get_blob(results[0]["image_object"])
    if blob is None:
        return None
    return blob.public_url

def get_all_prayer():
    query = datastore_client.query(kind='Prayer')
    results = list(query.fetch())
    return results

# print(get_prayer_image_url('มหาเศรษฐี'))
# print(get_all_prayer()[0]['name'])