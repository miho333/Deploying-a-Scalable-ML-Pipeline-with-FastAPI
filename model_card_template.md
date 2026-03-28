# Model Card

For additional information on Model Cards see: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model uses census data and a gradient boosting classifier to predict if a given individual makes above or below $50k in income. I developed this model as part of course on machine learning devlopment operations. 
Created in March 2026.
Model uses Scikit-Learn's Gradient Boosting Classifier model.
Data is taken from the 1994 census by Barry Becker, available from University of California Irvine at: https://archive.ics.uci.edu/dataset/20/census+income
License: This dataset was licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. This allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.

## Intended Use

The primary intended uses for this model are:
- To use census data to predict if a given person makes above $50k in income or less in 1994.
- As a training project to learn how to develop and deploy machine learning pipelines. Much of the comments in the code reflect the educational nature of the project.

Primary intended users:
- Students like myself who want to learn how to deploy machine learning pipelines.
- Interested parties curious in a gradient boosting classifier's ability to predict income based on census data.

Out-of-scope use cases:
- Drawing parallels or conclusions to modern census or income data. This data is 22 years out of date and likely will not match current category definitions for features like race or occupation. It also does not consider any factors outside of data available to the census dataset such market conditions or other socio-economic factors.

## Training Data

The model was trained on the 1994 census dataset mentioned earlier, available from UCI:
https://archive.ics.uci.edu/dataset/20/census+income

80% of the census dataset set was aside for use as the training dataset with Scikit-learn's train_test_split() funciton. 

Dataset features:
- age
- workclass
- fnlwgt
- education
- education-num
- marital-status
- occupation
- relationship
- race
- sex
- capital-gain
- capital-loss
- hours-per-week
- native-country
- income

## Evaluation Data

20% of the census dataset set aside for use as the evaluation dataset with Scikit-learn's train_test_split() funciton. After training the model on the training dataset it made predictions on the testing dataset. The ffficacy of the model was then evaluated according to three performance metrics: Precision, Recall, and F1 score. 

## Metrics
Scores for the evaluation metrics used to measure the model's performance:

Precision: 0.7582 
Recall: 0.6016
F1: 0.6709

## Ethical Considerations

The collected data was already anonymized and free of any personally identifiable information (PII). It it worth emphasizing again that this data should *not* be used to draw any conclusions about the present day as the data is already very out of date. Modern definitions for many fields in this dataset have also expanded, been redefined, and otherwise changed that would make this dataset incompatible with modern datasets. 

This model should not be used to make broad generalizions that would lead to descriminations about groups of people.

## Caveats and Recommendations

This work was designed to be instructional for students learning to devlop specific technical skills. It was and is a more useful as a training exercise for development processes than as a useful social evaluation. More modern datasets and sophisticated evaluations of this dataset are likely available online. 