import pandas as pd
import numpy as np

# 1. Simulating a messy dataset (Normally, you would use pd.read_csv('file.csv'))
# Notice the np.nan - this represents our missing, broken data!
raw_data = {
    "Customer_Name": ["Alice","Bob","Charlie","Rukum","Gunja"],
    "Age": [25,np.nan,26,25,18],
    "Support_Ticket": ["Login Issue","Billing Error","Login Issue","Refund","Billing Error"]
}

# 2. Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(raw_data)

print("---- Messy Raw Data ----")
print(df)

# 3. Data Cleaning: Let's fill the missing Age with the average age 
# First, calculate the average (mean) of the Age column
average_age = df["Age"].mean()

# Now fill the NaN values with that average 
df["Age"] = df["Age"].fillna(int(average_age))

print("\n---- Cleaned Data Ready for AI ----")
print(df)

