#---Using Unit tests---# examples
import unittest
from testing import eat

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """Testing Healthy""" #to get these to show run python file_name.py -v 
        self.assertEqual(
                eat("broccoli", is_healthy=True),
                "I'm eating broccoli, because it is healthy."
            )
    def test_eat_healthy_bool(self):
        """is_healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat("Pizza", is_healthy="who cars")

    def test_eat_unhealthy(self):
        """Testing Unhealthy"""
        self.assertEqual(
                eat("pizza", is_healthy=False),
                "I'm eating pizza, because YOLO!"
            )

if __name__ == "__main__":
    unittest.main()