-- =====================================================
-- Local Food Wastage Management System
-- SQL Analysis Queries
-- =====================================================

USE food_wastage_db;


-- Query 1: How many food providers are there in each city?

SELECT 
    City,
    COUNT(*) AS total_providers
FROM providers
GROUP BY City
ORDER BY total_providers DESC;


-- Query 2: How many receivers are there in each city?

SELECT 
    City,
    COUNT(*) AS total_receivers
FROM receivers
GROUP BY City
ORDER BY total_receivers DESC;


-- Query 3: Which type of food provider contributes the most food?

SELECT 
    Provider_Type,
    SUM(Quantity) AS total_food_quantity
FROM food_listings
GROUP BY Provider_Type
ORDER BY total_food_quantity DESC;


-- Query 4: Contact information of food providers in a specific city
-- You can change 'New Carol' to any city from your dataset.

SELECT 
    Name,
    Type,
    Address,
    City,
    Contact
FROM providers
WHERE City = 'New Carol';


-- Query 5: Which receivers have claimed the most food?

SELECT 
    r.Receiver_ID,
    r.Name,
    r.Type,
    r.City,
    COUNT(c.Claim_ID) AS total_claims
FROM receivers r
JOIN claims c
ON r.Receiver_ID = c.Receiver_ID
GROUP BY r.Receiver_ID, r.Name, r.Type, r.City
ORDER BY total_claims DESC;


-- Query 6: What is the total quantity of food available from all providers?

SELECT 
    SUM(Quantity) AS total_food_available
FROM food_listings;


-- Query 7: Which city has the highest number of food listings?

SELECT 
    Location,
    COUNT(*) AS total_food_listings
FROM food_listings
GROUP BY Location
ORDER BY total_food_listings DESC;


-- Query 8: What are the most commonly available food types?

SELECT 
    Food_Type,
    COUNT(*) AS total_count
FROM food_listings
GROUP BY Food_Type
ORDER BY total_count DESC;


-- Query 9: How many food claims have been made for each food item?

SELECT 
    f.Food_ID,
    f.Food_Name,
    COUNT(c.Claim_ID) AS total_claims
FROM food_listings f
LEFT JOIN claims c
ON f.Food_ID = c.Food_ID
GROUP BY f.Food_ID, f.Food_Name
ORDER BY total_claims DESC;


-- Query 10: Which provider has had the highest number of successful food claims?

SELECT 
    p.Provider_ID,
    p.Name AS provider_name,
    p.Type AS provider_type,
    p.City,
    COUNT(c.Claim_ID) AS successful_claims
FROM providers p
JOIN food_listings f
ON p.Provider_ID = f.Provider_ID
JOIN claims c
ON f.Food_ID = c.Food_ID
WHERE c.Status = 'Completed'
GROUP BY p.Provider_ID, p.Name, p.Type, p.City
ORDER BY successful_claims DESC;

-- Query 11: What percentage of food claims are completed, pending, and cancelled?

SELECT 
    Status,
    COUNT(*) AS total_claims,
    ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims)), 2) AS percentage
FROM claims
GROUP BY Status
ORDER BY total_claims DESC;


-- Query 12: What is the average quantity of food claimed per receiver?

SELECT 
    r.Receiver_ID,
    r.Name AS receiver_name,
    r.Type AS receiver_type,
    r.City,
    ROUND(AVG(f.Quantity), 2) AS average_quantity_claimed
FROM receivers r
JOIN claims c
ON r.Receiver_ID = c.Receiver_ID
JOIN food_listings f
ON c.Food_ID = f.Food_ID
GROUP BY r.Receiver_ID, r.Name, r.Type, r.City
ORDER BY average_quantity_claimed DESC;


-- Query 13: Which meal type is claimed the most?

SELECT 
    f.Meal_Type,
    COUNT(c.Claim_ID) AS total_claims
FROM food_listings f
JOIN claims c
ON f.Food_ID = c.Food_ID
GROUP BY f.Meal_Type
ORDER BY total_claims DESC;


-- Query 14: What is the total quantity of food donated by each provider?

SELECT 
    p.Provider_ID,
    p.Name AS provider_name,
    p.Type AS provider_type,
    p.City,
    SUM(f.Quantity) AS total_quantity_donated
FROM providers p
JOIN food_listings f
ON p.Provider_ID = f.Provider_ID
GROUP BY p.Provider_ID, p.Name, p.Type, p.City
ORDER BY total_quantity_donated DESC;


-- Query 15: Which food items are near expiry?

SELECT 
    Food_ID,
    Food_Name,
    Quantity,
    Expiry_Date,
    Location,
    Food_Type,
    Meal_Type
FROM food_listings
WHERE Expiry_Date <= DATE_ADD(CURDATE(), INTERVAL 7 DAY)
ORDER BY Expiry_Date ASC;