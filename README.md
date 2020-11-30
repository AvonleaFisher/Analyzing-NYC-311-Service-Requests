# An Analysis of NYC 311 Service Requests 
## Predicting the Responding Government Agency

**Author**: Avonlea Fisher

**Blog Post**: 

The contents of this repository detail an analysis of NYC 311 Service requests and the community districts in which they were recorded. 

### Problem:

Understanding trends in 311 data can help government agencies more effectively respond to requests and issues raised by the populations they serve. The exploratory analysis section of this project seeks to identify such trends, and the modelling section aims to build a classifier that can accurately predict the agency that responds to a call. This type of classification, if developed further, could facilitate the automatic assigment of non-emergency requests to the appropriate agency in a context where requests generate text descriptions.

### Data
The data used in this project was obtained from two sources:

* [NYC Open Data's 311 Service Requests from 2010 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)

This dataset contains information about the time, location, complaint type, and status of more than 24 million 311 service requests made in New York City within the past decade. This project uses a subset of the data from 2020 that was accessed with the Socrata Open Data (SODA) API.

* [NYC Department of City Planning’s Community District Profiles](https://communityprofiles.planning.nyc.gov/)

After navigating to any profile on the Community District Profiles website, the Indicators Data can be obtained under "Download the Data." This dataset contains development and population information for each Community District in New York City. Community board names, which correspond to community districts, can also be found in the 311 dataset.

## Methods
The notebooks for this project were organized based on the [OSEMN](https://people.duke.edu/~ccc14/sta-663/DataProcessingSolutions.html) process:

* [Obtaining data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Obtaining_the_Data.ipynb)—Accessed data through the SODA API and Community District profiles.
* [Scrubbing data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Scrubbing_the_Data.ipynb)—Dealt with missing and unnecessary data, reformatted values for consistency, and merged the two datasets.
* [Exploring data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/tree/main/Exploring_the_Data)—Generated summary statistics and interactive visualizations of the data. Due to the size of the data represented in the visuals, this section is broken up into five separate notebooks:
    * Bar Charts
    * Area Charts
    * Mapbox Density Heatmaps
    * Correlation Heatmap and Wordcloud
    * Scatterplots
* [Modeling data and iNterpreting data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Modeling_and_Interpreting.ipynb)—Using the Keras library, preprocessed data for modelling and evaluated the performance of different classification models with various parameter grids. 

## Results

#### Mapbox Density Heatmap Example
![August](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/August.gif)
> This animation depicts the day-to-day changes in call volume throughout NYC in August 2020. Yellow areas on the map indicate high call volume.

#### Most Frequent Words in Call Descriptions
![Word Cloud](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/311_word_cloud.png)
> Noise-related complaints comprised the overwhelming majority of calls each month.


## Recommendations:



## Limitations & Next Steps

The input variable, call descriptor, consisted of just over 800 unique string values before preprocessing. The model has only been trained, therefore, to recognize a relatively limited set of words that may appear in service request descriptions. Training on a larger and more diverse set of descriptions could enhance the model's ability to match descriptions with a responding agency. 


### For further information

For any additional questions, please contact me at mailto:fisheravonlea@gmail.com or via my [LinkedIn profile](https://www.linkedin.com/in/avonlea-fisher/).
