split -l 3000 $1 data/masters/XML/partition_

python append.py

dir="data/masters/XML"
for f in "$dir"/*; do
  python xml2json.py -t xml2json -o $f".json" "$f"
  mv $f".json" data/masters/JSON
done

dir="data/masters/JSON"
for f in "$dir"/*; do
  mongoimport -d discogs_masters -c temp $f
done

mongo < aggregate_masters.js

echo "Done with importing $1."
