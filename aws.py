# -*- coding: utf-8 -*-
from boto import ses
from boto3 import client

class Ses():

    def __init__(self, aws_region, access_key, secret_key):
        self.conn = ses.connect_to_region(aws_region,
                                               aws_access_key_id=access_key,
                                               aws_secret_access_key=secret_key)        


    def send_email(self, sender, recipients, subject, body):
        self.conn.send_email(
                        sender,
                        subject,
                        body,
                        recipients,
                        html_body=body)

        return

class Kms():

    def __init__(self, aws_region, access_key, secret_key, key_arn):
        self.client = client("kms",
                             aws_region,
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key)
        self.key_arn = key_arn
        return

    def encrypt(self, payload, context = {}):
        response = self.client.encrypt(KeyId=self.key_arn,
                                  Plaintext=payload,
                                  EncryptionContext=context
                                  )
        return response["CiphertextBlob"]

    def decrypt(self, blob, context = {}):
        response = self.client.decrypt(CiphertextBlob=blob,
                                  EncryptionContext=context)
        return response["Plaintext"]