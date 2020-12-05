# An Analysis of NYC 311 Service Requests 
## Predicting the Responding Government Agency

**Author**: Avonlea Fisher

**Blog Post**: https://towardsdatascience.com/analyzing-and-modelling-nyc-311-service-requests-eb6a9c9adc7c

The contents of this repository detail an analysis of NYC 311 Service requests and the community districts in which they were recorded. 

## Abstract:

Data pertaining to the time, location, and content of thousands of 311 calls in New York City is recorded every day. By studying trends in this data, government agencies can respond more effectively to non-emergency requests and issues raised by the populations they serve. Using public data on 311 calls and community districts in NYC, this project explores which types of calls are the most common, how daily call volume varies across different districts, and how calls are distributed to various responding government agencies. Using natural language processing and the Keras library, this project aims to develop a neural network that can classify the government agency that responded to a call, given the call's description as an input. The best-performing model correctly classified 73% of calls in a random subset of the data. The agency variable was heavily imbalanced: the New York Police Department (NYPD) responded to just over 50% of all 311 calls. There were 14 total government agencies to which 311 calls in the dataset were assigned, which presents difficulties in training a classifier with perfect accuracy. Currently, most non-emergency service requests are handled through a phone call. This type of classifier, if developed further, could facilitate the automatic assigment of non-emergency requests to the appropriate agency in an online context where requests generate text descriptions.

## Data
The data used in this project was obtained from two sources:

* [NYC Open Data's 311 Service Requests from 2010 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

This dataset contains information about the location, time, complaint type, and status of more than 24 million 311 service requests made in New York City within the past decade. This project uses a subset of the data from 2020 that was accessed with the Socrata Open Data (SODA) API.

* [NYC Department of City Planning’s Community District Profiles](https://communityprofiles.planning.nyc.gov/)

After navigating to any profile on the Community District Profiles website, the Indicators Data can be obtained under "Download the Data." This dataset contains development and population information for each Community District in New York City. Community board names, which correspond to community districts, can also be found in the 311 dataset.

## Methods
The notebooks for this project were organized based on the [OSEMN](https://people.duke.edu/~ccc14/sta-663/DataProcessingSolutions.html) process:

* [Obtaining data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Obtaining_the_Data.ipynb)—Accessed data through the SODA API and Community District profiles.
* [Scrubbing data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Scrubbing_the_Data.ipynb)—Dealt with missing and unnecessary data, reformatted values for consistency, and merged the two datasets.
* [Exploring data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/tree/main/Exploring_the_Data)—Generated summary statistics and interactive visualizations of the data. Noise complaints were the most common complaint type, and the New York Police Department (NYPD) was the agency that responded to the vast majority of calls. Due to the size of the data represented in the visuals, this section is broken up into five separate notebooks:
    * Bar Charts
    * Area Charts
    * Mapbox Density Heatmaps
    * Correlation Heatmap and Wordcloud
    * Scatterplots
* [Modeling data and iNterpreting data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Modeling_and_Interpreting.ipynb)—Using the Keras library, preprocessed data for modelling and evaluated the performance of different classification models with various parameter grids. Performance was evaluated on both test data from the resampled subset, as well as another random subset that was not resampled.

## Results

The best-performing model had 90% accuracy with the test data and 73% accuracy with the random subset.

#### Loss and Accuracy Curves
![Loss and Accuracy](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/loss_v_accuracy.png)
> Accuracy and loss curves show that the model began to learn at a mostly steady rate after about 50 epochs.

#### Mapbox Density Heatmap Example
![August](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/August.gif)
> This animation depicts the day-to-day changes in call volume throughout NYC in August 2020. Yellow areas on the map indicate high call volume.

#### Most Frequent Words in Call Descriptions
![Word Cloud](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/311_word_cloud.png)
> Noise-related complaints comprised the overwhelming majority of calls each month.

#### Call Totals by Time of Day
<img src="https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/hourly_calls.png" width="400" height="400">
> Calls to the NYPD, which include all noise complaints, peak at the earliest and latest hours of the day. 

## Recommendations:
Similar classification models can be developed to connect individuals with non-emergency government services by directing them to the appropriate responding agency. Given that the majority of non-emergency requests are responded to by the same agency responsible for emergency requests, local stakeholders may wish to evaluate whether the current division of labor in handling 311 calls is optimal for meeting the needs of city residents. 

## Limitations & Next Steps

The input variable, call descriptor, consisted of just over 800 unique string values before preprocessing. The model has only been trained, therefore, to recognize a relatively limited set of words that may appear in service request descriptions. Training on a larger and more diverse set of descriptions could enhance the model's ability to match descriptions with a responding agency. 

### For further information

For any additional questions, please contact me at [fisheravonlea@gmail.com](mailto:fisheravonlea@gmail.com) or via my [LinkedIn profile](https://www.linkedin.com/in/avonlea-fisher/).
