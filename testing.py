import unittest
from geo_requests import get_location_data

class TestGeocodingUtility(unittest.TestCase):
    def test_valid_city_state(self):
        result = get_location_data("Madison, Wisconsin")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Madison")
        self.assertEqual(result["state"], "Wisconsin")
        self.assertAlmostEqual(result["lat"], 43.0749, places=2)
        self.assertAlmostEqual(result["lon"], -89.3810, places=2)

    def test_valid_city_that_also_state(self):
        result = get_location_data("New York")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "New York County")
        self.assertEqual(result["state"], "New York")
        self.assertAlmostEqual(result["lat"], 40.7128, places=2)
        self.assertAlmostEqual(result["lon"], -74.0060, places=2)

    def test_valid_zip_code(self):
        result = get_location_data("53706")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Madison")
        #self.assertEqual(result["state"], "Wisconsin")
        self.assertAlmostEqual(result["lat"], 43.0749, places=2)
        self.assertAlmostEqual(result["lon"], -89.3810, places=1)

    def test_invalid_location(self):
        result = get_location_data("NonexistentCity")
        self.assertIsNone(result)

    def test_multiple_locations(self):
        result = get_location_data("Chicago")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Chicago")
        self.assertEqual(result["state"], "Illinois")

if __name__ == "__main__":
    unittest.main()