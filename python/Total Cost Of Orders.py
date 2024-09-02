import pandas as pd

df_orders = pd.read_excel(r'E:\\Data_analysis_projects\\Total Cost Of Orders\\dataset\\customers_orders_large_dummy_data.xlsx', sheet_name='Orders')
df_customers = pd.read_excel(r'E:\\Data_analysis_projects\\Total Cost Of Orders\\dataset\\customers_orders_large_dummy_data.xlsx', sheet_name='Customers')

df_merged = pd.merge(df_orders, df_customers, left_on='cust_id', right_on='id')

df_grouped = df_merged.groupby(['id_x','cust_id','first_name']).agg({
    'total_order_cost': 'sum'
}).reset_index()
print(df_grouped)


