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

Mapping Problem
Start Shipping -> 
Start Transporter ->

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
	Fungsionalitas:
		Sort Bid(type)
		Sort Job(type)
		CreateBid
	Buat test