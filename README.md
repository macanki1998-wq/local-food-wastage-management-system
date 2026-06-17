# Local Food Wastage Management System

## Project Overview

The Local Food Wastage Management System is a data-driven application designed to reduce food wastage by connecting surplus food providers with receivers such as NGOs, community centers, and individuals in need.

Many restaurants, grocery stores, supermarkets, and catering services often have extra food that may go unused. At the same time, many people and organizations require food support. This project creates a structured platform where surplus food can be listed, searched, filtered, claimed, and managed efficiently.

The project uses Python for data processing, MySQL for database management, SQL for analysis, and Streamlit for building an interactive web application.

---

## Problem Statement

Food wastage is a major issue in many cities. Surplus food from restaurants, stores, and individuals is often discarded, while many people face food insecurity. There is a need for a simple system that can connect food providers with receivers and make food redistribution easier.

This project aims to build a Local Food Wastage Management System where food providers can list surplus food, receivers can view and claim available food, and administrators can analyze food donation and claim trends using SQL and visual dashboards.

---

## Objectives

The main objectives of this project are:

* To create a database for storing food provider, receiver, food listing, and claim details.
* To clean and prepare the provided datasets using Python.
* To import cleaned datasets into a MySQL database.
* To perform SQL analysis using 15 queries.
* To identify food wastage and claim trends based on location, food type, meal type, provider type, and claim status.
* To build an interactive Streamlit application.
* To allow users to filter available food listings.
* To display provider contact details for coordination.
* To implement CRUD operations for food listings.
* To display EDA charts and SQL query outputs in the application.

---

## Tools and Technologies Used

* Python
* Pandas
* MySQL
* SQL
* Streamlit
* Matplotlib
* VS Code
* MySQL Workbench

---

## Dataset Description

The project uses four datasets:

### 1. Providers Dataset

This dataset contains details of food providers.

Columns:

* Provider_ID
* Name
* Type
* Address
* City
* Contact

### 2. Receivers Dataset

This dataset contains details of food receivers.

Columns:

* Receiver_ID
* Name
* Type
* City
* Contact

### 3. Food Listings Dataset

This dataset contains details of available surplus food.

Columns:

* Food_ID
* Food_Name
* Quantity
* Expiry_Date
* Provider_ID
* Provider_Type
* Location
* Food_Type
* Meal_Type

### 4. Claims Dataset

This dataset tracks claims made by receivers.

Columns:

* Claim_ID
* Food_ID
* Receiver_ID
* Status
* Timestamp

---

## Project Workflow

The project was completed using the following steps:

1. Created the project folder structure.
2. Added the original CSV files.
3. Checked the datasets using Python.
4. Cleaned the data using Python and Pandas.
5. Saved cleaned CSV files.
6. Created a MySQL database named `food_wastage_db`.
7. Created four tables: providers, receivers, food_listings, and claims.
8. Imported cleaned CSV files into MySQL.
9. Ran 15 SQL queries for analysis.
10. Created EDA charts using Python and Matplotlib.
11. Built a Streamlit web application.
12. Added filters for location, provider type, food type, and meal type.
13. Added provider contact details.
14. Added SQL query outputs inside the Streamlit app.
15. Added EDA visualizations inside the Streamlit app.
16. Implemented CRUD operations for food listings.

---

## SQL Analysis Performed

The project includes 15 SQL queries to answer key business questions:

1. How many food providers are there in each city?
2. How many receivers are there in each city?
3. Which type of food provider contributes the most food?
4. What is the contact information of food providers in a specific city?
5. Which receivers have claimed the most food?
6. What is the total quantity of food available?
7. Which city has the highest number of food listings?
8. What are the most commonly available food types?
9. How many food claims have been made for each food item?
10. Which provider has the highest number of successful claims?
11. What percentage of claims are completed, pending, and cancelled?
12. What is the average quantity of food claimed per receiver?
13. Which meal type is claimed the most?
14. What is the total quantity of food donated by each provider?
15. Which food items are near expiry?

---

## Business Questions and Insights

This project answers the following important business questions using SQL analysis:

### 1. How many food providers are there in each city?

This helps identify cities with a higher number of food providers. It is useful for understanding where food supply is stronger.

### 2. How many receivers are there in each city?

This helps identify locations where receivers such as NGOs, shelters, charities, and individuals are present. It supports better planning of food distribution.

### 3. Which type of food provider contributes the most food?

This query compares provider types such as restaurants, supermarkets, grocery stores, and catering services. It helps identify which provider category contributes the highest food quantity.

### 4. What is the contact information of food providers in a specific city?

This helps receivers or NGOs directly contact food providers in a selected city for food collection and coordination.

### 5. Which receivers have claimed the most food?

This identifies the most active receivers in the system. It helps understand which organizations or individuals are using the platform frequently.

