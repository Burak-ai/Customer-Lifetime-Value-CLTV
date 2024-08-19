import pandas as pd 
data = {
    "customer_id": [5, 6, 8, 1, 4, 7],
    
    "order_date": ['2023-01-01', '2023-02-15', '2023-03-10', 
                   '2023-01-15', '2023-04-05', '2023-03-20'],
    
    "order_value": [100, 150, 80, 200, 120, 190]              
}

df = pd.DataFrame(data)

# Average order value 
aov = df["order_value"].mean()

df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.month
purchase_frequency = df.groupby("customer_id")["month"].nunique().mean()

churn_rate = 0.6
profit_margin = 1.4

cltv = (aov * purchase_frequency) / churn_rate * profit_margin

print("CLTV:", cltv)