# import os
# import json
# from pymongo import MongoClient
# from datetime import datetime
# import gzip
# from itertools import chain, starmap
# from pathlib import Path
#
# class MongodbProcessing():
#     @staticmethod
#     def flatten_json2(y):
#         out = {}
#
#         def flatten(x, name=''):
#
#             # If the Nested key-value
#             # pair is of dict type
#             if type(x) is dict:
#
#                 for a in x:
#                     flatten(x[a], name + a + '_')
#
#             # If the Nested key-value
#             # pair is of list type
#             elif type(x) is list:
#
#                 i = 0
#
#                 for a in x:
#                     flatten(a, name + str(i) + '_')
#                     i += 1
#             else:
#                 out[name[:-1]] = x
#
#         flatten(y)
#         return out
#
#     @staticmethod
#     def parse_and_insert(filename,collection):
#         collection = collection
#         with gzip.open(filename, 'r') as file:
#             for line in file:
#                 try:
#                     data = json.loads(line)
#                     auction_id = data.get('auctionId', 'NA')
#                     campaign_id = data.get('biddingMainAccount', 'NA')
#                     creative_id = data.get('bidResponseCreativeName', 'NA')
#                     adgroup_id = data.get('biddingSubAccount', 'NA')
#                     unpack_bidRequestString = flatten_json2(json.loads((data.get('bidRequestString'))))
#
#                     user_agent = unpack_bidRequestString.get('userAgent', 'Others')
#                     #.get('userAgent', 'Others')
#                     site = unpack_bidRequestString.get('url', 'Others')
#                     geo = unpack_bidRequestString.get('device_geo_country', unpack_bidRequestString.get('device_ext_geo_criteria_id', 'Others'))
#                     exchange = unpack_bidRequestString.get('exchange', 'Others')
#                     price_str = data.get('winPrice', '0')
#                     price = float(price_str.split('USD')[0].strip()) * 1000000 if 'USD' in price_str else float(price_str)
#                     timestamp_val = unpack_bidRequestString.get('timestamp', 'Others')
#                     datetime_ = datetime.strptime(timestamp_val, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()
#                     timestamp_ = datetime.utcfromtimestamp(datetime_).replace(minute=0, second=0, microsecond=0).timestamp()
#
#                     # Insert into MongoDB
#                     collection.insert_one({
#                         'auctionId': auction_id,
#                         'campaignId': campaign_id,
#                         'creativeId': creative_id,
#                         'adgroupId': adgroup_id,
#                         'userAgent': user_agent,
#                         'site': site,
#                         'geo': geo,
#                         'exchange': exchange,
#                         'price': price,
#                         'time': int(timestamp_)
#                     })
#                 except Exception as e:
#                     print("Error processing line:", e)
#
#     @staticmethod
#     def aggregated_data_inv_win(from_collection):
#         from_collection_ = from_collection
#
#         pipeline = [
#             {
#                 '$group': {
#                     '_id': {
#                         'campaignId': '$campaignId',
#                         'creativeId': '$creativeId',
#                         'adgroupId': '$adgroupId',
#                         'geo': '$geo',
#                         'time': '$time'
#                     },
#                     'totalPrice': {'$sum': '$price'},
#                     'minPrice': {'$min': '$price'},
#                     'maxPrice': {'$max': '$price'},
#                     'totalCount': {'$sum': 1}
#                 }
#             },
#             {
#                 '$project': {
#                     '_id': 0,
#                     'campaignId': '$_id.campaignId',
#                     'creativeId': '$_id.creativeId',
#                     'adgroupId': '$_id.adgroupId',
#                     'geo': '$_id.geo',
#                     'time': '$_id.time',
#                     'totalPrice': 1,
#                     'minPrice': 1,
#                     'maxPrice': 1,
#                     'totalCount': 1
#                 }
#             }
#         ]
#
#         # Aggregate data
#         aggregated_data = list(from_collection_.aggregate(pipeline))
#         return aggregated_data
#
#     def upsert_task(aggregation_result_set,target_collection):
#         for entry in aggregation_result_set:
#             filter_query = {
#                 'campaignId': entry['campaignId'],
#                 'creativeId': entry['creativeId'],
#                 'adgroupId': entry['adgroupId'],
#                 'geo': entry['geo'],
#                 'time': entry['time']
#             }
#             update_query = {'$set': entry}
#             target_collection.update_one(filter_query, update_query, upsert=True)
#
#     def insert_data_to_collection():
#         client = MongoClient('localhost', 27017)
#         db = client['db_name']
#         insert_collection = db['collection_name']
#         # Insert into MongoDB
#         insert_collection.insert_one({
#                         'auctionId': auction_id,
#                         'campaignId': campaign_id,
#                         'creativeId': creative_id,
#                         'adgroupId': adgroup_id,
#                         'userAgent': user_agent,
#                         'site': site,
#                         'geo': geo,
#                         'exchange': exchange,
#                         'price': price,
#                         'time': int(timestamp_)
#                     })


# flake8: noqa

