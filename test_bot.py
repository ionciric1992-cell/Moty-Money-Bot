import unittest
import tempfile
import os

import ideas
import scripts
import analytics
import accounts


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
        self.assertIn("hashtags", result)

    def test_script_has_duration(self):
        result = scripts.generate_script("Money")

        self.assertEqual(result["duration_seconds"], 20)

    def test_script_has_five_hashtags(self):
        result = scripts.generate_script("Success")

        self.assertEqual(len(result["hashtags"]), 5)

    def test_analytics_record_video(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            original_file = analytics.DATA_FILE
            analytics.DATA_FILE = os.path.join(
                temp_dir, "performance.csv"
            )

            try:
                analytics.record_video(
                    "test_user",
                    "Motivation",
                    1000,
                    100,
                    20,
                    10,
                )

                rows = analytics.load_performance()

                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0]["username"], "test_user")
                self.assertEqual(rows[0]["views"], "1000")
                self.assertEqual(rows[0]["engagement"], "13.0")

            finally:
                analytics.DATA_FILE = original_file

    def test_accounts_save_and_load(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            original_file = accounts.ACCOUNTS_FILE
            accounts.ACCOUNTS_FILE = os.path.join(
                temp_dir, "accounts.json"
            )

            try:
                accounts.save_accounts([
                    {
                        "username": "test_user",
                        "niche": "Motivation",
                        "goal": "Growth",
                        "active": True,
                    }
                ])

                result = accounts.load_accounts()

                self.assertEqual(len(result), 1)
                self.assertEqual(result[0]["username"], "test_user")

            finally:
                accounts.ACCOUNTS_FILE = original_file


if __name__ == "__main__":
    unittest.main()
