from flask import Flask
from flask import render_template, request
import numpy as np
import pandas as pd
import boto3

personalize_runtime = boto3.client('personalize-runtime')
app = Flask(__name__)

# Load the data and campaignARN
artikel_raw = pd.read_csv('data/raw/artikel_agg_2018.csv')
artikel = artikel_raw[['id', 'name']]
artikel.columns = ['ITEM_ID', 'TITLE']

campaign_arn = "arn:aws:personalize:eu-west-1:873674308518:campaign/recommender-test-campaign"

# Create index webpage that receives user ID for recommendations
@app.route('/')
@app.route('/index')
def index():
    return render_template('master.html')

# Create web page that handles user query and displays model results
@app.route('/go')
def go():
    # Save user input in query
    query = request.args.get('query', '')

    # Get recommendations for query
    get_recommendations_response = personalize_runtime.get_recommendations(
        campaignArn=campaign_arn,
        userId=str(query))

    item_list = get_recommendations_response['itemList']
    recommendations = pd.Series(
        [artikel.loc[artikel['ITEM_ID'] == item['itemId']].values[0][-1]
            for item in item_list],
        name='Artikel',
        index=np.arange(1, 26, 1))

    # classification_labels = model.predict([query])[0]
    # classification_results = dict(zip(df.columns[4:], classification_labels))

    # Render the go.html
    return render_template(
        'go.html',
        query=query,
        rec_result=recommendations
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
