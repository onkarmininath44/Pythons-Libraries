import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df=pd.read_csv("C:/Users/onkar devkar/Downloads/Diwali Sales Data.csv",encoding='unicode_escape')
#drop unnecessary columns/blank columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)
df.isna().sum()
df.dropna(inplace=True)
df.isna().sum()
df.info()
df['Amount']=df['Amount'].astype('int')
df.rename(columns={'Marital_Status':'Shadi'},inplace=True)
#ploting a bar chart for gender and it's count
a=sb.countplot(x='Gender',data=df)
for bars in a.containers:
    a.bar_label(bars)
#plot the bar chart for gender vs amount.
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sb.barplot(x='Gender',y='Amount',data=sales_gen)
'''from the above analysis we can see that most of buyers are females and even the purchasing power of females are greater than the male.'''
## Age analysis
a=sb.countplot(data=df,x='Age Group',hue='Gender')
for bars in a.containers:
    a.bar_labels(bars)
#Total amount vs Age_Group
sales=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by="Amount",ascending=False)
sb.barplot(x="Age Group",y="Amount",data=sales)
'''from the above Graphs we can say that most of the buyers are age_group between 26-35 years and it is the females.'''
#Total number of orders from the top 10 states
sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by="Orders",ascending=False).head(10)
sb.set(rc={'figure.figsize':(15,5)})
sb.barplot(x="State",y="Orders",data=sales_state)
'''from the above Analysis we can say that most of the orders and total sales/amount are from the UP,Maharashtra and Karnataka respectively'''
''' 1)most of buyers are females and even the purchasing power of females are greater than the male.
    2)most of the orders and total sales/amount are from the UP,Maharashtra and Karnataka respectively
    3)most of the buyers are age_group between 26-35 years and it is the females.'''
