import re
import os
with open('basic.csv') as read:
    with open('frames.csv','wt') as write:
        for line in read:
            stem = line[0:-5]
            stem = stem +'\n'
            write.write(stem)
	
    
