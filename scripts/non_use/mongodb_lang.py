MongoDB Query Language


db.all_masters.find()
	returns all Documents



db.all_masters.find({_id: ObjectId("5d41e9823d07dc9f21d27fb3")},{"masters": 1})

	db.collection.find(<Document Identifier>, <Parameters>)
	returns the Document 
		whose _id is ObjectId("5d41e9823d07dc9f21d27fb3")
		only returns "masters" parameter


db.all_masters.find({_id: ObjectId("5d41e9823d07dc9f21d27fb3")},{"masters.masters.master": 1})

	. operator queries nested parameters

db.all_masters.findOne({_id: ObjectId("5d41e9823d07dc9f21d27fb3")}, {"masters.masters.master": { $elemMatch: {"main_release" : "23585"}}})

====================================================================================================

var docs = db.masters.aggregate({$unwind:'$masters'},{$unwind:'$masters.master'})
	
	set each master to one Document to docs

db.masters.updateOne({"_id" : ObjectId("5d4131063d07dc9f21d277c4")},docs, {upsert: true})
	update to this one separated masters. 1 master -> 1 doc

db.masters.findOne({"masters.master.artists.artist.name":"The Troggs", "masters.master.title" : "Greatest Hits"}, 
															{"masters.master.genres":1, "masters.master.styles":1})
	returns the genre and styles
	Query 
		artist: "The Troggs"
		title: "Greatest Hits"

====================================================================================================

# var docs = db.all_masters.aggregate([{$unwind:'$masters'},{$unwind:'$masters.master'},
# 		        { 
#             $group : {
#                 "_id" : null, 
#                 "master" : {
#                     "$addToSet" : "$master"
#                 }
#             }
#         }])



# db.all_masters.aggregate([
#   {"$group":{
#     "_id":null,
#     "$results": {}
#   }},
#   {"$replaceRoot":{"newRoot":"$results"}}
# ])

docs = db.all_masters.aggregate({$unwind: {path: "$masters.master"}})

docs = db.all_masters.aggregate({"_id": null, masters: {$mergeObjects: "$masters"}})




db.masters_edit.insert(docs.toArray())

	inserts aggregate to new collection


--------------------
=====AGGREGATE======
--------------------
var docs = db.all_masters.aggregate([{$unwind: {path: "$masters"}}, {$unwind: {path: "$masters.master"}}, {$project: {_id: 0}}])
db.<collection>.insert(docs.toArray())

db.master_edit_5.find({"masters.master.artists.artist.name": "I.O.S.", "masters.master.title": "Bum Bum Tot / Running"},{"_id": 0, "masters.master.genres": 1, "masters.master.styles": 1})


--------------------------
=====final AGGREGATE======
--------------------------
var docs = db.all_masters.aggregate([{$unwind: {path: "$masters"}}, {$unwind: {path: "$masters.master"}}, {$project: {_id: 0}}])
db.all_masters_final.insert(docs.toArray())

// "masters.master.artists.artist.name"     = "Brian Eno"
// "masters.master.title"				    = "Apollo"

var artist   = "Kiefer"
var album    = "Kickinit Alone"

db.all_masters_final.findOne({"masters.master.artists.artist.name":  {$regex: artist}, "masters.master.title": {$regex: album}},{"_id": 0, "masters.master.genres": 1, "masters.master.styles": 1})





