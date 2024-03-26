# import json
# import traceback
# from io import StringIO
#
# import ndjson
# import requests
# from airflow import models
# from gcloud import storage
# from gcloud.aio.auth import Token
# # from google.cloud import storage
# from google.oauth2.service_account import Credentials
# from include.task_scripts.common_task_handler import *
#
#
# class GoogleStorageHandler:
#     def __init__(self):
#         self.sa_info = self.get_gdrive_creds()
#         self.gcs_client = self.innit_google_storage_client(self.sa_info)
#         self.aio_token = self.innit_google_token_(self.sa_info)
#
#     def innit_google_storage_client(self, sa_info):
#         creds = Credentials.from_service_account_info(sa_info)
#         self.gcs_client = storage.Client(credentials=creds)
#         return self.gcs_client
#
#     def innit_google_token_(self, sa_info):
#         self.scopes = ["https://www.googleapis.com/auth/devstorage.full_control"]
#         key_string_io = StringIO(json.dumps(sa_info))
#         self.aio_token = Token(service_file=key_string_io, scopes=self.scopes)
#         return self.aio_token
#
#     def get_gdrive_creds(self) -> Credentials:
#         connection_object = models.Connection.get_connection_from_secrets("google_cloud_default")
#         creds_str = connection_object.get_extra()
#         creds_dict = json.loads(creds_str)
#         service_account_info = json.loads(creds_dict['extra__google_cloud_platform__keyfile_dict'])
#         return service_account_info
#
#     def _handle_error(self):
#         message = 'Error streaming file. Cause: %s' % (traceback.format_exc())
#         print(message)
#
#     def pull_data_from_api_to_gcs(api_url, bucket_name, gcs_path):
#         # Call the API
#         headers = {
#             'Authorization': f'Bearer {token}'
#         }
#         response = requests.get(api_url, headers=headers)
#         data = response.json()
#         # stringio_data = data
#         ## instane of the storage client
#         storage_client = storage.Client()
#
#         ## create the gcs_bucket if not exist
#         # bucket = storage_client.bucket(gcs_bucket_name)
#         # storage_client.create_bucket(gcs_bucket_name,exists_ok=True)
#
#         ## instance of a bucket in your google cloud storage
#         bucket = storage_client.get_bucket(bucket_name)
#
#         ## create new file name
#         blob = bucket.blob(f"{gcs_path}/data.json")
#
#         blob.upload_from_string(ndjson.dumps(data))
#         print(f"Pull data from api of {gcs_path} successfully")


# flake8: noqa
