# 載入模組




# import sys
# import sys as s
import sys
print(sys.platform)
print(sys.maxsize)

#利用別名
import sys as system
print(system.platform)
print(system.maxsize)


#印出模組的搜尋路徑
#因為geometry.py這個模組在modules這個folder裡面
#所以要增加一個路徑
import sys
sys.path.append("modules") #在模組搜尋路徑裡面新增自家的路徑的資料夾
print(sys.path)


#import自己建立好的模組geometry
import geometry as g
result=g.distance(5,3,2,4)
subtotal=g.slope(5,2,1,8)
print(result)
print(subtotal)
print(g.slope(1,3,4,5))