### 6. What is the total quantity of food available?

This gives the total available surplus food quantity in the system. It provides an overall view of food availability.

### 7. Which location has the highest number of food listings?

This helps identify areas where surplus food is most available. These locations can be prioritized for food collection and redistribution.

### 8. What are the most commonly available food types?

This shows whether vegetarian, non-vegetarian, or vegan food is more commonly available. It helps receivers search based on food preference or requirement.

### 9. How many food claims have been made for each food item?

This shows which food items are claimed more frequently. It helps understand demand for different food items.

### 10. Which provider has the highest number of successful food claims?

This identifies providers whose food listings are successfully claimed more often. It helps recognize active and reliable food contributors.

### 11. What percentage of claims are completed, pending, and cancelled?

This helps evaluate the claim process. A higher completed percentage indicates better food redistribution efficiency.

### 12. What is the average quantity of food claimed per receiver?

This shows how much food receivers claim on average. It helps identify receivers with higher food requirements.

### 13. Which meal type is claimed the most?

This identifies whether breakfast, lunch, dinner, or snacks are claimed most frequently. It helps understand demand based on meal type.

### 14. What is the total quantity of food donated by each provider?

This helps identify top food donors based on total food quantity contributed.

### 15. Which food items are near expiry?

This helps identify food items that should be distributed quickly to avoid wastage.

---

## Key Insights

Based on the SQL analysis and EDA visualizations, the project provides the following insights:

- Food availability can be analyzed location-wise using provider and food listing data.
- Provider types such as restaurants, supermarkets, grocery stores, and catering services contribute differently to the total food quantity.
- Claim status analysis helps understand how many claims are completed, pending, or cancelled.
- Food type and meal type analysis helps understand the kind of food most commonly available and claimed.
- Near-expiry food analysis helps prioritize urgent redistribution.
- Receiver claim analysis helps identify active receivers and organizations.
- The Streamlit application makes the system interactive by allowing users to filter data, view provider contacts, analyze SQL outputs, view charts, and manage food listings using CRUD operations.
---

## EDA Visualizations

The following visualizations were created:

* Top 10 locations by food listings
* Food type distribution
* Meal type distribution
* Claim status distribution
* Provider type contribution by quantity

These charts help understand food availability, food demand, provider contribution, and claim patterns.

---

## Streamlit Application Features

The Streamlit app includes:

* Project overview dashboard
* Total providers, receivers, food listings, and claims
* Food listing filters
* Provider contact details
* Raw data tables
* SQL query analysis dropdown
* EDA chart dropdown
* CRUD operations for food listings

---

## CRUD Operations

The application supports CRUD operations for food listings:

### Create

Users can add a new food listing by entering food details such as food name, quantity, expiry date, provider ID, provider type, location, food type, and meal type.

### Read

Users can view current food listings from the MySQL database.

### Update

Users can update the quantity of an existing food listing using Food ID.

### Delete

Users can delete a food listing using Food ID.

---

## How to Run the Project

### Step 1: Install required libraries

```bash
pip3 install pandas matplotlib streamlit mysql-connector-python
```

### Step 2: Run the data checking file

```bash
python3 data_check.py
```

### Step 3: Run the data cleaning file

```bash
python3 data_cleaning.py
```

### Step 4: Run the EDA file

```bash
python3 SQL/eda_analysis.py
```

### Step 5: Run the Streamlit app

```bash
python3 -m streamlit run App/app.py
```

Then open the app in the browser:

```text
http://localhost:8501
```

---

## Project Folder Structure

```text
Local Food Wastage Project
├── App
│   └── app.py
├── Data
│   ├── providers_data.csv
│   ├── receivers_data.csv
│   ├── food_listings_data.csv
│   ├── claims_data.csv
│   ├── cleaned_providers.csv
│   ├── cleaned_receivers.csv
│   ├── cleaned_food_listings.csv
│   └── cleaned_claims.csv
├── SQL
│   ├── analysis_queries.sql
│   └── eda_analysis.py
├── Screenshots
├── data_check.py
├── data_cleaning.py
├── requirements.txt
└── README.md
```

---

## Conclusion

The Local Food Wastage Management System successfully demonstrates how technology can help reduce food wastage by connecting surplus food providers with receivers. The project combines data cleaning, SQL analysis, EDA, and Streamlit application development. It provides useful insights into food availability, provider contribution, claim status, and food distribution trends.

The application can be further improved by adding user login, real-time geolocation, claim request tracking, and automated expiry alerts.

---

## Future Scope

* Add login system for providers and receivers.
* Add real-time location-based food search.
* Add automated alerts for near-expiry food.
* Add claim approval workflow.
* Add dashboard for NGOs and administrators.
* Deploy the app online for public access.
* Add email or SMS notifications.
* Improve UI design and mobile responsiveness.
