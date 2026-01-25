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

- Train ≈ Val and both low
    -> unable to capture meaningful feature (each feature contribute independently in lr)
    -> unable to capture non-linear interactions because model could be too simple

- Val >> LB
    -> This drop is normal because
        - Training/validation data and test data come from different distributions. (e.g.Passenger demographics differ)
        - Public LB is noisy (only part of test set)
    -> However, we can also say there is room for generalization improvement.

## Next Experiment
- add feature for better generalization of logistic regression.
- use decision tree to caputre no-linear interactions.
- try some hyperparameters