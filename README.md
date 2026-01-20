# ML Product Design Document

---

## Project title
Titanic Survival Prediction

---

## Background & Motivation
The Titanic dataset is a classic binary classification problem where the objective is to predict passenger survival based on demographic and ticket-related information.

---

## Problem Definition
- business problem
    * Given passenger information at boarding time, estimate the probability that a passenger would survive in order to understand which factors most strongly influence survival.
- ML problem
    * Task type : Binary Classification
    * Target variable : Survived(0:no,1:yes)
    * Input : Structured tabular data
- success criteria
    * Stable and reproducible validation performance
    * Reasonable generalization to unseen data
    * Interpretable model and features

---

## Stakeholders & Use case
- DS team : model development and validation
- Business team : understand suvival drivers
- Engineering team : Deployment and maintenance

---

## Data description
- Data source
    * kaggle titanic dataset
- features
    * Passenger demographics: Age, Sex
    * Socioeconomic status: Pclass, Fare
    * Family information: SibSp, Parch
    * Ticket-related: Ticket, Cabin, Embarked
- data leakage check
    * No post-event features included
    * All features available before outcome

---

## Evaluation Strategy
- Metric
    * Primary : Accuracy
    * Secondary : ROC-AUC
    * Rationale
        - the ratio of classes isn't biased
        - easy to explain
- Validation method
    * Stratified K-Fold Cross-Validation (k=5)
    * Fixed random seed for reproducibility
    * Rationale
        - Single train/validation splits are unstable for small datasets.
        - Cross-validation provides a more reliable estimate of generalization performance and reduces dependency on one specific split.

---

## Baseline model
- Model choice
    * Logistic Regression
    * Rationale
        - Interpretable
        - Low variance
        - Strong baseline for tabular data
- baseline results (for reference)
    * CV accuracy : 
    * Train vs Val gap : Small
    * Train/Val vs Test gap : Large
- Rationale
    * This baseline confirms data quality and establishes a reference point for future improvements

---

## Feature Engineering Strategy
- Goal
    * Encode domain knowledge
    * Improve linear separability
    * Reduce reliance on model complexity
- Planned features
    * FamilySize = SibSp + Parch + 1
    * IsAlone (binary)
    * Title extracted from Name
    * Age bins / child indicator
    * Fare log transformation
    * Interaction features (e.g., Sex × Pclass)
- Ratioanle
    * Each feature addition is evaluated independently to confirm stable improvement.

---

## Model Iteration strategy
- Capacity progression
    logistic-regression -> random-forest -> Gradient-Boosting
    * Ratioanle
        - lr : 
        - rf : 
        - gb : 
- Principle
    * Increase model capacity only after feature representation is sufficiently mature to avoid unnecessary overfitting.

---

## Experiment Tracking
- each experiment records,
    * model type and params
    * feature set version
    * val score (mean,std)
    * generalization gap

---

## Generalization & Risk Analysis
- Potential Risks
    - Overfitting due to small dataset
    - Validation optimism
    - Distribution shift between train and test

- Mitigation
    - Cross-validation
    - Regularization
    - Conservative feature design

---

## Deployment Consideration
- Inference  batch prediction
- Monitoring (e.g. input distribution drift, prediction confidence)
- Retraining Policy (e.g. triggered by data distribution change)

---

## Limitations
- Small dataset size
- Historical and non-actionable outcome
- Simplified evaluation metric
These limitations are explicitly acknowledged in model communication.


--------------------------------------------------------------------


■お題
Titanic

■ビジネス課題
乗客の属性情報から
生存確率を予測し、救助優先度を決めたい

■モデル設計

type: Binary Classification
baseline model: Logistic Regression

why?
- high interpretability
- use a few features
- able to prevent overfitting

■評価設計

metrics: Accuracy

why?
- the ratio of classes isn't biased
- easy to explain

■改善プラン

- try regularization
- add feature
- change model


■結果の説明

- what workked well
- what didnt work
- whay i think so
- what i would try next