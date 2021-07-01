# Prediction of food products' ecological footprint 👣
According to research by [Our World in Data](https://ourworldindata.org/), food production generates **more** than 25% of global greenhouse gas emissions. One of the best ways to minimize our impact on the environment is to pay more attention to the food we consume and rethink the products with a high CO2 score. With this goal in mind, I have created Foodly. Foodly provides you with information about the total CO2 score per kilogram of your chosen product and suggests other products in the same food category with the lowest environmental impact. Based on the results, Foodly additionally shows you an equivalent in kilometers of driving a regular petrol car and minutes of a commercial flight.

<p align="center">
<kbd><img src="https://github.com/lenaromanenko/food_carbon_footprint/blob/main/readme_images/GitHub%20Share%20Foodly.png" width="1000"></kbd>
</p>
      
foodly.cc is currently unavailable! ⏳ (The project is available via www.foodly.cc Please note: The website is not optimized for mobile screens, and it may take ca. 20 seconds to load the page when you try to access it for the first time during your session. This is due to using a free tier Heroku server that goes to sleep when the website was not visited recently.)

<p align="center">
<kbd><img src="https://github.com/lenaromanenko/food_carbon_footprint/blob/main/readme_images/Foodly_HD_readme.gif" width="900"></kbd>
</p>

### Data Sources:
- Small data set with CO2 scores from [Kaggle ](https://www.kaggle.com/)
- Extensive data set without CO2 scores from [FooDB](https://foodb.ca/)
- Country codes ISO alpha-2 from [International Organization for Standardization (ISO)](https://www.iso.org/obp/ui/#search/code/)
- Data set about human consumption of food from [Food and Agriculture Organization (FAO)](http://www.fao.org/faostat/en/#data/FBS/report)

### Dashboard:
<p align="center">
<kbd><img src= "https://github.com/lenaromanenko/food_carbon_footprint/blob/main/readme_images/Dashboard_Foodly.gif" width="900"></kbd>
</p>

### Workflow:
1. Hosting MySQL Database in the cloud using AWS Relational Database Services (RDS).
2. Reading, cleaning, and merging the data in JupyterLab.
3. Exploring the data by writing SQL Queries and creating a dashboard using PostgreSQL and Metabase.
4. Train-test split, feature engineering.
5. Solving the problem with missing CO2 scores in the large data set using Gradient Boosting Regressor to predict CO2 scores based on the small data set from Kaggle and generate a more extensive database for Foodly.
6. Creating a web interface using Flask and Bootstrap.
7. Deploying the app to Heroku.

<p align="center">
<kbd><img src="https://github.com/lenaromanenko/food_carbon_footprint/blob/main/readme_images/Tech%20Stack%20Foodly.png" width="1000"></kbd>
</p>

This project has been created as a final project during the last week of the Data Science Boot Camp at [SPICED Academy](https://www.spiced-academy.com/de/?gclid=Cj0KCQjwpdqDBhCSARIsAEUJ0hMmcIQjTdphHzDxQTmnqK5hOF_SyvKfxtLCWJCT485yk5wrQXlz2zQaAjYyEALw_wcB).

### To Do:
- Fix bugs 🐞 Sometimes, Foodly shows the wrong results with a higher score bc there are no products with the same or lower score in this food category
- Train the model with new features (e.g. add nutritions)
- Deploy the dashboard to AWS
- Front-end: fix mobile version of the website, change [icons](https://www.flaticon.com/) in description
- Add some diagrams to the website (e.g. dashboard from Metabase or create horizontal sankey diagram using Tableau)
