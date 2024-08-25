import io
import unittest
from click.testing import CliRunner
from analyze_purchases.cli import analyze_purchases, load_and_validate_json

class TestCLI(unittest.TestCase):
    #
    # def test_load_purchase_data(self):
    #     sample_data = '{"purchases": [{"product_id": "A", "quantity": 2, "price_per_unit": 10.0}]}'
    #     file = io.StringIO(sample_data)
    #     data = load_and_validate_json(file)
    #     self.assertEqual(len(data["purchases"]), 1)
    #     self.assertEqual(data["purchases"][0]["product_id"], "A")

    def test_analyze_purchases(self):
        runner = CliRunner()
        sample_data = '''
        [
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
        '''
        with runner.isolated_filesystem():
            with open('input.json', 'w') as f:
                f.write(sample_data)
            result = runner.invoke(analyze_purchases, ['input.json'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('"total_volume_spend": 80.0', result.output)

if __name__ == '__main__':
    unittest.main()
