# Mocking the count distance
def count_distance(origin, destination):
    return 1

class Shipper:
    def __init__(self):
        self.jobs = []

    def create_job(self, budget, origin, destination, ship_date, ship_duration):
        job = Job(budget, origin, destination, ship_date, ship_duration)
        self.jobs.append(job)
        return job

class Job:
    def __init__(self, budget, origin, destination, ship_date, ship_duration):
        self.budget = budget
        self.origin = origin
        self.destination = destination
        self.ship_date = ship_date
        self.ship_duration = ship_duration
        self.distance = count_distance(self.origin, self.destination)
        self.bids = []
    
    def add_bid(self, bid):
        self.bids.append(bid)
    def sort_bid(self, sort_type="truck_name", reverse=False):
        try:
            return sorted(self.bids, key=lambda x: getattr(x, sort_type), reverse=reverse)
        except AttributeError:
            raise AttributeError("{} is not a valid sort_type", sort_type)

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
            bid = Bid(self, budget, truck_name)
            job.add_bid(bid)
            return bid
        else:
            raise LookupError("{} don't exist inside {}'s truck list".format(truck_name, self.name))

    @classmethod
    def sort_job(cls, job_market, sort_type="budget", reverse=False):
        try:
            return sorted(job_market, key=lambda x: getattr(x, sort_type), reverse=reverse)
        except AttributeError:
            raise AttributeError("{} is not a valid sort_type", sort_type)
        

class Bid:
    def __init__(self, transporter, budget, truck):
        self.transporter = transporter
        self.budget = budget
        self.truck_name = truck

    @property
    def transporter_name(self):
        return self.transporter.name

    @property
    def rating(self):
        return self.transporter.rating
