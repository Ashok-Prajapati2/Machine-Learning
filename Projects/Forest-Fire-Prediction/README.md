# Forest Fire Prediction in Algeria
This repository contains the Exploratory Data Analysis (EDA) and implementation of Machine Learning algorithms on the Algerian forest fires dataset. The goal of this project is to predict future forest fires in Algeria by analyzing historical data and training machine learning models.

## About the Dataset

The dataset used in this project contains information about forest fires that occurred in two regions of Algeria: Bejaia region and Sidi Bel-Abbes region, from June to September 2012. The data includes the following features:
- Date (DD/MM/YYYY): Day, month (June to September), year (2012)
- Weather data observations:
  - Temp: temperature noon (temperature max) in Celsius degrees (22 to 42)
  - RH: Relative Humidity in % (21 to 90)
  - Ws: Wind speed in km/h (6 to 29)
  - Rain: total day in mm (0 to 16.8)
- FWI Components:
  - Fine Fuel Moisture Code (FFMC) index from the FWI system (28.6 to 92.5)
  - Duff Moisture Code (DMC) index from the FWI system (1.1 to 65.9)
  - Drought Code (DC) index from the FWI system (7 to 220.4)
  - Initial Spread Index (ISI) index from the FWI system (0 to 18.5)
  - Buildup Index (BUI) index from the FWI system (1.1 to 68)
  - Fire Weather Index (FWI) Index (0 to 31.1)
- Classes: two classes, namely: fire and not fire

This dataset provides valuable information for understanding the patterns and causes of forest fires in Algeria, and can be used to predict future forest fires.

## EDA
In order to gain insight into the patterns and trends of forest fires in Algeria, the data is analyzed and visualized in the EDA. In addition, the data is pre-processed in order to prepare it for use in the machine learning models.

## Machine Learning Algorithms
The following machine learning algorithms have been implemented on the data:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* XGB Classifier
## Results
The results of the machine learning models are compared and evaluated, and the best performing model is selected based on its accuracy.

## Future Work
This project can be further improved by using more advanced machine learning algorithms, and by incorporating additional data sources such as satellite imagery.