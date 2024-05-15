import pandas as pd

# Useful functions
# df.sort_values(by='Sales', ascending=False)
# df.groupby('Region')['Sales'].mean()
# df2 = pd.concat([df, df])
# df['Product'].str.lower()
# df['Product'].str.contains('A')
# df['Cumulative_Sales'] = df['Sales'].cumsum()
# df['Rolling_Mean'] = df['Sales'].rolling(window=2).mean()
# Identify and replace outliers
# import numpy as np
# upper_bound = df['Sales'].mean() + 2 * df['Sales'].std()
# mask, action True, action False
# df['Sales'] = np.where(df['Sales'] > upper_bound, df['Sales'].median(), df['Sales'])
# df['Sales'].plot(kind='line')  # 'bar'
# bank_data['default'].map({'no':0,'yes':1,'unknown':0})


df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})

df2 = df.copy()
df2 = df2.drop_duplicates(subset='brand')
print(df2)

# df2['rating'] = df.groupby('brand')['rating'].mean()
for brand in df2['brand']:
    df2.rating[df2.brand == brand] = df[df['brand'] == brand]['rating'].mean()
ax1 = df2['rating'].plot(kind='bar')
import matplotlib.pyplot as plt
plt.xlabel('Brands', fontsize=20)
plt.show()
print(df2)
