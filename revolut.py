import sys
from datetime import datetime

categories = eval(open(".revolut.conversion").read())
with open(sys.argv[1]) as f:
    entries = f.readlines()
    
    for entry in entries[1:]:
        val = dict()
        vals = entry.split(',')

        date = vals[0]
        date = datetime.strptime(date[:-1], "%d %b %Y")
        ref = vals[1]
        out_str = vals[2]
        in_str = vals[3]

        print(date.strftime("%Y/%m/%d"), end='')
        print(ref, end='')
        if out_str == "  ":
            num = float(in_str)
        else:
            num = -1 * float(out_str)
        print("\n    assets:bank     " + str(num))

        done = False
        for key, val in categories.items():
            if key in ref:
                print("    expenses:" + val)
                done = True
                break
        if not done:
            print("    expenses:misc")
        print("")

    f.close()

