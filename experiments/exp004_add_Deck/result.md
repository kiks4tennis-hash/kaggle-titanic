## Hypothesis
A new feature (Title) affects performance 
because it encodes more information about passenger, like gender + age + social status.

## Model
Logistic Regression

## Parameters
solver="liblinear"

## Validation Score
Training Accuracy: 0.8160
Validation Accuracy: 0.8156

## Kaggle LB
Score: 0.77990

## Conclusion
This try improved train and val score by +1 point compared with baseline.

## Next Experiment
Try another feature on top of this experiment.

2. Deck (from Cabin)
Example: Cabin = "C85" → Deck = "C"
Why it works:
Deck correlates with ship location
Location mattered in evacuation

