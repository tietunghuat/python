#篩選資料
import pandas as pd 
data=pd.Series([30,20,15])
condition=[True,False,True] #篩選資料
filteredData=data[condition]
print(filteredData) #篩選之後的資料，因為20是false,不會被篩選出來
print("------------------------------")
source = pd.Series([30, 20, 15])
condition_source =source>18  # 篩選資料 若大於18顯示
print(condition_source)
filteredData_source = data[condition_source]
print(filteredData_source)

print("------------------------------")
nba = pd.Series(["James","KD","Lillard"])
nba_con=[True,False,True]
filteredData_nba=nba[nba_con]
print(filteredData_nba)
print("------------------------------")
nba = pd.Series(["James", "KD", "Lillard"])
nba_con = nba.str.contains("J") #篩選出只含有J的
filteredData_nba = nba[nba_con]
print(filteredData_nba)
print("------------------------------")

nba_data = pd.DataFrame(
    {"team": ["Lakers", "Nets", "Washington"], "salary": [80000, 70000, 50000]})
nba_money=nba_data["salary"]>=70000
filteredData_money=nba_data[nba_money]
print(filteredData_money)
print("------------------------------")
nba_name=nba_data["team"]=="Lakers"
filteredData_name=nba_data[nba_name]
print(filteredData_name)
