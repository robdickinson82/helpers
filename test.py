# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
sys.path.append(".")

import unittest

import logging

from config import LOG_PATH, LOG_FORMAT, AWS_KMS_SECRET_KEY, AWS_KMS_ACCESS_KEY, AWS_REGION, KMS_KEY_ARN
from aws import Kms

logging.basicConfig(filename=LOG_PATH+'helpers_tests.log',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)


class TestBasicKMS(unittest.TestCase):

    def test_create_client(self):
        kms_client = Kms(AWS_REGION, AWS_KMS_ACCESS_KEY, AWS_KMS_SECRET_KEY, KMS_KEY_ARN)
        return

    def test_encrypt_decrypt(self):
        kms_client = Kms(AWS_REGION, AWS_KMS_ACCESS_KEY, AWS_KMS_SECRET_KEY, KMS_KEY_ARN)
        plain_text = b"Hello World"
        context = {"type": "testData"}
        cipher_text = kms_client.encrypt(plain_text, context)
        decrypted_text = kms_client.decrypt(cipher_text, context)
        self.assertEqual(decrypted_text, plain_text)
        return


if __name__ == '__main__':
    logging.info('Starting HelperTests')
    unittest.main()
    logging.info('Starting HelperTests')
