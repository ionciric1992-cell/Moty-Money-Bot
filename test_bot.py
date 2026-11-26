import unittest
import ideas
import scripts


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


if __name__ == "__main__":
    unittest.main()
