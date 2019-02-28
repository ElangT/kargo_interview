from solution import Job, Transporter, Bid
import unittest
from datetime import datetime

class SortBidTest(unittest.TestCase):
    def setUp(self):
        self.job = Job(100, "A", "B", datetime.strptime('Jun 3 2019', '%b %d %Y'), 30)
        self.tr1 = Transporter("C", rating=6, trucks=["1", "2"])
        self.tr2 = Transporter("B", rating=5, trucks=["1", "2"])
        self.tr3 = Transporter("A", rating=1, trucks=["3", "1"])
        self.bid1 = self.tr1.create_bid(200, "1", self.job)
        self.bid2 = self.tr2.create_bid(100, "2", self.job)
        self.bid3 = self.tr3.create_bid(300, "3", self.job)      

    def test_default_sort(self):
        self.assertEqual(self.job.sort_bid(), [self.bid1, self.bid2, self.bid3])

    def test_rating_sort(self):
        self.assertEqual(self.job.sort_bid("rating")[0], self.bid3)

    def test_transporter_name_sort(self):
        self.assertEqual(self.job.sort_bid("transporter_name"), [self.bid3, self.bid2, self.bid1])

    def test_fail_sort(self):
        self.assertRaises(AttributeError, self.job.sort_bid, "weee")


class SortJobTest(unittest.TestCase):
    def setUp(self):
        self.job1 = Job(100, "A", "B", datetime.strptime('Jun 3 2019', '%b %d %Y'), 30)
        self.job2 = Job(200, "B", "C", datetime.strptime('Jun 1 2019', '%b %d %Y'), 31)
        self.job3 = Job(300, "A", "C", datetime.strptime('Jun 2 2019', '%b %d %Y'), 34)
        self.market = [self.job1, self.job2, self.job3]

    def test_default_sort(self):
        self.assertEqual(Transporter.sort_job(self.market), [self.job1, self.job2, self.job3])

    def test_start_date_sort(self):
        self.assertEqual(Transporter.sort_job(self.market, "ship_date"), [self.job2, self.job3, self.job1])

    def test_fail_sort(self):
        self.assertRaises(AttributeError, Transporter.sort_job, self.market,"weee")

if __name__ == '__main__':
    unittest.main()
