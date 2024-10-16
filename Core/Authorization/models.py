from django.db import models
import json

class HeaderRequest(models.Model):
    url = models.URLField(max_length=200)  # URL field to store the request URL
    cookies = models.TextField(blank=True, null=True)  # TextField to store cookies as JSON
    headers = models.TextField(blank=True, null=True)  # TextField to store headers as JSON
    payload = models.TextField(blank=True, null=True)  # TextField to store the payload as JSON

    def set_cookies(self, cookies_dict):
        """Set cookies as a JSON string."""
        self.cookies = json.dumps(cookies_dict)

    def get_cookies(self):
        """Get cookies as a dictionary."""
        return json.loads(self.cookies) if self.cookies else {}

    def set_headers(self, headers_dict):
        """Set headers as a JSON string."""
        self.headers = json.dumps(headers_dict)

    def get_headers(self):
        """Get headers as a dictionary."""
        return json.loads(self.headers) if self.headers else {}

    def set_payload(self, payload_dict):
        """Set payload as a JSON string."""
        self.payload = json.dumps(payload_dict)

    def get_payload(self):
        """Get payload as a dictionary."""
        return json.loads(self.payload) if self.payload else {}

    def __str__(self):
        return f'API Request to {self.url}'
