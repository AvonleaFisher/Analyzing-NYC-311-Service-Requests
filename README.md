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

* NYC Department of City Planning’s Community District Profiles

After navigating to any profile on the Community District Profiles website, the Indicators Data can be obtained under "Download the Data." This dataset contains development and population information for each Community District in New York City. Community board names, which correspond to community districts, can also be found in the 311 dataset.

## Methods
The notebooks for this project were organized based on the [OSEMN](https://people.duke.edu/~ccc14/sta-663/DataProcessingSolutions.html) process:

* [Obtaining data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Obtaining_the_Data.ipynb)
* [Scrubbing data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Scrubbing_the_Data.ipynb)
* [Exploring data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/tree/main/Exploring_the_Data)

Due to the size of the data represented in exploratory visuals, this section is broken up into three separate notebooks:
    * Bar Charts
    * Area Charts
    * Mapbox Density Heatmaps
    * Correlation Heatmap and Wordcloud
    * Scatterplots
* [Modeling data and iNterpreting data](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/Modeling_and_Interpreting.ipynb)

## Results

#### Mapbox Density Heatmap Example
![August](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/August.gif)
> This animation depicts the day-to-day changes in call volume throughout NYC in August 2020. Yellow areas on the map indicate high call volume.

#### Most Frequent Words in Call Descriptions
![Word Cloud](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests/blob/main/311_word_cloud.png)
> Noise-related complaints comprised the overwhelming majority of calls each month.


## Recommendations:

More of your own text here


## Limitations & Next Steps

More of your own text here


### For further information

For any additional questions, please contact Avonlea Fisher at fisheravonlea@gmail.com.


##### Repository Structure:

```

├── README.md                       <- The top-level README for reviewers of this project.
├── main_notebook.ipynb             <- narrative documentation of analysis in jupyter notebook
├── presentation.pdf                <- pdf version of project presentation
└── images
    └── images                          <- both sourced externally and generated from code

```
