## Hypothesis
baseline model

## Model
Logistic Regression

## Parameters
solver="liblinear"

## Validation Score
Training Accuracy: 0.8006
Validation Accuracy: 0.8045

## Kaggle LB
Score: 0.76076

## Conclusion
- Val >> LB
    -> suggests remaining generalization gap and room for improvement
        -> feature engineering because each feature contributes independantly in logistic regression. proper and meaningful features are important to predict target.
        -> higher-capacity models to express more complex patterns.
    -> Data leakage , overfitting could be occured. (but train≈test)
    -> This drop is normal because
        - Training/validation data and test data come from different distributions. (e.g.Passenger demographics differ)
        - Public LB is noisy (only part of test set)

- Train ≈ Val and both low
    -> Model could be too simple, which means the model seems unable to capture non-linear interactions. (Model capacity problem)
    -> No signs of overfitting.

## Next Experiment
- use cross-validation to improve evaluation process. 