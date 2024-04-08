import os
from typing import List, Optional

import boto3
import dotenv

dotenv.load_dotenv()


class S3Client:
    def __init__(
        self, access_key: Optional[str] = None, secret_key: Optional[str] = None
    ):
        """
        Initialize the AWS S3 client.
        """
        if access_key is None:
            self.access_key = os.getenv("AWS_ACCESS_KEY_ID")
        else:
            self.access_key = access_key
        if secret_key is None:
            self.secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        else:
            self.secret_key = secret_key
        self.session = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

    def get_file_names(self, bucket_name: str, file_prefix: str) -> List:
        """
        Get the list of files in the S3 bucket.
        :param bucket_name: The name of the s3 bucket.
        :param file_prefix: The prefix of the file.
        :return: List: The list of file paths in the S3 bucket.
        """
        s3 = self.session.resource("s3")

        my_bucket = s3.Bucket(bucket_name)

        list_log_files = []

        for objects in my_bucket.objects.filter(Prefix=file_prefix):
            list_log_files.append(f"{bucket_name}/{objects.key}")

        return list_log_files
