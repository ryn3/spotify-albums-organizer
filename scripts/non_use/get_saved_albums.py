import json
import optparse
import sys
import os
from collections import OrderedDict

def main():
    p = optparse.OptionParser(
        description='Imports JSON files of saved Spotify albums to MongoDB database and collection',
        prog='get_saved_albums',
        usage='%prog -t xml2json -o file.json [file]'
    )
    p.add_option('--type', '-t', help="'xml2json' or 'json2xml'", default="xml2json")
    p.add_option('--out', '-o', help="Write to OUT instead of stdout")
    p.add_option(
        '--strip_text', action="store_true",
        dest="strip_text", help="Strip text for xml2json")
    p.add_option(
        '--pretty', action="store_true",
        dest="pretty", help="Format JSON output so it is easier to read")
    p.add_option(
        '--strip_namespace', action="store_true",
        dest="strip_ns", help="Strip namespace for xml2json")
    p.add_option(
        '--strip_newlines', action="store_true",
        dest="strip_nl", help="Strip newlines for xml2json")
    options, arguments = p.parse_args()

    inputstream = sys.stdin
    if len(arguments) == 1:
        try:
            inputstream = open(arguments[0])
        except:
            sys.stderr.write("Problem reading '{0}'\n".format(arguments[0]))
            p.print_help()
            sys.exit(-1)

    input = inputstream.read()

    strip = 0
    strip_ns = 0
    if options.strip_text:
        strip = 1
    if options.strip_ns:
        strip_ns = 1
    if options.strip_nl:
        input = input.replace('\n', '').replace('\r','')
    if (options.type == "xml2json"):
        out = xml2json(input, options, strip_ns, strip)
    else:
        out = json2xml(input)

    if (options.out and out != None):
        file = open(options.out, 'w')
        file.write(out)
        file.close()
    else:
        print("fix: "+str(arguments))

if __name__ == "__main__":
    main()

