# 🚢 Will I Survive Titanic?

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](#)
[![License](https://img.shields.io/badge/license-MIT-green)](#)

A lightweight ensemble-based predictive model for the Titanic dataset, leveraging the `BlackSwan` strategy with 100 minimal submodels.

## 🚀 Project Overview

This repository provides a Python-based model that answers the classic Kaggle Titanic competition question: **Would this person survive?**

Rather than using a traditional ML framework, it offers:
- 100 handwritten submodels, each making a micro-judgment.
- A custom CSV parser.
- A feature importance estimator.
- Lightweight tools for model interpretation and visualization.

## 📁 Main Components

### `titanic.py`
This is the core library that includes:
- `make_population(csv_path)` → Parses a Titanic CSV file and returns a list of dictionaries (one per row).
- `my_function(row_dict)` → Predicts survival likelihood (0–1) for a given passenger.
- `my_graphic_function(row_dict)` → Returns a detailed dictionary with:
  - Raw input
  - Survival estimate
  - Similar rows used in prediction
  - Feature contribution summary
- `get_feature_importance()` → Shows global feature influence.
- `datapoint_to_csv(row_dict)` → Converts a single passenger dictionary back into a CSV string.

### CSV Files
- `train.csv` – used as training basis for all models.
- `test.csv` – standard evaluation set (like on Kaggle).

## 🧠 How to Use

```python
from titanic import make_population, my_function, my_graphic_function

# Load test data
population = make_population("test.csv")

# Predict survival for the first passenger
prediction = my_function(population[0])

# Get a full visual + feature breakdown
report = my_graphic_function(population[0])
print(report["estimation"])  # e.g., 0.113 = 11.3% chance of survival
print(report["features_audit"])  # Feature weights
```

## 🏗️ Model Logic

The prediction is based on 100 minimal models (`function_nu_0` to `function_nu_99`), each voting on the result. Their outputs are aggregated to produce the final probability.

Each model focuses on different heuristics like fare class, gender, age, or ticket number patterns. This acts as a hand-crafted ensemble meant to simulate feature diversity.

## 📊 Output Breakdown

When calling `my_graphic_function`, you get:
- `estimation`: The predicted survival probability.
- `features_audit`: Shows how important each feature was in the decision.
- `csv`: A generated table of similar passengers used for reasoning.

## ✅ Requirements

No external libraries required beyond Python 3 standard library.

## 👤 Author

Developed by **Charles Dana** under the Algorithme.ai.

## 🧾 License

This project is licensed under the [MIT License](./LICENSE) — feel free to use, modify, and distribute.
