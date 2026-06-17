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

## Business Questions and Actual Insights from SQL Analysis

This project answers the following business questions using SQL analysis on the Local Food Wastage Management System database.

---

### 1. How many food providers are there in each city?

The query shows the number of food providers available city-wise.

**Actual result:**

* New Carol has the highest number of providers with **3 providers**.
* South Christopherborough also has **3 providers**.
* Several cities such as New Amanda, North Kevinhaven, Lake Kyle, North Michelle, West Lauraborough, New Richard, East Melissa, New Daniel, New Lisa, and New John have **2 providers each**.

**Insight:**
New Carol and South Christopherborough have the highest provider presence in the dataset. These cities can be considered stronger food supply locations.

---

### 2. How many receivers are there in each city?

The query shows the number of food receivers available city-wise.

**Actual result:**

* New Christopher has the highest number of receivers with **3 receivers**.
* Other cities such as Spencermouth, Moorechester, Lake Mary, Smithshire, Lake Daniel, Kellybury, Greenton, North Lori, West James, and North Christina have **2 receivers each**.

**Insight:**
New Christopher has the highest receiver concentration. This location may have higher food demand compared to other cities.

---

### 3. Which type of food provider contributes the most food?

The query calculates the total food quantity contributed by each provider type.

**Actual result:**

| Provider Type    | Total Food Quantity |
| ---------------- | ------------------: |
| Restaurant       |                6923 |
| Supermarket      |                6696 |
| Catering Service |                6116 |
| Grocery Store    |                6059 |

**Insight:**
Restaurants contributed the highest quantity of food with **6923 units**, followed by supermarkets with **6696 units**. This shows that restaurants are the strongest contributors in this dataset.

---

### 4. What is the contact information of food providers in a specific city?

The query displays provider details for a selected city.

**Actual result for city: New John**

| Provider Name       | Type        | City     | Contact              |
| ------------------- | ----------- | -------- | -------------------- |
| Smith-Turner        | Supermarket | New John | 001-084-709-0706x311 |
| Moore, Peck and Cox | Supermarket | New John | 001-403-232-7921     |

**Insight:**
The query helps receivers directly access provider contact details for coordination. In New John, both listed providers are supermarkets.

---

### 5. Which receivers have claimed the most food?

The query identifies receivers who made the highest number of claims.

**Actual result:**

| Receiver Name     | Receiver Type | City       | Total Claims |
| ----------------- | ------------- | ---------- | -----------: |
| William Frederick | NGO           | Port Dean  |            5 |
| Scott Hunter      | Individual    | Greenton   |            5 |
| Anthony Garcia    | Individual    | Brownbury  |            5 |
| Matthew Webb      | Charity       | West David |            5 |

**Insight:**
These receivers are the most active claimants in the system, each having made **5 claims**.

---

### 6. What is the total quantity of food available?

The query calculates the total available food quantity from all food listings.

**Actual result:**

* Total food available = **25,794 units**

**Insight:**
The system contains a large amount of surplus food, which can be redistributed to reduce wastage.

---

### 7. Which location has the highest number of food listings?

The query identifies locations with the highest number of listed food items.

**Actual result:**

| Location      | Total Food Listings |
| ------------- | ------------------: |
| New Carol     |                   6 |
| South Kathryn |                   6 |
| Jimmyberg     |                   5 |
| Perezport     |                   5 |
| East Angela   |                   5 |

**Insight:**
New Carol and South Kathryn have the highest number of food listings, with **6 listings each**. These locations have higher food availability.

---

### 8. What are the most commonly available food types?

The query shows the distribution of food types.

**Actual result:**

| Food Type      | Total Count |
| -------------- | ----------: |
| Vegetarian     |         336 |
| Vegan          |         334 |
| Non-Vegetarian |         330 |

**Insight:**
Vegetarian food is the most commonly available food type with **336 listings**, but the distribution is almost balanced among vegetarian, vegan, and non-vegetarian food.

---

### 9. How many food claims have been made for each food item?

The query shows which food items received the highest number of claims.

**Actual result:**

| Food ID | Food Name | Total Claims |
| ------: | --------- | -----------: |
|     463 | Soup      |            5 |
|     486 | Chicken   |            5 |
|     548 | Fish      |            5 |
|      35 | Rice      |            4 |
|      92 | Chicken   |            4 |
|     190 | Salad     |            4 |

**Insight:**
Soup, chicken, and fish were among the most claimed food items, each receiving **5 claims**.

---

### 10. Which provider has the highest number of successful food claims?

The query identifies providers with the highest completed claims.

**Actual result:**

| Provider Name               | Provider Type    | City             | Successful Claims |
| --------------------------- | ---------------- | ---------------- | ----------------: |
| Barry Group                 | Restaurant       | South Kathryn    |                 5 |
| Harper, Blake and Alexander | Catering Service | Devinmouth       |                 4 |
| Miller Inc                  | Grocery Store    | Coleburgh        |                 4 |
| Butler-Richardson           | Grocery Store    | East Heatherport |                 4 |
| Barnes, Castro and Curtis   | Restaurant       | Zimmermanville   |                 4 |

