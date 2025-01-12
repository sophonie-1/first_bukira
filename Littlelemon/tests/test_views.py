from restaurant.views import MenuSerializerView
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MenuSerializerViewTest(APITestCase):
    def setUp(self):
        """
        Set up test data and authentication for the test case.
        """
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)

        # Add authentication token to the client
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        print(self.token.key,self.user)

        # Create menu items
        self.menu_item1 = Menu.objects.create(title="Pizza", price=10.99, inventory=5)
        self.menu_item2 = Menu.objects.create(title="Burger", price=5.49, inventory=10)
        self.menu_item3 = Menu.objects.create(title="Salad", price=4.99, inventory=7)
        print(self.menu_item1)

        # Define the endpoint
        self.url = "/menu/"  # Adjust the endpoint URL to match your project

    def test_getall(self):
        """
        Test retrieving all menu items.
        """
        # Make a GET request to the endpoint
        response = self.client.get(self.url)

        # Serialize the data from the database
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        """
        Test creating a new menu item.
        """
        # Define the data for a new menu item
        new_menu_item = {
            "title": "Pasta",
            "price": 8.99,
            "inventory": 12
        }

        # Make a POST request to the endpoint
        response = self.client.post(self.url, new_menu_item)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 4)  # Three items from setUp + one new
        self.assertEqual(Menu.objects.last().title, "Pasta")
