# Project-file-ip
import pandas as pd
import matplotlib.pyplot as plt
import os

# File name to store data
FILE_NAME = "car_sales.csv"

# Function to add new data to the dataset
def add_and_save_data(new_data):
    """ Appends new data to an existing dataset and saves it.
        If the dataset does not exist, it creates a new one.
        Args: new_data (dict): Dictionary of new data to add.
    """
    new_df = pd.DataFrame(new_data)
    if os.path.exists(FILE_NAME):
        old_df = pd.read_csv(FILE_NAME)
        combined_df = pd.concat([old_df, new_df], ignore_index=True)
    else:
        combined_df = new_df
    combined_df.to_csv(FILE_NAME, index=False)
    print("✅ Data has been successfully saved!")

# Function to input new data interactively
def input_new_data():
    """Takes input from the user for new car sales data."""
    new_data = {"Car_Brand": [], "Model": [], "Year": [], "Price": [], "Units_Sold": []}
    print("\n🆕 Enter new car sales data. Type 'done' at any time to stop.")
    
    while True:
        brand = input("Enter Car Brand (or 'done' to finish): ").strip()
        if brand.lower() == "done":
            break
        model = input("Enter Model: ").strip()
        try:
            year = int(input("Enter Year: ").strip())
            price = float(input("Enter Price: ").strip())
            units_sold = int(input("Enter Units Sold: ").strip())
        except ValueError:
            print("❌ Invalid input. Please enter valid numerical values for Year, Price, and Units Sold.")
            continue
        
        new_data["Car_Brand"].append(brand)
        new_data["Model"].append(model)
        new_data["Year"].append(year)
        new_data["Price"].append(price)
        new_data["Units_Sold"].append(units_sold)

    if new_data["Car_Brand"]:
        add_and_save_data(new_data)
    else:
        print("⚠ No data entered.")

# Function to view the dataset
def view_data():
    """Displays the current dataset."""
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        print("\n📊 Current Dataset:")
        print(df)
    else:
        print("⚠ No dataset found. Please add data first.")

# Function to analyze the dataset
def analyze_data():
    """Analyzes the dataset and displays insights."""
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
        print("\n📈 Analysis Results:")
        print("Total Units Sold by Brand:")
        print(df.groupby("Car_Brand")["Units_Sold"].sum())
        print("\nAverage Car Price by Brand:")
        print(df.groupby("Car_Brand")["Price"].mean())
    else:
        print("⚠ No dataset found. Please add data first.")

# Function to visualize data
def visualize_data():
    """Creates visualizations based on the dataset."""
    if os.path.exists(FILE_NAME):
        df = pd.read_csv(FILE_NAME)
       
Total Units Sold by Brand
        brand_sales = df.groupby("Car_Brand")["Units_Sold"].sum()
        plt.figure(figsize=(8, 5))
        brand_sales.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Total Units Sold by Car Brand")
        plt.xlabel("Car Brand")
        plt.ylabel("Units Sold")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

Average Car Price by Brand
        brand_avg_price = df.groupby("Car_Brand")["Price"].mean()
        plt.figure(figsize=(8, 5))
        brand_avg_price.plot(kind="barh", color="orange", edgecolor="black")
        plt.title("Average Car Price by Brand")
        plt.xlabel("Average Price ($)")
        plt.ylabel("Car Brand")
        plt.tight_layout()
        plt.show()

Units Sold Over Years
        yearly_sales = df.groupby("Year")["Units_Sold"].sum()
        plt.figure(figsize=(8, 5))
        yearly_sales.plot(kind="line", marker="o", linestyle="--", color="green")
        plt.title("Units Sold Over Years")
        plt.xlabel("Year")
        plt.ylabel("Units Sold")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("⚠ No dataset found. Please add data first.")

# Main menu for the software
def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n🚗 Car Sales Analysis Software")
        print("1. Add New Data")
        print("2. View Dataset")
        print("3. Analyze Data")
        print("4. Visualize Data")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

  if choice == "1":
            input_new_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            analyze_data()
        elif choice == "4":
            visualize_data()
        elif choice == "5":
            print("👋 Thank you for using the software. Goodbye! ")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

# Run the software
if __name__ == "__main__":
    main_menu()
