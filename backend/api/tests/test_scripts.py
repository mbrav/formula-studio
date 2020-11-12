from django.test import TestCase

# To run on a docker compose do:
# docker-compose run app sh -c "python manage.py test"

# Test functions 
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return y - x

# Run tests 
class CalcTests(TestCase):

    def test_num(self):
        """Test that nums are added"""
        self.assertEqual(add(3, 8), 11)
    
    def test_subtract_numbers(self):
        """Test that nums are subtracted"""
        self.assertEqual(subtract(5, 11), 6)