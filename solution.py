class Job:
    def __init__(self):
        self.bids = []
    def add_bid(self, bid):
        self.bids.append(bid)
    def sort_bid(self, sort_type="name", reverse=False):
        try:
            return sorted(self.bids, key=lambda x: getattr(x, sort_type), reverse=reverse)
        except AttributeError:
            return self.bid

class Transporter:
    def __init__(self, name, rating=0, trucks=None):
        self.name = name
        self.rating = 0.0
        if(trucks):
            self.trucks = trucks
        else:
            self.trucks = []

    def create_bid(self, budget, truck_name, job):
        if(truck_name in self.trucks):
            job.add_bid(Bid(self, budget, truck_name))
        else:
            raise LookupError("{} don't exist inside {}'s truck list".format(truck_name, self.name))

    @staticmethod
    def sort_job(sort_type="budget"):
        pass

class Bid:
    def __init__(self, transporter, budget, truck):
        self.transporter = transporter
        self.budget = budget
        self.truck = truck

    @property
    def name(self):
        return self.transporter.name

    @property
    def rating(self):
        return self.transporter.rating
    
    def __repr__(self):
        return self.transporter.name + " " + self.truck + " " + str(self.budget)

if __name__ == '__main__':
    job = Job()
    tr = Transporter("C", rating=4, trucks=["1", "2"])
    tr2 = Transporter("B", trucks=["1", "2"])
    tr3 = Transporter("A", trucks=["3", "1"])
    tr.create_bid(100, "1", job)
    tr2.create_bid(200, "2", job)
    tr3.create_bid(300, "3", job)
    print(job.sort_bid("truck", reverse=True))