**Insight:**
Barry Group had the highest number of successful claims with **5 completed claims**, making it the top successful provider in the dataset.

---

### 11. What percentage of claims are completed, pending, and cancelled?

The query calculates claim status percentage.

**Actual result:**

| Status    | Total Claims | Percentage |
| --------- | -----------: | ---------: |
| Completed |          339 |     33.90% |
| Cancelled |          336 |     33.60% |
| Pending   |          325 |     32.50% |

**Insight:**
The claim statuses are almost evenly distributed. Completed claims are the highest at **33.90%**, but cancelled and pending claims are also close, showing scope for improving claim completion efficiency.

---

### 12. What is the average quantity of food claimed per receiver?

The query calculates average food quantity claimed by each receiver.

**Actual result examples:**

| Receiver Name      | Receiver Type | City               | Average Quantity Claimed |
| ------------------ | ------------- | ------------------ | -----------------------: |
| Nancy Jones        | Shelter       | West Bradley       |                    50.00 |
| Lisa Pitts         | Shelter       | Lake Stephenport   |                    50.00 |
| Christopher Wright | Shelter       | New Kellytown      |                    50.00 |
| Nancy Silva        | Individual    | Russellville       |                    50.00 |
| Peggy Knight       | Shelter       | North Michaelville |                    50.00 |
| Daniel Williams    | Shelter       | Russellburgh       |                    50.00 |

**Insight:**
Several receivers have an average claimed quantity of **50 units**, which is the highest visible value in the output. Shelters appear frequently among high average claim receivers.

---

### 13. Which meal type is claimed the most?

The query identifies the most claimed meal type.

**Actual result:**

| Meal Type | Total Claims |
| --------- | -----------: |
| Breakfast |          278 |
| Lunch     |          250 |
| Snacks    |          240 |
| Dinner    |          232 |

**Insight:**
Breakfast is the most claimed meal type with **278 claims**, followed by lunch with **250 claims**.

---

### 14. What is the total quantity of food donated by each provider?

The query calculates total food quantity donated by each provider.

**Actual result:**

| Provider Name              | Provider Type    | City             | Total Quantity Donated |
| -------------------------- | ---------------- | ---------------- | ---------------------: |
| Barry Group                | Restaurant       | South Kathryn    |                    179 |
| Evans, Wright and Mitchell | Catering Service | North Keith      |                    158 |
| Smith Group                | Restaurant       | Jimmyberg        |                    150 |
| Nelson LLC                 | Restaurant       | Lake Andrewmouth |                    142 |
| Ruiz-Oneal                 | Grocery Store    | Lake Travis      |                    140 |

**Insight:**
Barry Group donated the highest total quantity of food with **179 units**, making it the top food donor in the dataset.

---

### 15. Which food items are near expiry?

The query identifies food items whose expiry dates are near.

**Actual result examples:**

| Food ID | Food Name | Quantity | Expiry Date | Location        | Food Type  | Meal Type |
| ------: | --------- | -------: | ----------- | --------------- | ---------- | --------- |
|       4 | Fruits    |       15 | 2025-03-16  | Kellytown       | Vegan      | Lunch     |
|      30 | Soup      |        4 | 2025-03-16  | Clarkberg       | Vegetarian | Dinner    |
|      42 | Rice      |       50 | 2025-03-16  | North Michelle  | Vegan      | Lunch     |
|      48 | Rice      |       30 | 2025-03-16  | North Jamesberg | Vegan      | Breakfast |
|      53 | Fruits    |       13 | 2025-03-16  | North Carolfurt | Vegetarian | Lunch     |

**Insight:**
The near-expiry food query helps identify items that should be distributed urgently. This is important because fast redistribution of near-expiry food can reduce wastage.

---

## Overall Key Insights

Based on the SQL analysis and EDA visualizations, the following insights were found:

* The database contains **1000 providers, 1000 receivers, 1000 food listings, and 1000 claims**.
* The total available food quantity is **25,794 units**.
* Restaurants contribute the highest food quantity with **6923 units**.
* New Carol and South Kathryn have the highest food listings with **6 listings each**.
* Vegetarian food is the most available food type with **336 listings**.
* Breakfast is the most claimed meal type with **278 claims**.
* Completed claims are the highest claim status with **339 claims**, equal to **33.90%**.
* Barry Group is the top donor with **179 units donated** and also has the highest successful claims with **5 completed claims**.
* Near-expiry food items can be identified using SQL and prioritized for quick distribution.
* The Streamlit app allows users to view data, filter food listings, access provider contacts, analyze SQL outputs, view EDA charts, and perform CRUD operations.

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
