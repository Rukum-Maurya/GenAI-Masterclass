import pandas as pd
import numpy as np



def process_sales_data(file_path):
    try:
        # Step 2: Load the data
        print("Attempting to load {file_path}....")

        df = pd.read_csv(file_path)

        print("Data loaded successfully!")

       # Step 3: Clean the missing Data
        df = df.dropna(subset=["Customer_Name"])

        average_price = df["Item_Price"].mean()
        df["Item_Price"] = df["Item_Price"].fillna(average_price)
 
        df["Quantity"] = df["Quantity"].fillna(1)

        # Step 4: Filter the Data
        df = df[df["Status"] == "Completed"]

        # Step 5: Calculate Total Revenue
        df["Total_Revenue"] = df["Item_Price"]*df["Quantity"]


        # Step 6: Export the Clean Data
        df.to_csv("clean_sales.csv",index=False)
        print("Success! Clean data saved to 'clean_sales.csv'")

        

    # except FileNotFoundError:
    #     print(f"Error: The file '{file_path}' was not found. Please check the folder.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the pipeline
process_sales_data("salees.csv")


      


    
   



