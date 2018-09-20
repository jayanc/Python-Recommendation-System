# User-Items Recommendation Systems

This repo shows a set of Jupyter Notebooks demonstrating a online retail recommendation systems which recommend items for the [online-retail dataset](https://www.kaggle.com/jihyeseo/online-retail-data-set-from-uci-ml-repo). 

Here are the different notebooks:
* [Data Processing](https://github.com/AdnanShah/Python-Recommendation-System/blob/master/retail_recom_sys_data_preprocessing.ipynb): Loading and processing the data to prepare them for input into my models.
* [Deep Learning Model](https://github.com/AdnanShah/Python-Recommendation-System/blob/master/retail_recom_sys.ipynb): Using implicit collaborative filtering which is a Deep Learning approach

## Data Source

This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

https://www.kaggle.com/jihyeseo/online-retail-data-set-from-uci-ml-repo

## Installing

I created a virtual environment in my machine, and run the code. 
To run the python code first create a virtual environment and install all dependencies by run the command:

```
$: pip install -r requirements.txt 
```
and run jupyter nootebook

```
$:  jupyter nootebook
```
To make predictions run lightFM_retail_recom_sys _prediction.ipynb


## Requirements

* [Python 2.7](https://www.python.org/download/releases/2.7/) or [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [Jupyter Notebook](http://jupyter.org/)

## Dependencies

Choose the latest versions of any of the dependencies below:
* [lightfm](https://github.com/lyst/lightfm)
* [pandas](https://pandas.pydata.org/)
* [numpy](http://www.numpy.org/)
* [scipy](https://www.scipy.org/)
* [sklearn](http://scikit-learn.org/stable/)

