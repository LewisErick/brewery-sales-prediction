# Hack MTY
## JDA Challenge

## Inspiration
Keep it simple.

## What it does
Predicts the next three months of demand for the products based on historical data.

## How we built it
- Scikit learn model trains on historical data and predicts next three months unit sales
- Flask server to serve results from model to UI
- UI in Vue JS for visualization results additional to the generated csv with predictions

## Challenges we ran into
- Model training time
- Feature engineering wasn't working
- Linear regression model had a very low R2 score, so we opted for 

## Accomplishments that we're proud of
- 31.09 MSE
- 81.72% R2 Score on Holdout Set
- Successful predictions exported as CSV
- UI that displays and filters predictions for visualization

## What we learned
- Technologies used

## Prototype
https://xd.adobe.com/view/6b1e5abb-63da-4bf4-5e55-99d98fb0f28c-1d2f/

## Design Document
https://docs.google.com/document/d/1nO4DE8haCMBuGBMlUqrNuGajJz8BdoYMsDWdVw-Zc4I/edit?usp=sharing

## Results (output csv)
https://drive.google.com/file/d/1tZQJ8R8LIzYaZShG1Untl_6UsehCfvSB/view?usp=sharing
