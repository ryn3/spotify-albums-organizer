db = connect("localhost:27017/discogs_masters");

var docs = db.temp.aggregate([{$unwind: {path: "$masters"}}, {$unwind: {path: "$masters.master"}}, {$project: {_id: 0}}])
db.current_masters.insert(docs.toArray())
db.temp.drop()