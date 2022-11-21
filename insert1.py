import numpy as np
np1=np.array([[1,2],[3,4]])
np2=np.insert(np1,0,([5,6],[7,8]),axis=0)
np3=np.insert(np1,0,([5,6],[7,8]),axis=1)
print(np1,end="\n")
print("\n")
print(np2,end="\n")
print("\n")
print(np3)