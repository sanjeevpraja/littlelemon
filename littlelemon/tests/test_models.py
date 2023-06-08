from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuItemTest(TestCase):
  def test_get_item(self):
    item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    serializer = MenuItemSerializer(item)
    self.assertEqual(str(item), 'IceCream : 80')
