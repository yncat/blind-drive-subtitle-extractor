import argparse
import sys
import pandas as pd

def checkargs(args):
    if args.list_languages:
        return True
    # end list languages
    missing = ["--%s" % (x) for x in ["input", "output", "language"] if not getattr(args, x)]
    if len(missing)>0:
        sys.stderr.write("You must specify the following options. Run extract.py --help for details:\n%s\n" % "\n".join(missing))
        return False
    # end error
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Path to the input file", required=True)
    parser.add_argument("-o", "--output", help="Path to the output file")
    parser.add_argument("-l", "--language", help="language of the subtitle to extract")
    parser.add_argument("--include-original", help="include original english text as well", action="store_true")
    parser.add_argument("--list-languages", help="show available languages and exit", action="store_true")
    args = parser.parse_args()
    if not checkargs(args):
        return 1
    # end error
    df = pd.read_csv(args.input)
    if args.list_languages:
        exc = "event,marker,sound,character,directions,en,comments,character #,time,duration".split(",")
        langs = [x for x in list(df.columns) if (not x in exc)]
        print("The following languages are available:\n%s" % "\n".join(langs))
        return 0
    # end list languages
    if not args.language in df.columns:
        sys.stderr.write("Language %s is not found.\n" % args.language)
        return 1
    # end language not found
    flt = ["event", "character", args.language]
    if args.include_original:
        flt.append("en")
    extracted = df.loc[:, flt]
    extracted.to_csv("output.csv", index=False)
    return 0

sys.exit(main())