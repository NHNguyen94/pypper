# import io
# import json
# import traceback
# from pathlib import Path
#
# import pandas
# from airflow import models
# from google.api_core import retry
# from google.cloud import bigquery
# from google.oauth2.service_account import Credentials
# from include.task_scripts.common_task_handler import *
# from six import StringIO
#
# root_path = str(Path(__file__).resolve().parents[2])
#
#
# class BigQueryError(Exception):
#     '''Exception raised whenever a BigQuery error happened'''
#
#     def __init__(self, errors):
#         super().__init__(self._format(errors))
#         self.errors = errors
#
#     def _format(self, errors):
#         err = []
#         for error in errors:
#             err.extend(error['errors'])
#         return json.dumps(err)
#
#
# class BigqueryHandler:
#     def __init__(self):
#         self.bq_client = self.innit_bigquery_connection()
#
#     def innit_bigquery_connection(self):
#         creds = self.get_gdrive_creds()
#         self.bq_client = bigquery.Client(credentials=creds)
#         return self.bq_client
#
#     def get_gdrive_creds(self) -> Credentials:
#         connection_object = models.Connection.get_connection_from_secrets("google_cloud_default")
#         creds_str = connection_object.get_extra()
#         creds_dict = json.loads(creds_str)
#         service_account_info = json.loads(creds_dict['extra__google_cloud_platform__keyfile_dict'])
#         return Credentials.from_service_account_info(service_account_info)
#
#     def _handle_error(self):
#         message = 'Error streaming file. Cause: %s' % (traceback.format_exc())
#         print(message)
#
#     def execute_bigquery_job(self, sql_statement, data_return_type=None):
#         print(f"Run the sql statement on BQ: {sql_statement}")
#         query_job = self.bq_client.query(sql_statement)
#         print(query_job)
#         if not data_return_type:
#             for row in query_job.result():
#                 print(row)
#                 return 'Execute Success'
#         elif data_return_type == 'list':
#             return_list = []
#             for row in query_job:
#                 return_list.append(dict(row.items()))
#             return return_list
#         elif data_return_type == 'df':
#             return query_job.to_dataframe()
#         else:
#             return 'Failed job'
#
#     def _insert_rows_into_bigquery(self, bucket_name, file_name):
#         blob = self.bq_client.get_bucket(bucket_name).blob(file_name)
#
#         row = json.loads(blob.download_as_string())
#         print('row: ', row)
#         table_id = self.bq_client.dataset('').table('')
#         errors = self.bq_client.insert_rows_json(table_id,
#                                                  json_rows=[row],
#                                                  row_ids=[file_name],
#                                                  retry=retry.Retry(deadline=30))
#
#         print(errors)
#         if errors != []:
#             raise BigQueryError(errors)
#
#     def _load_table_from_uri(self, uri_path, file_name, dataset, tableSchema, tableName, source_format, load_type,
#                              max_bad_records_=0):
#         # ! source file must be like this:
#         """
#         {"id": "1", "first_name": "John", "last_name": "Doe", "dob": "1968-01-22", "addresses": [{"status": "current", "address": "123 First Avenue", "city": "Seattle", "state": "WA", "zip": "11111", "numberOfYears": "1"}, {"status": "previous", "address": "456 Main Street", "city": "Portland", "state": "OR", "zip": "22222", "numberOfYears": "5"}]}
#         {"id": "2", "first_name": "John", "last_name": "Doe", "dob": "1968-01-22", "addresses": [{"status": "current", "address": "123 First Avenue", "city": "Seattle", "state": "WA", "zip": "11111", "numberOfYears": "1"}, {"status": "previous", "address": "456 Main Street", "city": "Portland", "state": "OR", "zip": "22222", "numberOfYears": "5"}]}
#         """
#         # ! source file must be the same.
#         # ! if source file is not a NEWLINE_DELIMITED_JSON then you need to load it with blob, convert to JSON and then load as file.
#         client = self.bq_client
#         job_config = bigquery.LoadJobConfig()
#
#         uri = f'gs://{uri_path}/{file_name}'
#         table_id = client.dataset(dataset).table(tableName)
#
#         if source_format == 'CSV':
#             job_config.field_delimiter = '\t'
#             job_config.quote_character = None
#
#         if tableSchema is not None:
#             schema = create_schema_from_yaml(tableSchema)
#             print(schema)
#             job_config.schema = schema
#         else:
#             job_config.autodetect = True
#
#         job_config.source_format = source_format
#         job_config.write_disposition = load_type
#         job_config.max_bad_records = max_bad_records_
#
#         load_job = client.load_table_from_uri(
#             uri,
#             table_id,
#             job_config=job_config,
#         )
#
#         load_job.result()
#         print(f"Ingestion to BQ table: {table_id} finished.")
#
#     def _load_table_from_object_string(self, bucket_name, file_name, dataset, tableSchema, tableName):
#         client = self.bq_client
#         # ! we will convert body to a new line delimited JSON
#         blob = client.get_bucket(bucket_name).blob(file_name)
#         blob = blob.download_as_string().decode()
#         # Transform object string data into JSON outer array string:
#         blob = json.dumps('[' + blob.replace('}{', '},{') + ']')
#         # Load as JSON:
#         body = json.loads(blob)
#         # Create an array of string elements from JSON:
#         jsonReady = [json.dumps(record) for record in json.loads(body)]
#         # Now join them to create new line delimited JSON:
#         data_str = u"\n".join(jsonReady)
#         print('data_file :', data_str)
#         # Create file to load into BigQuery:
#         data_file = StringIO(data_str)
#         job_config = bigquery.LoadJobConfig()
#         table_id = client.dataset(dataset).table(tableName)
#
#         schema = create_schema_from_yaml(tableSchema)
#         job_config.schema = schema
#
#         job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
#         job_config.write_disposition = 'WRITE_APPEND',
#
#         load_job = client.load_table_from_file(
#             data_file,
#             table_id,
#             job_config=job_config,
#         )
#
#         load_job.result()  # Waits for table load to complete.
#         print("Job finished.")
#
#         def _load_table_from_json(self, bucket_name, file_name, dataset, tableSchema, tableName):
#             client = self.bq_client
#             blob = client.get_bucket(bucket_name).blob(file_name)
#             # ! source data file format must be outer array JSON:
#
#             body = json.loads(blob.download_as_string())
#             table_id = client.dataset(dataset).table(tableName)
#
#             job_config = bigquery.LoadJobConfig()
#             job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
#             job_config.write_disposition = 'WRITE_APPEND'
#
#             schema = create_schema_from_yaml(tableSchema)
#             job_config.schema = schema
#
#             load_job = client.load_table_from_json(
#                 body,
#                 table_id,
#                 job_config=job_config,
#             )
#
#             load_job.result()  # Waits for table load to complete.
#             print("Job finished.")
#
#     def _load_table_from_dataframe(self, bucket_name, file_name, dataset, tableSchema, tableName):
#         """
#         Source data file must be outer JSON
#         """
#         client = self.bq_client
#         blob = client.get_bucket(bucket_name).blob(file_name)
#         body = json.loads(blob.download_as_string())
#         table_id = client.dataset(dataset).table(tableName)
#
#         schema = create_schema_from_yaml(tableSchema)
#         job_config = bigquery.LoadJobConfig()
#         job_config.schema = schema
#
#         df = pandas.DataFrame(
#             body,
#             # In the loaded table, the column order reflects the order of the
#             # columns in the DataFrame.
#             columns=["id", "first_name", "last_name", "dob", "addresses"],
#
#         )
#         df['addresses'] = df.addresses.astype(str)
#         df = df[
#             [
#                 'id',
#                 'first_name',
#                 'last_name',
#                 'dob',
#                 'addresses'
#             ]
#         ]
#
#         load_job = client.load_table_from_dataframe(
#             df,
#             table_id,
#             job_config=job_config,
#         )
#
#         load_job.result()
#         print("Job finished.")
#
#     def _load_table_as_src(self, bucket_name, file_name, dataset, tableSchema, tableName):
#         client = self.bq_client
#         # ! source file must be outer array JSON
#         # ! this will work for CSV where a row is A JSON string --> SRC column (Snowflake like)
#         blob = client.get_bucket(bucket_name).blob(file_name)
#         body = json.loads(blob.download_as_string())
#         table_id = client.dataset(dataset).table(tableName)
#         job_config = bigquery.LoadJobConfig()
#         schema = create_schema_from_yaml(tableSchema)
#         job_config.schema = schema
#
#         job_config.source_format = bigquery.SourceFormat.CSV,
#         # something that doesn't exist in your data file:
#         job_config.field_delimiter = ";"
#         # Notice that ';' worked because the snippet data does not contain ';'
#
#         job_config.write_disposition = 'WRITE_APPEND',
#
#         data_str = u"\n".join(json.dumps(item) for item in body)
#         print('data_str :', data_str)
#         data_file = io.BytesIO(data_str.encode())
#         print('data_file :', data_file)
#         load_job = client.load_table_from_file(
#             data_file,
#             table_id,
#             job_config=job_config,
#         )
#
#         load_job.result()
#         print("Job finished.")
#
#     def _load_table_as_df_normalized(self, bucket_name, file_name, dataset, tableSchema, tableName):
#         client = self.bq_client
#         """
#         Source data file must be outer JSON
#         """
#         blob = client.get_bucket(bucket_name).blob(file_name)
#         body = json.loads(blob.download_as_string())
#         table_id = client.dataset(dataset).table(tableName)
#         job_config = bigquery.LoadJobConfig()
#         schema = create_schema_from_yaml(tableSchema)
#         job_config.schema = schema
#
#         df = pandas.io.json.json_normalize(data=body, record_path='addresses',
#                                            meta=['id', 'first_name', 'last_name', 'dob']
#                                            , record_prefix='addresses_'
#                                            , errors='ignore')
#
#         df = df[
#             [
#                 'id',
#                 'first_name',
#                 'last_name',
#                 'dob',
#                 'addresses_status',
#                 'addresses_address',
#                 'addresses_city',
#                 'addresses_state',
#                 'addresses_zip',
#                 'addresses_numberOfYears'
#             ]
#         ]
#
#         load_job = client.load_table_from_dataframe(
#             df,
#             table_id,
#             job_config=job_config,
#         )
#
#         load_job.result()
#         print("Job finished.")

# flake8: noqa
