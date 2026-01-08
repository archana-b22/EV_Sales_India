-- Total EV sales by year
SELECT year, SUM(ev_sales_quantity) AS total_sales
FROM ev_sales
GROUP BY year
ORDER BY year;

-- Top 10 states by EV sales
SELECT state, SUM(ev_sales_quantity) AS total_sales
FROM ev_sales
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;

-- EV sales by vehicle category
SELECT vehicle_category, SUM(ev_sales_quantity) AS total_sales
FROM ev_sales
GROUP BY vehicle_category
ORDER BY total_sales DESC;

-- EV sales by vehicle type
SELECT vehicle_type, SUM(ev_sales_quantity) AS total_sales
FROM ev_sales
GROUP BY vehicle_type
ORDER BY total_sales DESC;