from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
  def setup(self, title_set, price_set, inventory_set):
    MenuItem.objects.create(title=title_set, price=price_set, inventory=inventory_set)

  def test_getall(self):
    self.setup('IceCream',80,100)
    self.setup('Cake',80,100)
    itemcount = MenuItem.objects.all().count()
    self.assertEqual(itemcount, 2)