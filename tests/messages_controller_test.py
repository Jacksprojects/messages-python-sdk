# -*- coding: utf-8 -*-

"""
    message_media_messages

    This file was automatically generated for MessageMedia by APIMATIC v2.0 ( https://apimatic.io ).
"""

import unittest

from message_media_messages.exceptions.api_exception import APIException
from tests.test_configuration import TestConfiguration
from tests.test_util import TestUtility
from message_media_messages.message_media_messages_client import MessageMediaMessagesClient


class MessageControllerTest(unittest.TestCase):

    # Testing successful post request to endpoint
    def test_successful_post_request_with_hmac_auth_to_endpoint(self):
        use_hmac_authentication = True
        body = TestUtility.create_body()

        client = MessageMediaMessagesClient(use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.send_messages(body)
        self.assertIsNotNone(result)

    # Testing unsupported request raises exception
    def test_unsuccessful_request_with_hmac_auth_raises_exception(self):
        hmac_auth_user_name = 'wrong'
        hmac_auth_password = 'value'
        use_hmac_authentication = True
        body = TestUtility.create_body()

        client = MessageMediaMessagesClient(hmac_auth_user_name, hmac_auth_password, use_hmac_authentication)
        messages_controller = client.messages

        with self.assertRaises(APIException) as context_manager:
            messages_controller.send_messages(body)
        raised_exception = context_manager.exception
        self.assertIsNotNone(raised_exception)

    # Testing successful get request endpoint
    def test_successful_get_request_with_hmac_auth_to_endpoint(self):
        expected_id = '{}'.format(TestConfiguration.request_message_id)
        use_hmac_authentication = True

        client = MessageMediaMessagesClient(use_hmac_authentication)
        messages_controller = client.messages

        result = messages_controller.get_message_status(expected_id)
        actual_id = result.message_id
        assert actual_id == expected_id
