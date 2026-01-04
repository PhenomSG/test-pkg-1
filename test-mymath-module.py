# this file tests mymath module working
#
# path:/home/phenomsg/Documents/test-pkg-1/mymath

import sys

sys.path.append('/home/phenomsg/Documents/test-pkg-1/mymath')
import mymath

print(mymath.add(5,5))
print(mymath.subtract(5,5))
print(mymath.sqrt(9))

