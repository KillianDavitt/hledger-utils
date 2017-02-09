import sys
from datetime import datetime
values = dict()
with open(sys.argv[1]) as f:
    entries = f.readlines()

    
    for entry in entries[1:]:
        #print(entry)
        val = dict()
        vals = entry.split(',')
        val["date"] = vals[0]
        date = datetime.strptime(val["date"][:-1], "%d %b %Y")
        val["ref"] = vals[1]
        val["out"] = vals[2]
        val["in"] = vals[3]
        val["ex out"] = vals[4]
        val["ex in"] = vals[5]
        val["bal"] = vals[6]
        print(date.strftime("%Y/%m/%d"), end='')
        print(val["ref"], end='')
        if val["out"] == "  ":
            num = float(val["in"])
        else:
            num = -1 * float(val["out"])
        print("\n    assets:bank " + str(num))
        print("    expenses:misc")
        print("")
        #expenses:food

