
import unittest
import csv
import os
import ideas
import scripts
import analytics


class TestMotyBot(unittest.TestCase):

    def test_generate_ideas(self):
        result = ideas.generate_ideas(5)
        self.assertEqual(len(result), 5)

    def test_generate_one_idea(self):
        result = ideas.generate_ideas(1)
        self.assertEqual(len(result), 1)

    def test_generate_script(self):
        result = scripts.generate_script("Motivation")
        self.assertEqual(result["topic"], "Motivation")
        self.assertIn("hook", result)
        self.assertIn("body", result)
        self.assertIn("cta", result)

    def test_record_video(self):
        old_file = analytics.DATA_FILE
        analytics.DATA_FILE = "test_performance.csv"

        try:
            if os.path.exists(analytics.DATA_FILE):
                os.remove(analytics.DATA_FILE)

            analytics.record_video(
                "test_user", "Motivation", 1000, 100, 20, 30
            )

            self.assertTrue(os.path.exists(analytics.DATA_FILE))

            with open(
                analytics.DATA_FILE,
                newline="",
                encoding="utf-8"
            ) as file:
                rows = list(csv.DictReader(file))

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["username"], "test_user")
            self.assertEqual(rows[0]["views"], "1000")
            self.assertEqual(rows[0]["engagement"], "15.0")

        finally:
            if os.path.exists(analytics.DATA_FILE):
                os.remove(analytics.DATA_FILE)

            analytics.DATA_FILE = old_file


if __name__ == "__main__":
    unittest.main()
