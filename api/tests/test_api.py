import json
import os
from django.core.files import File
from .tests_setup import TestSetupAPI
from django.core.files.uploadedfile import SimpleUploadedFile

from users.models import User
from api.models import Report

PATH_TO_FILES = os.path.join(os.path.dirname(__file__), "files")


class TestAPI(TestSetupAPI):
    """API tests"""

    def test_add_note(self):

        # user 1 adding private note to report 1

        file = File(open(f"{PATH_TO_FILES}/room.jpg", "rb"))

        note1_payload = {
            "content": "1_private",
            "file": file,
            "user_id": "1",
            "public": "false",
            "report_id": self.report1_id,
        }

        note1 = self.client.post(self.add_note_post_url, data=note1_payload)
        print(f"{note1.content=}")
        self.assertEqual(note1.status_code, 201)

    def test_uploaded_file_extension_size(self):
        file = File(open(f"{PATH_TO_FILES}/big.jpg", "rb"))

        note1_payload = {
            "content": "1_private",
            "file": file,
            "user_id": "1",
            "public": "false",
            "report_id": self.report1_id,
        }

        note1 = self.client.post(self.add_note_post_url, data=note1_payload)
        print(f"{note1.content=}")
        self.assertEqual(note1.status_code, 400)

        file = File(open(f"{PATH_TO_FILES}/stam.exe", "rb"))

        note1_payload = {
            "content": "1_private",
            "file": file,
            "user_id": "1",
            "public": "false",
            "report_id": self.report1_id,
        }

        note1 = self.client.post(self.add_note_post_url, data=note1_payload)
        print(f"{note1.content=}")
        self.assertEqual(note1.status_code, 400)

    def test_note_visibility(self):

        # Create notes from user 1 to report 1
        note1 = self.add_note(
            self.user1_id, self.report1_id, "This is public note 1", True
        )

        note2 = self.add_note(
            self.user1_id, self.report1_id, "This is public note 2", True
        )

        note3 = self.add_note(
            self.user1_id, self.report1_id, "This is private note 3", False
        )

        # User 1 to read all 3 notes
        read = self.client.get(
            f"{self.note_read_url}?report_id={self.report1_id}&user_id={self.user1_id}"
        )
        notes = json.loads(read.content)["notes"]

        print(f"User {self.user1_id} read {len(notes)} notes")
        self.assertEqual(len(notes), 3)

        # User 2 to read only the two public notes
        read = self.client.get(
            f"{self.note_read_url}?report_id={self.report1_id}&user_id={self.user2_id}"
        )
        notes = json.loads(read.content)["notes"]

        print(f"User {self.user2_id} read {len(notes)} notes")
        self.assertEqual(len(notes), 2)
