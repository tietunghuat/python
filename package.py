 #封包
#  要先建立一個__init__.py
import packet.point as p
print("Result of distance:", p.distance(2, 3))
result=p.distance(5,8)
print("Result of distance:",result)

import packet.line as line
print("Line slope:",line.slope(1,2,8,9))

#資料夾裡的子資料夾
# import packet.secondpacket.pa as pi
# print("PI:",pi.pa())