from django.test import TestCase
from restaurant.models import Menu,Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="book",price=200,inventory=2)
        book= Booking.objects.create(name="python",no_of_guests=2,booking_date='2000-03-02,00:00')
        self.assertEqual(str(item),"book:200")
        self.assertEqual(str(book),"python")