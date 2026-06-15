import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(
    page_title="Local Food Wastage Management System",
    layout="wide"
)

st.title("Local Food Wastage Management System")

st.write("""
This application helps connect surplus food providers with receivers such as NGOs, 
community centers, and individuals in need.
""")

# Load datasets
providers = pd.read_csv("Data/cleaned_providers.csv")
receivers = pd.read_csv("Data/cleaned_receivers.csv")
food = pd.read_csv("Data/cleaned_food_listings.csv")
claims = pd.read_csv("Data/cleaned_claims.csv")
def run_query(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MYSQL_PASSWORD",
        database="food_wastage_db"
    )
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Project overview
st.subheader("Project Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Providers", len(providers))
col2.metric("Total Receivers", len(receivers))
col3.metric("Food Listings", len(food))
col4.metric("Total Claims", len(claims))

st.markdown("---")

# Filters section
st.subheader("Filter Available Food Listings")

col1, col2, col3, col4 = st.columns(4)

with col1:
    selected_location = st.selectbox(
        "Select Location",
        ["All"] + sorted(food["Location"].unique().tolist())
    )

with col2:
    selected_provider_type = st.selectbox(
        "Select Provider Type",
        ["All"] + sorted(food["Provider_Type"].unique().tolist())
    )

with col3:
    selected_food_type = st.selectbox(
        "Select Food Type",
        ["All"] + sorted(food["Food_Type"].unique().tolist())
    )

with col4:
    selected_meal_type = st.selectbox(
        "Select Meal Type",
        ["All"] + sorted(food["Meal_Type"].unique().tolist())
    )

filtered_food = food.copy()

if selected_location != "All":
    filtered_food = filtered_food[filtered_food["Location"] == selected_location]

if selected_provider_type != "All":
    filtered_food = filtered_food[filtered_food["Provider_Type"] == selected_provider_type]

if selected_food_type != "All":
    filtered_food = filtered_food[filtered_food["Food_Type"] == selected_food_type]

if selected_meal_type != "All":
    filtered_food = filtered_food[filtered_food["Meal_Type"] == selected_meal_type]

st.write("Filtered Food Listings:")
st.dataframe(filtered_food)

st.markdown("---")

# Provider contact details
st.subheader("Provider Contact Details")

provider_contacts = pd.merge(
    filtered_food,
    providers,
    on="Provider_ID",
    how="left",
    suffixes=("_food", "_provider")
)

provider_contacts = provider_contacts[
    [
        "Food_ID",
        "Food_Name",
        "Quantity",
        "Expiry_Date",
        "Location",
        "Food_Type",
        "Meal_Type",
        "Name",
        "Type",
        "Address",
        "City",
        "Contact"
    ]
]

st.dataframe(provider_contacts)

st.markdown("---")

# Raw data sections
st.subheader("Food Providers")
st.dataframe(providers)

st.subheader("Receivers")
st.dataframe(receivers)

st.subheader("Claims Data")
st.dataframe(claims)
st.markdown("---")
st.subheader("SQL Query Analysis")

query_options = {
    "1. Providers count by city": """
        SELECT City, COUNT(*) AS total_providers
        FROM providers
        GROUP BY City
        ORDER BY total_providers DESC;
    """,

    "2. Receivers count by city": """
        SELECT City, COUNT(*) AS total_receivers
        FROM receivers
        GROUP BY City
        ORDER BY total_receivers DESC;
    """,

    "3. Provider type contributing most food": """
        SELECT Provider_Type, SUM(Quantity) AS total_food_quantity
        FROM food_listings
        GROUP BY Provider_Type
        ORDER BY total_food_quantity DESC;
    """,

    "4. Provider contact information by city": """
        SELECT Name, Type, Address, City, Contact
        FROM providers
        WHERE City = 'New Carol';
    """,

    "5. Receivers who claimed the most food": """
        SELECT r.Receiver_ID, r.Name, r.Type, r.City,
               COUNT(c.Claim_ID) AS total_claims
        FROM receivers r
        JOIN claims c ON r.Receiver_ID = c.Receiver_ID
        GROUP BY r.Receiver_ID, r.Name, r.Type, r.City
        ORDER BY total_claims DESC;
    """,

    "6. Total quantity of food available": """
        SELECT SUM(Quantity) AS total_food_available
        FROM food_listings;
    """,

    "7. City with highest food listings": """
        SELECT Location, COUNT(*) AS total_food_listings
        FROM food_listings
        GROUP BY Location
        ORDER BY total_food_listings DESC;
    """,

    "8. Most commonly available food types": """
        SELECT Food_Type, COUNT(*) AS total_count
        FROM food_listings
        GROUP BY Food_Type
        ORDER BY total_count DESC;
    """,

    "9. Claims made for each food item": """
        SELECT f.Food_ID, f.Food_Name,
               COUNT(c.Claim_ID) AS total_claims
        FROM food_listings f
        LEFT JOIN claims c ON f.Food_ID = c.Food_ID
        GROUP BY f.Food_ID, f.Food_Name
        ORDER BY total_claims DESC;
    """,

    "10. Provider with highest successful claims": """
        SELECT p.Provider_ID, p.Name AS provider_name, p.Type AS provider_type,
               p.City, COUNT(c.Claim_ID) AS successful_claims
        FROM providers p
        JOIN food_listings f ON p.Provider_ID = f.Provider_ID
        JOIN claims c ON f.Food_ID = c.Food_ID
        WHERE c.Status = 'Completed'
        GROUP BY p.Provider_ID, p.Name, p.Type, p.City
        ORDER BY successful_claims DESC;
    """,

    "11. Claim status percentage": """
        SELECT Status,
               COUNT(*) AS total_claims,
               ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims)), 2) AS percentage
        FROM claims
        GROUP BY Status
        ORDER BY total_claims DESC;
    """,

    "12. Average quantity claimed per receiver": """
        SELECT r.Receiver_ID, r.Name AS receiver_name, r.Type AS receiver_type,
               r.City, ROUND(AVG(f.Quantity), 2) AS average_quantity_claimed
        FROM receivers r
        JOIN claims c ON r.Receiver_ID = c.Receiver_ID
        JOIN food_listings f ON c.Food_ID = f.Food_ID
        GROUP BY r.Receiver_ID, r.Name, r.Type, r.City
        ORDER BY average_quantity_claimed DESC;
    """,

    "13. Most claimed meal type": """
        SELECT f.Meal_Type, COUNT(c.Claim_ID) AS total_claims
        FROM food_listings f
        JOIN claims c ON f.Food_ID = c.Food_ID
        GROUP BY f.Meal_Type
        ORDER BY total_claims DESC;
    """,

    "14. Total quantity donated by each provider": """
        SELECT p.Provider_ID, p.Name AS provider_name, p.Type AS provider_type,
               p.City, SUM(f.Quantity) AS total_quantity_donated
        FROM providers p
        JOIN food_listings f ON p.Provider_ID = f.Provider_ID
        GROUP BY p.Provider_ID, p.Name, p.Type, p.City
        ORDER BY total_quantity_donated DESC;
    """,

    "15. Food items near expiry": """
        SELECT Food_ID, Food_Name, Quantity, Expiry_Date, Location, Food_Type, Meal_Type
        FROM food_listings
        WHERE Expiry_Date <= DATE_ADD(CURDATE(), INTERVAL 7 DAY)
        ORDER BY Expiry_Date ASC;
    """
}

