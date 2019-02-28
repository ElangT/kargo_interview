from solution import Job, Transporter, Bid
import unittest

class SortBidTest(unittest.TestCase):
    def setUp(self):
        self.job = Job()
        self.tr1 = Transporter("C", rating=4, trucks=["1", "2"])
        self.tr2 = Transporter("B", trucks=["1", "2"])
        self.tr3 = Transporter("A", trucks=["3", "1"])
        self.bid1 = self.tr1.create_bid(200, "1", self.job)
        self.bid2 = self.tr2.create_bid(100, "2", self.job)
        self.bid3 = self.tr3.create_bid(300, "3", self.job)      

    def test_default_sort(self):
        self.assertEqual(self.job.sort_bid(), [self.bid1, self.bid2, self.bid3])

    def test_rating_sort(self):
        self.assertEqual(self.job.sort_bid("rating")[0], self.bid1)

    def test_transporter_name_sort(self):
        self.assertEqual(self.job.sort_bid("transporter_name"), [self.bid3, self.bid2, self.bid1])

    def test_fail_sort(self):
        self.assertRaises(AttributeError, self.job.sort_bid, "weee")

if __name__ == '__main__':
    unittest.main()
