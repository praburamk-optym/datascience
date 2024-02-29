import seaborn as sns
import pandas as pd

df=pd.read_csv('/Users/praburam.krishnamurthy/GL/Mod-1/Automobile.csv')
sns.histplot(data=df,x='price')
