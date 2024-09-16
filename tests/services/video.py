import unittest
from flask import Flask
from flask_login import current_user
from webapp.auth.models import User
from webapp.chat.models import Message
from app import app
from webapp import db
from unittest.mock import patch

class VideoCallTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test app and push app context."""
        # Push the app context
        self.app_context = app.app_context()
        self.app_context.push()

        # Set the test client and app testing mode
        self.client = app.test_client()
        app.testing = True

        # Create the test database
        db.create_all()

        # Create and add test user and doctor to the database
        self.test_user =  User.query.filter_by(username="testuser").first()
        self.test_doctor = User.query.filter_by(username="testdoctor").first()
        db.session.add_all([self.test_user, self.test_doctor])
        db.session.commit()

    def tearDown(self):
        """Clean up after tests by popping the app context and dropping the test DB."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    @patch('flask_login.utils._get_user', return_value=None)
    def test_post_video_call_form(self, mock_get_user, mock_commit, mock_add):
        """Test posting the video call form with valid data."""
        # Simulate a POST request with form data for video call ID and doctor ID
        response = self.client.post('/your_video_call_route', data={
            'videoCallID': '123456789',  # Simulated WhatsApp number or video call ID
            'doctorId': str(self.test_doctor.id),  # Simulated doctor ID
        }, follow_redirects=True)

        # Check if the data was processed correctly
        mock_add.assert_called_once()  # Ensure db.session.add was called
        mock_commit.assert_called_once()  # Ensure db.session.commit was called

        # Verify that the Message object was created with correct values
        msg = mock_add.call_args[0][0]
        self.assertEqual(msg.phone_number, '123456789')
        self.assertEqual(msg.sender_id, self.test_user.id)
        self.assertEqual(msg.receiver_id, self.test_doctor.id)

        # Check if flash message was displayed in the response
        self.assertIn(b'whatsapp number sent', response.data)

if __name__ == '__main__':
    unittest.main()
