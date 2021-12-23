import json
from django.urls import reverse
from rest_framework.test import APISimpleTestCase
from django.test import TransactionTestCase


class TestSetupAPI(TransactionTestCase):
    """setup API tests"""

    def setUp(self) -> None:
        # Define API URLs
        self.add_note_post_url = reverse("api:note-post")
        self.note_read_url = reverse("api:note-read")
        self.add_user_url = reverse("users:add-user")
        self.add_report_url = reverse("reports:report")

        # Create users
        user1_info = {
            "username": "user1",
            "email": "user1@mail.com",
            "password": "user1P@ss",
            "password2": "user1P@ss",
        }

        user2_info = {
            "username": "user2",
            "email": "user2@mail.com",
            "password": "user2P@ss",
            "password2": "user2P@ss",
        }

        self.user1_id = self.create_user(user1_info)["user"]["id"]
        self.user2_id = self.create_user(user2_info)["user"]["id"]

        # Create reports
        user1_payload = {"user": self.user1_id}
        user2_payload = {"user": self.user2_id}
        self.report1_id = self.create_report(user1_payload)["report"]["report_id"]
        self.report2_id = self.create_report(user2_payload)["report"]["report_id"]

        return super().setUp()

    def create_user(self, user_info):
        user = self.client.post(self.add_user_url, data=user_info)
        return json.loads(user.content)

    def create_report(self, user_payload):
        report = self.client.post(self.add_report_url, data=user_payload)
        return json.loads(report.content)

    def add_note(self, user_id, report_id, content, public):
        note_payload = {
            "content": content,
            "user_id": user_id,
            "public": public,
            "report_id": report_id,
        }

        note = self.client.post(self.add_note_post_url, data=note_payload)
        return note
