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

## What we learned
- Technologies used
