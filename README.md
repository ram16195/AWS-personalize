# Recommender System with Amazon Personalize

Building a recommender system with Amazon Personalize using the SDK for Python option (boto3). The basic data consists of a B2B-Retail set containing roughly 2.8 Mio. user-item interactions for approx 104'000 users and 74'000 interactions. I also provided the industry sector of the users as meta-data but this did not improve the solution. I left the choice of algorithm and model tuning to the Personalize Service and it selected a HRNN model.

 When the campaign is activated (it is not at the moment), the recommendations can be requested from a little web app.

### Code / Files

- `1-AWS_Recommender_Test_Retail.ipynb`: Main jupyter notebook, containing code for cleaning and uploading the data, creating and activating the recommendation solution.
- `run.py`: Launches a little web app to get recommendation for individual user IDs. 
- `templates`: Folder containing the files necessary to run and render the web app.
- `demo_notebooks`: Folder containing different demo notebooks from AWS repository (e.g. how to enable cold starts etc.)

### Run the web app

In a terminal or command window, navigate to the top-level project directory (the one that contains this README) and run the following command:

```bash
python run.py
```
(Then go to http://0.0.0.0:3001, or on your local machine: http://127.0.0.1:3001/)

### Install

This project requires **Python 3.x** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [flask](https://pypi.org/project/Flask)


You will also need to have software installed to run and execute an [iPython Notebook](http://ipython.org/notebook.html)