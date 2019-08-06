split -l 3000 $1 data/masters/XML/partition_

python scripts/append.py

dir="data/masters/XML"
for f in "$dir"/*; do
  python scripts/xml2json.py -t xml2json -o $f".json" "$f"
  mv $f".json" data/masters/JSON
done

  # python scripts/xml2json.py -t xml2json -o data/masters/XML/partition_sv.json data/masters/XML/partition_sv
  # mv data/masters/XML/partition_sv.json data/masters/JSON

dir="data/masters/JSON"
for f in "$dir"/*; do
  mongoimport -d discogs_masters -c temp $f
done

# mongoimport -d discogs_masters -c temp data/masters/JSON/partition_sv.json

mongo < scripts/aggregate_masters.js

echo "Done with importing $1."
