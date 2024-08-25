import unittest
from analyze_purchases.calculations import calculate_statistics


class TestCalculations(unittest.TestCase):

    def test_calculate_statistics(self):
        data = [
                {
                    "purchase_id": "1",
                    "items": [
                        {"product_name": "A", "quantity": 2, "price": "10.0"},
                        {"product_name": "B", "quantity": 1, "price": "20.0"}
                    ]
                },
                {
                    "purchase_id": "2",
                    "items": [
                        {"product_name": "C", "quantity": 1, "price": "30.0"},
                        {"product_name": "A", "quantity": 1, "price": "10.0"}
                    ]
                }
            ]

        expected_output = {
            "total_volume_spend": 80.0,
            "average_purchase_value": 20.0,
            "maximum_purchase_value": 30.0,
            "median_purchase_value": 20.0,
            "number_of_unique_products_purchased": 3
        }

        results = calculate_statistics(data)
        self.assertAlmostEqual(results['total_volume_spend'], expected_output['total_volume_spend'])
        self.assertAlmostEqual(results['average_purchase_value'], expected_output['average_purchase_value'], places=2)
        self.assertAlmostEqual(results['maximum_purchase_value'], expected_output['maximum_purchase_value'])
        self.assertAlmostEqual(results['median_purchase_value'], expected_output['median_purchase_value'])
        self.assertEqual(results['number_of_unique_products_purchased'],
                         expected_output['number_of_unique_products_purchased'])


if __name__ == '__main__':
    unittest.main()
