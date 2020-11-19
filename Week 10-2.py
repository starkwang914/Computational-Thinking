t=123
h=t//60
m=t%60
print(t,"是",h,"小時",m,"分鐘")

h1=int(t/60)
m1=((t/60)-h1)*60
import math
m1=round(m1)
print(t,"是",h1,"小時",m1,"分鐘")