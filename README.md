# Project 3: Home Value & Temperature City Map
Presented by: Group 3 - Connor Crowley, David Gamarran, Ziye Jin

Project Goal
Analyzing climate data to understand potential effects of temperature on home values in major U.S. cities. This application aims to identify trends in precipitation and temperature to assess impacts on housing prices.

City Selection
We selected 14 major U.S. cities spanning diverse geographic regions and climates:

Northeast: New York City, NY & Boston, MA
Southeast: Miami, FL & Atlanta, GA
Midwest: Chicago, IL & Minneapolis, MN
South: Dallas, TX & Houston, TX
West: Los Angeles, CA & San Francisco, CA & Seattle, WA
Mountain West: Denver, CO
Desert Southwest: Phoenix, AZ & Las Vegas, NV
Datasets
Open Meteo
Zillow Research
Data Cleaning
Consolidated data from 14 cities into two files: Home Value and Temperature.
Converted daily temperature readings to monthly averages.
Ensured alignment of temperature and home value data by end-of-month dates.
Application Features
Default map of the U.S. with markers for each city.
Interactive dropdown menu to select and zoom into each city on the map.
Historical home value chart displaying data for the past five years (monthly).
Temperature trend chart showing monthly data for the past five years.
Default Screen
Upon selecting a city from the dropdown menu, the map zooms into the selected city with corresponding home value and temperature charts displayed.

Summary
HTML Structure:

Organized web page with map area, city selector dropdown, and chart canvases.
Div containers for layout and styling.
Styling:

CSS applied for visual enhancements and layout adjustments.
Map Initialization:

Implemented using Leaflet library, centered on the U.S.
Added city markers with swipe and zoom functionalities.
City Selector:

Dropdown populated with city names.
Event listener updates map and charts based on city selection.
Home Value Chart:

Fetched data via server-side API.
Chart.js used to visualize home value trends.
Dynamic chart updates based on selected city.
Temperature Chart:

Similar setup as home value chart.
Displays temperature trends over time.
Miscellaneous Scripts:

Includes additional scripts for examples and checks (e.g., Results variable).
Event Listeners:

Listeners for dropdown selection to update visuals.


Conclusion
Our analysis of major U.S. cities showed varied trends in home values, with notable decreases in San Francisco, Seattle, and Minneapolis. However, temperature variations did not consistently correlate with these trends across all cities. Our application serves as a tool for homebuyers to consider climate factors, despite inconclusive correlations found in our data.

Due to time constraints, features such as sunshine hours tracking, air quality monitoring, and broader home type analysis were not implemented. These areas will be addressed in future updates for enhanced application functionality.
