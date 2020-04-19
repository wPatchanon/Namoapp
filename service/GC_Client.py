import os
from google.cloud import datastore
from google.cloud import storage

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./etc/dbauthen.json'
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
#     os.path.dirname(os.path.realpath(__file__)), 'etc', 'dbauthen.json')

datastore_client = datastore.Client()
storage_client = storage.Client()

# Datastore kind/table name
kind = 'Prayer'

# storage bucket
bucket_name = "namo-chatbot"
bucket = storage_client.get_bucket(bucket_name)


def get_prayer_image_url(prayer_name):
    query = datastore_client.query(kind='Prayer')
    query.add_filter('name', '=', prayer_name)
    results = list(query.fetch())
    if len(results) == 0:
        return []

    image_urls = []
    if type(results[0]["image_object"]) == list:
        for image_object in results[0]["image_object"]:
            blob = bucket.get_blob("prayers/"+image_object)
            if blob is None:
                continue
            image_urls.append(blob.public_url)
    elif type(results[0]["image_object"]) == str:
        blob = bucket.get_blob("prayers/"+results[0]["image_object"])
        if blob is not None:
            image_urls.append(blob.public_url)
    return image_urls


def get_all_prayer():
    query = datastore_client.query(kind='Prayer')
    results = list(query.fetch())
    return results


def get_prayers_by_tag(tag):
    query = datastore_client.query(kind='Prayer')
    query.add_filter('tags', '=', tag)
    results = list(query.fetch())

    # prayers = []
    # for res in results:
    #     blob = bucket.get_blob("prayers/"+res["image_object"])
    #     prayers.append({"name": res["name"], "image_url": blob.public_url})
    return results

def get_teaching_image_url(id):
    key = datastore_client.key('Teaching', id)
    result = datastore_client.get(key)
    print(result["image_object"])

    if result is None:
        return []

    image_urls = []
    if type(result["image_object"]) == list:
        for image_object in result["image_object"]:
            blob = bucket.get_blob("teachings/"+image_object)
            if blob is None:
                continue
            image_urls.append(blob.public_url)
    elif type(result["image_object"]) == str:
        blob = bucket.get_blob("teachings/"+result["image_object"])
        if blob is not None:
            image_urls.append(blob.public_url)
    return image_urls

def get_all_teaching():
    query = datastore_client.query(kind='Teaching')
    results = list(query.fetch())
    return results


# print(get_prayers_by_tag("สุข"))
# print(get_prayer_image_url("ทดสอบ"))
# print(get_prayer_image_url("อิติปิโส"))
# print(get_all_prayer()[0]['name'])

print(get_teaching_image_url(5643280054222848))
print(get_all_teaching())