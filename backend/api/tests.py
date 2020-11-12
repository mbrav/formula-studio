from django.test import TestCase
from api.scripts import *

# To run on a docker compose do:
# docker-compose run app sh -c "python manage.py test"

class CalcTests(TestCase):

    def test_num(self):
        """Test that nums are added"""
        self.assertEqual(add(3, 8), 11)
    
    def test_subtract_numbers(self):
        """Test that nums are subtracted"""
        self.assertEqual(subtract(5,11), 6)
