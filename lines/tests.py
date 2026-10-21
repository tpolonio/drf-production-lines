from django.urls import reverse
from rest_framework.test import APITestCase

from .models import ProductionLine


class ProductionLineApiTest(APITestCase):
    def test_create_line(self):
        response = self.client.post(
            reverse("line-list"),
            {"code": "MDF", "capacity": 800, "active": True},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["code"], "MDF")
        self.assertTrue(ProductionLine.objects.filter(code="MDF").exists())
