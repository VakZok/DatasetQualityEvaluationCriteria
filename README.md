# Data Set Quality Evaluation Criteria

This project is designed to analyse the data sets of the UCR Time Series Classification Archive using quantitative metrics.
The results are discussed in depth in our paper "An Analysis of Quantitative Quality Metrics for Univariate Time Series Classification Benchmark Data Sets".

## Scripts
The scripts are numbered in the order they should be run.

1. extractDatasets.py: extract all the data sets from the downloaded UCR Time Series Classification Archive files into a single folder
2. zNormalizeUnscaledDatasets.ipynb: z-normalize the 13 unscaled data sets added to the archive in 2018
3. concatTrainAndTestData.ipynb: concatenates pairs of training and testing data sets
5. extractMetricValues.ipynb: extract the objectively evaluable metrics for each time series data set
5. analyseDatasets.ipynb: analyse the extracted metrics, create visualizations, define normal ranges and specify percentage of data sets outside of normal range

## Prerequisites

In order for the scripts to run, it is assumed that the UCR Time Series Classification Archive lies unzipped at the root folder.
The archive can be downloaded here: https://www.cs.ucr.edu/%7Eeamonn/time_series_data_2018/

If you want to start with the analysis of the extracted metrics right away, you can skip step 1-4 by using the provided extractedMetrics.csv file (result of step 4).

## Results

There are five files in the results folder:
- histograms.png: contains a PNG of the histograms of the metrics
- scatterplots.png: contains a PNG of the scatter plots of the metrics
- boxplots.png: contains a PNG of the box plots of the metrics
- metric_correlation_matrix.png: contains a PNG of the correlation matrix of the metrics