selected_query = st.selectbox("Select SQL query to view output", list(query_options.keys()))

result = run_query(query_options[selected_query])

st.dataframe(result)
st.markdown("---")
st.subheader("EDA Visualizations")

chart_option = st.selectbox(
    "Select EDA chart to view",
    [
        "Top Locations by Food Listings",
        "Food Type Distribution",
        "Meal Type Distribution",
        "Claim Status Distribution",
        "Provider Type Contribution"
    ]
)

if chart_option == "Top Locations by Food Listings":
    st.image("Screenshots/eda_top_locations_food_listings.png")

elif chart_option == "Food Type Distribution":
    st.image("Screenshots/eda_food_type_distribution.png")

elif chart_option == "Meal Type Distribution":
    st.image("Screenshots/eda_meal_type_distribution.png")

elif chart_option == "Claim Status Distribution":
    st.image("Screenshots/eda_claim_status_distribution.png")

elif chart_option == "Provider Type Contribution":
    st.image("Screenshots/eda_provider_type_quantity.png")
    st.markdown("---")
st.subheader("CRUD Operations for Food Listings")

crud_option = st.selectbox(
    "Select CRUD operation",
    ["Add New Food Listing", "Update Food Quantity", "Delete Food Listing", "View Food Listings"]
)

# Function for insert, update, delete
def execute_query(query, values=None):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MYSQL_PASSWORD",
        database="food_wastage_db"
    )
    cursor = conn.cursor()
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


if crud_option == "Add New Food Listing":
    st.write("Add a new surplus food listing")

    food_id = st.number_input("Food ID", min_value=1001, step=1)
    food_name = st.text_input("Food Name")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    expiry_date = st.date_input("Expiry Date")
    provider_id = st.number_input("Provider ID", min_value=1, step=1)
    provider_type = st.selectbox("Provider Type", sorted(food["Provider_Type"].unique().tolist()))
    location = st.text_input("Location")
    food_type = st.selectbox("Food Type", sorted(food["Food_Type"].unique().tolist()))
    meal_type = st.selectbox("Meal Type", sorted(food["Meal_Type"].unique().tolist()))

    if st.button("Add Food Listing"):
        insert_query = """
            INSERT INTO food_listings
            (Food_ID, Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            food_id,
            food_name,
            quantity,
            expiry_date,
            provider_id,
            provider_type,
            location,
            food_type,
            meal_type
        )

        execute_query(insert_query, values)
        st.success("New food listing added successfully!")


elif crud_option == "Update Food Quantity":
    st.write("Update quantity for an existing food listing")

    update_food_id = st.number_input("Enter Food ID to update", min_value=1, step=1)
    new_quantity = st.number_input("Enter new quantity", min_value=1, step=1)

    if st.button("Update Quantity"):
        update_query = """
            UPDATE food_listings
            SET Quantity = %s
            WHERE Food_ID = %s
        """

        values = (new_quantity, update_food_id)

        execute_query(update_query, values)
        st.success("Food quantity updated successfully!")


elif crud_option == "Delete Food Listing":
    st.write("Delete a food listing")

    delete_food_id = st.number_input("Enter Food ID to delete", min_value=1, step=1)

    if st.button("Delete Food Listing"):
        delete_query = """
            DELETE FROM food_listings
            WHERE Food_ID = %s
        """

        values = (delete_food_id,)

        execute_query(delete_query, values)
        st.success("Food listing deleted successfully!")


elif crud_option == "View Food Listings":
    st.write("Current food listings from MySQL database")

    view_query = """
        SELECT *
        FROM food_listings
        ORDER BY Food_ID DESC;
    """

    latest_food_data = run_query(view_query)
    st.dataframe(latest_food_data)