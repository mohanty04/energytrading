import pandas as pd
from datetime import datetime

df = pd.read_csv("orderlist.csv")

print(df)
df_salers = df[df['ordertype'] == 'S']

df_buyers = df[df['ordertype'] == 'B']


df_salers_sort = df_salers.sort_values(['price', 'qty', 'orderid'], ascending=[False, True, True]).to_records(index=False)
print("Saler List:", df_salers_sort)

df_buyers_sort = df_buyers.sort_values(['price', 'qty', 'orderid'], ascending=[False, True, True]).to_records(index=False)
print("Buyer List:", df_buyers_sort)

# iterate through buyer list
cntserial = int(datetime.now().strftime("%Y%m%d%H%M%S") + '100')
cnt = 0
sel_ind = 0
cnt_list = []
for saler in df_salers_sort:
    buy_ind = 0
    for buyer in df_buyers_sort:
        if saler[2] <= buyer[2] and saler[3] >= buyer[3] and saler[5] == 'O' and buyer[5] == 'O':
            cntserial = cntserial + 1
            cnt_list.insert(cnt,(cntserial, saler[4], buyer[4], buyer[2], buyer[3])) ### Need to fix how to create a tuple or list...
            df_buyers_sort[buy_ind][5] = 'C'
            df_salers_sort[sel_ind][5] = 'C'


            cnt = cnt + 1
            break
        buy_ind = buy_ind + 1
    sel_ind = sel_ind + 1
print("Total Contracts : ", cnt)
print("Contracts:", cnt_list)




#for index, buyer in df_buyers_sort.iterrows():     #iterate through the buyer list
    #for index, saler in df_salers_sort:  #iterate through the buyer list
        #if buyer['price'] >= saler['price'] and buyer['qty'] <= saler['qty']: #if buyprice less than eqaul to sale price (match the price and qty)
            # Buyer and Saler price and Quantity matched : Contract will be created
            #cntserial = cntserial + 1
           # cntid = 'CN' + cntserial
            # create contract list with new contractid buyerid, sellerid and other details (Contract status as "E")
            #df_contract = [cntid, saler['userid'], buyer['userid'], buyer['price'], buyer['qty'],'E', datetime.now().strftime("%Y%m%d%H%M%S") ]
            #print(df_contract)
            #update the buyer with contract id and updated status
            #update seller with contract id and updated status ("O" - Open, "C" - Contracted)
        #else break the inner loop
    ##
#print contractlist
















































