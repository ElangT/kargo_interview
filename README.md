# kargo_interview
Kargo Interview


Requirements:

	Shipper:
		Sort By:
			Truk
			Budget
			Transporter Name
			Rating Transporter


	Transporter
		Sort By:
			Budget
			Distance # origin-destination
			Origin
			Destination
			Ship Date
			Ship Duration

Mapping Problem:

	Start Shipping -> Input Jobs -> Input Bid -> Sort Bid

	Start Transporter -> Sort Jobs -> Input Bid

Solution Structure:

	Entity:
		Shipper:
			Attribute:
				list of job
		Job
			Attribute:
				Budget
				Distance # origin-destination
				Origin
				Destination
				Ship Date
				Ship Duration
			Method:
				Sort Bid
		Transporter
			Attribute:
				Rating
				list of truk
				Name
			Method
				Check Job
				Sort Job
				Create Bid
		Bid
			Attribute
				Refrence Transporter
				Truk
				Budget
				Transporter.Rating
				Transporter.Name

Data structure

	Shipper has many job
	Job has many Bid
	Transporter has many Bid
	Transporter has many Truck

Pseudo Code

	Class Shipper
		getAttribute()
		createJob()

	Class Job
		getAttribute()
		SortBid(sort_type)

	Class Transporter
		getAttribute()
		SortJob(sort_type)
		CreateBid(job)

	Class Bid
		getAttribute()

Planning

	1. Sort Bids functionality
		Transporter
			- create bid
		Job
			- add bid
			- sort bid
		Bid
			- getter for some attribute

	2. Sort Jobs functionality
		Shipper
			- Create Job
		Transporter
			- Sort Bid

	Buat test for every functionality?

	3. Other functionality
		Assure the uniqueness of Transporter and Shipper

	Fix the import issue if in different .py file