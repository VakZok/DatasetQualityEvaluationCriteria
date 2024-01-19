# Data Set Quality Evaluation Criteria

This project is designed to evaluate the data sets of the UCR Time Series Classification Archive using various quality metrics. The results are discussed in depth in our paper "An Analysis of Quantitative Quality Metrics for Univariate Time Series Classification Benchmark Data Sets".

## Overview

- extractDatasets.py: This script is designed to find and copy all files with a '.tsv' extension from a specified root folder and its subfolders to a destination folder.
- concatTrainAndTestData.ipynb: This script concatenates pairs of training and testing datasets from the UCR Time Series Classification archive.
- zNormalizeUnscaledDatasets.ipynb: The purpose of this script is to normalize the 13 unscaled data sets from the UCR Time Series Classification Archive.
- extractMetricValues.ipynb: This script serves the purpose of extracting various statistical metrics and information from the data sets into a .csv-file.
- preparedMetricsToAnalyse.csv: This table includes all the 
- analyseDatasets.ipynb: With this script, the data sets are analysed. A correlation matrix, histograms, box plots and scatter plots are created, the normal ranges are calculated and the outlier data sets are specified as a percentage.

### Prerequisites

In order for the scripts to run, it is assumed that the UCR Time Series Classification Archive can be found unzipped in the root folder. The archive can be downloaded here: https://www.cs.ucr.edu/%7Eeamonn/time_series_data_2018/

### Reproducing the test

1. Make sure to have the "UCRArchive_2018"-folder in your root folder.
2. Run the extractDatasets.py script.
3. Run the concatTrainAndTestData.ipynb script.
3. Run the zNormalizeUnscaledDatasets.ipynb script.
4. Run the extractMetricValues.ipynb script.
5. [OPTIONAL] Import the extractedMetrics.csv & the .csv from the UCR archive website into a Excel file. Sort ascending by data set name. Manually transfer the desired information from the UCR table ('additionalUCRInformation.csv' in this case) to the 'extractedMetrics' table. This involves filling in the empty columns in the 'extractedMetrics.csv' table with information from the UCR table.Remove the value for the learned 'w' in the 'dynamic time warping learned' column. Specifically for the 'SmoothSubspace' dataset, insert the mean of all KS statistic values. This is done because of an initially calculated value of 66, and the calculation error could not be found. Manually calculate the following metrics for each dataset:
train test ratio, percentage of missing values, percentage of duplicate values 
6. Run the analyseDatasets.ipynb script.

