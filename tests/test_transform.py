import unittest

from job import transform


class TransformTestCase(unittest.TestCase):

    def test_transform(self):
        cust_id, score = transform(("8625", {}))
        self.assertEqual("8625", cust_id)
        self.assertEqual(score, "Good")