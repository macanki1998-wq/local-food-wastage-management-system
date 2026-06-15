import pandas as pd

# Load datasets
providers = pd.read_csv("Data/providers_data.csv")
receivers = pd.read_csv("Data/receivers_data.csv")
food = pd.read_csv("Data/food_listings_data.csv")
claims = pd.read_csv("Data/claims_data.csv")

# Remove duplicate rows
providers = providers.drop_duplicates()
receivers = receivers.drop_duplicates()
food = food.drop_duplicates()
claims = claims.drop_duplicates()

# Remove extra spaces from text columns
for df in [providers, receivers, food, claims]:
    text_columns = df.select_dtypes(include="object").columns
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()

# Convert date columns
food["Expiry_Date"] = pd.to_datetime(food["Expiry_Date"], errors="coerce")
claims["Timestamp"] = pd.to_datetime(claims["Timestamp"], errors="coerce")

# Standardize status values
claims["Status"] = claims["Status"].str.title()

# Save cleaned files
providers.to_csv("Data/cleaned_providers.csv", index=False)
receivers.to_csv("Data/cleaned_receivers.csv", index=False)
food.to_csv("Data/cleaned_food_listings.csv", index=False)
claims.to_csv("Data/cleaned_claims.csv", index=False)

print("Data cleaning completed successfully!")
print("Cleaned files saved inside the Data folder.")