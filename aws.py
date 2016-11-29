# -*- coding: utf-8 -*-
from boto import ses

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