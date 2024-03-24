import json
import traceback
import ndjson
from airflow import models
from google.oauth2.service_account import Credentials
from google.cloud import storage
from include.task_scripts.common_task_handler import *
from itertools import chain, starmap
from gcloud.aio.auth import Token
from gcloud.aio.storage import Storage
import asyncio
from io import StringIO


class GoogleStorageHandler:
    def __init__(self):
        self.sa_info = self.get_gdrive_creds()
        self.gcs_client = self.innit_google_storage_client(self.sa_info)
        self.aio_token = self.innit_google_token_(self.sa_info)

    def innit_google_storage_client(self,sa_info):
        creds = Credentials.from_service_account_info(sa_info)
        self.gcs_client = storage.Client(credentials = creds)
        return self.gcs_client
    
    def innit_google_token_(self,sa_info):
        self.scopes = ["https://www.googleapis.com/auth/devstorage.full_control"]
        key_string_io = StringIO(json.dumps(sa_info))
        self.aio_token = Token(service_file=key_string_io,scopes=self.scopes)
        return self.aio_token
    
    def get_gdrive_creds(self) -> Credentials:
        connection_object = models.Connection.get_connection_from_secrets("google_cloud_default")
        creds_str = connection_object.get_extra()
        creds_dict = json.loads(creds_str)
        service_account_info = json.loads(creds_dict['extra__google_cloud_platform__keyfile_dict'])
        return service_account_info

    def _handle_error():
        message = 'Error streaming file. Cause: %s' % (traceback.format_exc())
        print(message)
