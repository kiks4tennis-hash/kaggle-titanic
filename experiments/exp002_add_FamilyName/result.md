## Hypothesis
A new feature (FamilySize) will improve performance 
because the number of people they should take care of might affect the difficuly of survival.

## Model
Logistic Regression

## Parameters
solver="liblinear"

## Validation Score
Training Accuracy: 0.8006
Validation Accuracy: 0.7989

## Kaggle LB
Score: 0.76076

## Conclusion
Adding new feature dropped val score -0.0056

## Next Experiment
Try another feature.

1. title (from Name)
Example: Mr, Mrs, Miss, Master, Rare
why it works:
Encodes gender + age + social status
Often more informative than raw Sex or Age

2. Deck (from Cabin)
Example: Cabin = "C85" → Deck = "C"
Why it works:
Deck correlates with ship location
Location mattered in evacuation

