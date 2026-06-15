import pandas as pd
import matplotlib.pyplot as plt
import os

# Create screenshots folder if it does not exist
os.makedirs("Screenshots", exist_ok=True)

# Load cleaned datasets
providers = pd.read_csv("Data/cleaned_providers.csv")
receivers = pd.read_csv("Data/cleaned_receivers.csv")
food = pd.read_csv("Data/cleaned_food_listings.csv")
claims = pd.read_csv("Data/cleaned_claims.csv")

# 1. Food listings by location
location_counts = food["Location"].value_counts().head(10)
plt.figure(figsize=(10, 6))
location_counts.plot(kind="bar")
plt.title("Top 10 Locations by Food Listings")
plt.xlabel("Location")
plt.ylabel("Number of Food Listings")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Screenshots/eda_top_locations_food_listings.png")
plt.close()

# 2. Food type distribution
food_type_counts = food["Food_Type"].value_counts()
plt.figure(figsize=(8, 6))
food_type_counts.plot(kind="bar")
plt.title("Food Type Distribution")
plt.xlabel("Food Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Screenshots/eda_food_type_distribution.png")
plt.close()

# 3. Meal type distribution
meal_type_counts = food["Meal_Type"].value_counts()
plt.figure(figsize=(8, 6))
meal_type_counts.plot(kind="bar")
plt.title("Meal Type Distribution")
plt.xlabel("Meal Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Screenshots/eda_meal_type_distribution.png")
plt.close()

# 4. Claim status distribution
claim_status_counts = claims["Status"].value_counts()
plt.figure(figsize=(8, 6))
claim_status_counts.plot(kind="bar")
plt.title("Claim Status Distribution")
plt.xlabel("Claim Status")
plt.ylabel("Number of Claims")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Screenshots/eda_claim_status_distribution.png")
plt.close()

# 5. Provider type contribution by quantity
provider_type_quantity = food.groupby("Provider_Type")["Quantity"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
provider_type_quantity.plot(kind="bar")
plt.title("Total Food Quantity by Provider Type")
plt.xlabel("Provider Type")
plt.ylabel("Total Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Screenshots/eda_provider_type_quantity.png")
plt.close()

print("EDA completed successfully!")
print("Charts saved inside the Screenshots folder.")