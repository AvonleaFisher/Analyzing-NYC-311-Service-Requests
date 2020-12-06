# An Analysis of NYC 311 Service Requests 
## Predicting the Responding Government Agency

**Author**: Avonlea Fisher

**Blog Post**: https://towardsdatascience.com/analyzing-and-modelling-nyc-311-service-requests-eb6a9c9adc7c

**Dashboard**: https://nyc-311.herokuapp.com/


The contents of this repository detail an analysis of NYC 311 Service requests and the community districts in which they were recorded. Interactive visualizations that cannot render in this repository are available in the Heroku dashboard linked above (note: the dashboard may take some time to load).

## Abstract:

Data pertaining to the time, location, and content of thousands of 311 calls in New York City is recorded every day. By studying trends in this data, government agencies can respond more effectively to non-emergency requests and issues raised by the populations they serve. Using public data on 311 calls and community districts in NYC, this project explores which types of calls are the most common, how daily call volume varies across different districts, and how calls are distributed to various responding government agencies. Using natural language processing and the Keras library, this project aims to develop a neural network that can classify the government agency that responded to a call, given the call's description as an input. The best-performing model correctly classified 73% of calls in a random subset of the data. The agency variable was heavily imbalanced: the New York Police Department (NYPD) responded to just over 50% of all 311 calls. There were 14 total government agencies to which 311 calls in the dataset were assigned, which presents difficulties in training a classifier with perfect accuracy. Currently, most non-emergency service requests are handled through a phone call. This type of classifier, if developed further, could facilitate the automatic assigment of non-emergency requests to the appropriate agency in an online context where requests generate text descriptions.

## Data
The data used in this project was obtained from two sources:

* [NYC Open Data's 311 Service Requests from 2010 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

This dataset contains information about the location, time, complaint type, and status of more than 24 million 311 service requests made in New York City within the past decade. This project uses a subset of the data from 2020 that was accessed with the Socrata Open Data (SODA) API.

* [NYC Department of City Planning’s Community District Profiles](https://communityprofiles.planning.nyc.gov/)

After navigating to any profile on the Community District Profiles website, the Indicators Data can be obtained under "Download the Data." This dataset contains development and population information for each Community District in New York City. Community board names, which correspond to community districts, can also be found in the 311 dataset.

## Methods and Repository Structure
The <b>notebooks</b> for this project were organized based on the [OSEMN](https://people.duke.edu/~ccc14/sta-663/DataProcessingSolutions.html) process, and should be followed in this order:

* [Obtaining data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Obtaining_the_Data.ipynb)—Accessed data through the SODA API and Community District profiles.
* [Scrubbing data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Scrubbing_the_Data.ipynb)—Dealt with missing and unnecessary data, reformatted values for consistency, and merged the two datasets.
* [Exploring data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/tree/main/Exploring_the_Data)—Generated summary statistics and interactive visualizations of the data. Noise complaints were the most common complaint type, and the New York Police Department (NYPD) was the agency that responded to the vast majority of calls. Due to the size of the data represented in the visuals, this section is broken up into five separate notebooks:
    * Bar Charts
    * Line and Area Charts
    * Mapbox Density Heatmaps
    * Correlation Heatmap and Wordcloud
    * Scatterplots
* [Modeling data and iNterpreting data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Modeling_and_Interpreting.ipynb)—Using the Keras library, preprocessed data for modelling and evaluated the performance of different classification models with various parameter grids. Performance was evaluated on 1) test data from the resampled subset and 2) another random subset of the data that was not resampled.

The <b>Dashboard</b> folder contains the files that were used to create the NYC 311 Heroku app:

* Various CSV files with data used in app
* [main.py](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Dashboard/main.py)—Python code for app 
* [requirements.txt](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Dashboard/requirements.txt)—Dependencies 
* [Procfile](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Dashboard/Procfile)—Instructions to Heroku for how to start the app

A .gitignore file, which tells Heroku which contents are superfluous and should be ignored, was also used in deployment. More information about Heroku with Python can be found at [Heroku Dev Center](https://devcenter.heroku.com/articles/getting-started-with-python).

## Results

The best-performing model had 91.7% accuracy on the test data and 73.8% accuracy on the random subset.

#### Loss and Accuracy Curves
![Loss and Accuracy](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Images/loss_acc.png)
> Accuracy and loss curves show that the model began to learn at a mostly steady rate after about 50 epochs.

#### Mapbox Density Heatmap Example
![August](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Images/august.gif)
> This animation depicts the day-to-day changes in call volume throughout NYC in August 2020. Yellow areas on the map indicate high call volume.

#### Most Frequent Words in Call Descriptions
<img src="https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Images/wordcloud.png" width="400" height="400">

> Noise-related complaints comprised the overwhelming majority of calls each month.

> <sup>Wordcloud mask attribution: Image #19210492 at VectorStock.com<sup>

#### Top 5 Agencies with Highest Number of Calls: Hourly Totals
<img src="https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Images/Total_Calls_Hour.png" width="400" height="400">

> Calls to the NYPD, which include all noise complaints, peak at the earliest and latest hours of the day. 

## Recommendations:
* Similar classification models can be developed to connect individuals with non-emergency government services by directing them to the appropriate responding agency. This potential application would require training on a larger, more varied set of descriptors. 
* Agencies should be attentive to how call volume tends to change based on certain temporal, geographic, and environmental factors. Many of these changes are intuitively expected: widespread tree damage following major weather events, noise calls peaking in the middle of the night, and overall call volume remaining consistently high in the most densely populated borough, Manhattan. Due to the novelty of COVID-19 regulations, complaints related to COVID-19 have appeared only recently, so particular attention should be directed toward the circumstances surrounding any future peaks.
* Given that the majority of non-emergency requests are responded to by the same agency responsible for emergency requests, local stakeholders may wish to evaluate whether the current division of labor in handling 311 calls is optimal for meeting the needs of city residents. Amid growing concerns that law enforcement officers are over-utilized for intervention in non-emergency situations, this could be a fruitful area for further inquiry.

## Limitations & Next Steps

The input variable, call descriptor, consisted of just over 800 unique string values before preprocessing. The model has only been trained, therefore, to recognize a relatively limited set of words that may appear in service request descriptions. Training on a larger and more diverse set of descriptions could enhance the model's ability to match descriptions with a responding agency. 

### For further information

For any additional questions, please contact me at [fisheravonlea@gmail.com](mailto:fisheravonlea@gmail.com) or via my [LinkedIn profile](https://www.linkedin.com/in/avonlea-fisher/).
