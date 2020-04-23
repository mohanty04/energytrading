
# Import pandas
import pandas as pd
#import matplotlib.pyplot as plt


# Assign url of file: url
url_prefix="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-"
url_suffix="-2020.csv"

#url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-16-2020.csv"


india=pd.DataFrame()
for i in range(7,22):
    filename = url_prefix + str(i).zfill(2) + url_suffix
    #print(filename)
    # Save file locally
    # Read file into a DataFrame and print its head
    df = pd.read_csv(filename)
    df1= df.set_index('Country_Region')
    #print(df1.head())


    df_ind = df1.loc['India']
    df_ita = df1.loc['Italy']
    #print(df_ind)
    #data_date = "2020-04-"+ str(i).zfill(2)
    #df_ind['Last_Update'] = data_date
    #df.set_index('Update_Date')
    india= india.append(df_ind)
#print(india)

india=india.drop(['Admin2','Combined_Key','FIPS','Lat','Long_','Province_State'],axis=1)
#print(india)

Ind_data=india.reset_index().set_index('Last_Update')
Ind_data= Ind_data.drop(['index'], axis=1)
print(Ind_data)



















