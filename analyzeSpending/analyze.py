import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("~/Documents/python/analyzeSpending/latestCsvStatement.csv", parse_dates=["Date"])

print(data.head())
print(data.info())
print(data.describe())

data["Total Spending"] = data["Debit"] + data["Credit Amount"]

spending_over_time = data.groupby("Date")["Total Spending"].sum().reset_index()
print(spending_over_time)


def extract_category(narration):
    parts = narration.split("-")
    return parts[1].strip() if len(parts) >= 2 else "Other"

data["Category"] = data["Narration"].apply(extract_category)
spending_by_category = data.groupby("Category")["Total Spending"].sum().reset_index()
print(spending_by_category)

data["Vendor"] = data["Narration"].str.extract(r'UPI-(.*?)-')
data["Payment To"] = data["Narration"].str.extract(r'-(.*?)-')
data["Location"] = data["Narration"].str.extract(r'@(.*)$')

def categorize_transaction(narration):
    if "FOOD" in narration.upper():
        return "Food"
    if "SUPERMARKET" in narration.upper():
        return "Groceries"
    elif "SHOPPING" in narration.upper():
        return "Shopping"
    elif "TRAVEL" or "UBER" in narration.upper():
        return "Travel"
    elif "PETROL" in narration.upper():
        return "Petrol"
    else:
        return "Other"

data["Transaction_Category"] = data["Narration"].apply(categorize_transaction)




data["Is_UPI"] = data["Narration"].str.contains("UPI", case=False)
data["Is_Credit_Card"] = data["Narration"].str.contains("CREDIT CARD", case=False)
print(data[["Date", "Narration", "Vendor", "Payment To", "Location", "Transaction_Category", "Is_UPI", "Is_Credit_Card"]])
