import pandas as pd

providers = pd.read_csv("Data/providers_data.csv")
receivers = pd.read_csv("Data/receivers_data.csv")
food = pd.read_csv("Data/food_listings_data.csv")
claims = pd.read_csv("Data/claims_data.csv")

print("\n--- PROVIDERS DATA ---")
print(providers.head())
print(providers.info())

print("\n--- RECEIVERS DATA ---")
print(receivers.head())
print(receivers.info())

print("\n--- FOOD LISTINGS DATA ---")
print(food.head())
print(food.info())

print("\n--- CLAIMS DATA ---")
print(claims.head())
print(claims.info())

print("\nAll files loaded successfully!")