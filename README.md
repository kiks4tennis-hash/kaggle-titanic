# ML Product Design Document


## Project title
Titanic Survival Prediction

## Background & Motivation


## Problem Definition
- business problem
- ML problem
- success criteria

## Stakeholders & Use case
- e.g. DS team : model development and validation
       Business team : understand suvival drivers

## Data description
- data source
- features
- data leakage check

## Evaluation Strategy
- metric (=accuracy why?)
- validation method 

## Baseline model
- model choice
- reasoning
- baseline results (for reference)

## Feature Engineering Strategy
- planned features
    * Each feature addition is evaluated independently to confirm stable improvement.

## Model Iteration strategy
- capacity progression
    logistic-regression -> random-forest -> Gradient-Boosting
    * Increase model capacity only after feature representation is sufficiently mature to avoid unnecessary overfitting.

## Experiment Tracking
- each experiment records,
    - model type and params
    - feature set version
    - val score (mean,std)
    - generalization gap

## Generalization & Risk Analysis
- potential risk
- mitigation

## Deployment Consideration
- Inference  batch prediction
- Monitoring (e.g. input distribution drift, prediction confidence)
- Retraining Policy (e.g. triggered by data distribution change)







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