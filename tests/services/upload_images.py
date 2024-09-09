import unittest
from io import BytesIO
from app import create_app, db
from flask import url_for

class TestImageUpload(unittest.TestCase):

    def setUp(self):
        """Set up a test app and test client"""
        self.app = create_app('config.TestConfig')  # Use a test config
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Create test database

        # Add a test user here if you have authentication

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()
        db.drop_all()  # Drop the test database
        self.app_context.pop()

    def login(self):
        """Helper function to log in"""
        self.client.post(url_for('auth.login'), data={
            'username': 'testuser',
            'password': 'testpassword'
        })

    def test_image_upload_empty(self):
        """Test uploading an empty image file"""
        self.login()  # Assuming login is required for upload

        response = self.client.post(
            url_for('main.upload_image'),
            data={'image': (BytesIO(b''), '')},  # Empty file
            content_type='multipart/form-data',
            follow_redirects=True
        )

        # Check that the file was rejected
        self.assertIn(b'No file selected', response.data)

    def test_image_upload_valid(self):
        """Test uploading a valid image file"""
        self.login()  # Assuming login is required for upload

        data = {
            'image': (BytesIO(b'my file contents'), 'test_image.png')
        }
        response = self.client.post(
            url_for('main.upload_image'),
            data=data,
            content_type='multipart/form-data',
            follow_redirects=True
        )

        # Check for a successful upload
        self.assertIn(b'Image uploaded successfully!', response.data)

    def test_image_upload_invalid_format(self):
        """Test uploading an invalid file format"""
        self.login()  # Assuming login is required for upload

        data = {
            'image': (BytesIO(b'my file contents'), 'test_file.txt')
        }
        response = self.client.post(
            url_for('main.upload_image'),
            data=data,
            content_type='multipart/form-data',
            follow_redirects=True
        )

        # Check that it raises an invalid format error (this depends on your validation logic)
        self.assertIn(b'Invalid file format', response.data)  # Example flash message

if __name__ == '__main__':
    unittest.main()
