
import pandas as pd
from datetime import datetime

df = pd.read_csv("orderlist.csv")
print(df)

df_buyer=df[df["ordertype"]=="B"]
print(df_buyer)

df_saler=df[df["ordertype"]=="S"]
print(df_saler)


df_buyer_order=df_buyer.sort_values(["qty","price","orderid"],ascending= [True,False,True]).to_records(index=False)
print("BUYER order",":",df_buyer_order)

df_saler_order=df_saler.sort_values(["qty","price","orderid"],ascending= [True,False,True]).to_records(index=False)
print("SALER order",":",df_saler_order)

Contract=[]
for buyer in df_buyer_order:
    print("Available Saler", df_saler_order)
    for saler, row in df_saler_order:
        if saler[2]<=buyer[2] and saler [3]>= buyer[3] and saler[5]=='O'and buyer[5]=='O':
           Contract.append((saler[4], buyer[4], buyer[2], buyer[3]))
           df_saler_order[row][5] =='C'
           break
print("Contract_List",':',Contract)
print("Total_Contract",":",len(Contract))







