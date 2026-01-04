# Triple quotes are string literals / multi-line strings not comments 
# 
# init.py
# -> helps in setting path locations
# -> We can leave both __init__.py files blank, but then we’ll have to write 
# code like 
#             mymath.add.add(x,y)     
# which is pretty ugly
#
# To use this
# Method 1: Copy this folder 'mymath' into your Python’s site-packages folder
#          and then use it as an import
#
# Method 2: You can edit the path on the fly in your test code

#    modify this path to match your environment
#    sys.path.append('C:\Users\phenomsg\Documents')



from .add import add
from .subtract import subtract
from .adv.sqrt import sqrt


