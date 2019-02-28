#!/usr/bin/python
dows = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
with open("in.txt") as fp:
        next(fp) # we don't need the first line, not sure why it's even in there, throw it away
        for line in fp:
                dow,dom = line.split()
                row,dnum = divmod(int(dom)+dows.index(dow)-1, 7) # the math that makes it all easy - work smarter, not harder
                if (int(dom) > 9):
                        print row, dnum*3, (dnum*3)+1
                else:
                        print row, (dnum*3)+1
