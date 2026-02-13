# US Pollution Analysis

An end-to-end data science project analyzing air pollution across the United States — from raw data ingestion through exploratory analysis to machine learning modeling.

## Overview

This project leverages a comprehensive dataset of **~1.4 million** air pollution measurements covering four major pollutants — nitrogen dioxide (NO₂), sulfur dioxide (SO₂), carbon monoxide (CO), and ozone (O₃) — recorded at EPA monitoring stations across multiple U.S. states over several years.

The goal is to clean and transform this data, uncover spatial and temporal patterns, and apply machine learning techniques to:
- **Predict** pollutant concentrations from temporal and geographic features
- **Classify** air quality levels (Good / Moderate / Unhealthy)
- **Identify** the most important factors driving pollution
- **Detect** anomalous pollution events

## Project Structure

```
US_pollution_analysis/
│
├── data/
│   ├── raw/                        # Original CSV dataset (not tracked — too large)
│   ├── preprocessed/               # Parquet conversion + geocoded dataset
│   │   └── pollution_dataset_geocoded.parquet
│   └── processed/                  # Final cleaned dataset ready for modeling
│       └── pollution_dataset_cleaned.parquet
│
├── notebooks/
│   ├── csv_to_parquet.ipynb        # Step 1: Convert large CSV to Parquet format
│   ├── coordinates_to_dataset.ipynb # Step 2: Enrich dataset with lat/lon coordinates
│   ├── etl_eda.ipynb               # Step 3: ETL pipeline — cleaning, AQI calculation, unit conversion
│   └── ml_modeling.ipynb           # Step 4: Machine learning — regression, classification, anomaly detection
│
├── reports/
│   └── figures/                    # Saved plots and visualizations
│
├── README.md
└── requirements.txt
```

## Dataset

**Source:** [US Pollution Dataset on Kaggle](https://www.kaggle.com/datasets/sogun3/uspollution)

The raw dataset is too large to include directly in the repository. It was converted to Parquet format for efficient storage and fast I/O.

### Columns (Raw Dataset — 28 variables)

| Column | Description |
|--------|-------------|
| State Code | Numeric code representing the U.S. state |
| County Code | Numeric code for the county within the state |
| Site Num | Identifier for the air monitoring site |
| Address | Street address of the monitoring station |
| State | Full name of the U.S. state |
| County | Name of the county |
| City | City where the measurement site is located |
| Date Local | Date of the observation (YYYY-MM-DD) |
| NO2 Units / Mean / 1st Max Value / 1st Max Hour / AQI | Nitrogen dioxide measurements |
| O3 Units / Mean / 1st Max Value / 1st Max Hour / AQI | Ozone measurements |
| SO2 Units / Mean / 1st Max Value / 1st Max Hour / AQI | Sulfur dioxide measurements |
| CO Units / Mean / 1st Max Value / 1st Max Hour / AQI | Carbon monoxide measurements |

### Cleaned Dataset (22 columns, ~407 500 rows)

After the ETL pipeline, pollutant concentrations are standardized to **µg/m³** and the dataset includes computed AQI values and geographic coordinates (Latitude, Longitude).

## Notebooks

### 1. `csv_to_parquet.ipynb` — Data Format Conversion

Converts the original large CSV file into Apache Parquet format for:
- Significant file size reduction (~10× smaller)
- Columnar storage enabling fast analytical queries
- Compatibility with pandas, PyArrow, and Spark

### 2. `coordinates_to_dataset.ipynb` — Geocoding

Enriches the dataset with geographic coordinates (latitude and longitude) for each monitoring station address, enabling spatial analysis and map-based visualizations.

### 3. `etl_eda.ipynb` — ETL Pipeline & Data Cleaning

The core data preparation notebook:

- **Load** the geocoded Parquet dataset
- **Remove invalid data**: negative pollutant values (physically impossible) — 8,286 negative SO₂ and 1,064 negative CO rows removed
- **Compute missing AQI values**: SO₂ AQI and CO AQI were missing for ~870K rows. Recalculated using EPA breakpoint tables and linear interpolation formula
- **Remove duplicates**: exact duplicates dropped; conflicting duplicates (same date/address, different values) resolved by keeping maximum values (consistent with EPA AQI methodology)
- **Validate**: final check for remaining negative values (828 in NO₂ — auto-removed)
- **Standardize units**: all pollutant concentrations converted from ppb/ppm to µg/m³ using EPA conversion factors at standard conditions (25°C, 1 atm)
- **Save** cleaned dataset to `pollution_dataset_cleaned.parquet`

### 4. `ml_modeling.ipynb` — Machine Learning

Implements four ML use-cases on the cleaned dataset:

#### Regression — Predicting O₃ Concentration
- **Target**: O₃ Max (µg/m³)
- **Features**: temporal (year, month cyclical encoding, day of week), geographic (lat, lon, state), cross-pollutant means (NO₂, SO₂, CO)
- **Models**: Linear Regression (baseline), Random Forest, Gradient Boosting / XGBoost
- **Evaluation**: MAE, RMSE, R², actual-vs-predicted plots, residual analysis
- **Validation**: 5-fold cross-validation

#### Classification — Air Quality Category
- **Target**: 3-class label — Good (AQI ≤ 50), Moderate (51–100), Unhealthy (> 100)
- **Features**: temporal + geographic + all pollutant means
- **Models**: Random Forest Classifier, Gradient Boosting / XGBoost Classifier (with `class_weight="balanced"` for imbalance handling)
- **Evaluation**: accuracy, precision, recall, F1-score, confusion matrices

#### Feature Importance
- Tree-based feature importance (Gini impurity) for both regression and classification
- Pollutant correlation matrix revealing inter-pollutant relationships

#### Anomaly Detection
- Isolation Forest identifies ~2% of observations as anomalous
- Analysis of anomaly distribution by state, year, and season
- Visualizations: anomaly score distribution, NO₂ vs O₃ scatter with flagged anomalies

## Key Findings

- **Seasonal patterns**: Ozone peaks in summer months due to photochemical reactions; NO₂ and CO show higher concentrations in winter (heating, inversions)
- **Geographic variation**: Pollution levels vary significantly across states, with urban monitoring stations showing distinct profiles
- **Cross-pollutant relationships**: Negative correlation between O₃ and NO₂ in urban areas (NO titration effect); positive correlation between CO and NO₂ (shared combustion sources)
- **Model performance**: Tree-based ensemble models significantly outperform linear regression for pollutant concentration prediction
- **Anomalies**: Detected pollution spikes concentrated in specific states and years, potentially linked to industrial events, wildfires, or instrument issues

## Technologies Used

- **Python 3.x**
- **Data Processing**: pandas, NumPy, PyArrow
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: scikit-learn, XGBoost
- **Storage**: Apache Parquet
- **Environment**: Jupyter Notebook

## Getting Started

### Prerequisites

```bash
pip install pandas numpy pyarrow matplotlib seaborn plotly scikit-learn xgboost jupyter
```

### Running the Notebooks

1. Download the [US Pollution dataset from Kaggle](https://www.kaggle.com/datasets/sogun3/uspollution) and place the CSV in `data/raw/`
2. Run the notebooks **in order**:
   ```
   csv_to_parquet.ipynb → coordinates_to_dataset.ipynb → etl_eda.ipynb → ml_modeling.ipynb
   ```
3. Alternatively, if the cleaned Parquet file is already available, you can start directly from `etl_eda.ipynb` or `ml_modeling.ipynb`

## Future Work

- **Time-series forecasting** using LSTM / ARIMA / SARIMA for future pollutant predictions
- **Spatial interpolation** and heatmaps to estimate pollution in unmonitored areas
- **Hyperparameter optimization** with GridSearchCV or Optuna
- **Integration with meteorological data** (temperature, wind speed, humidity) to improve model accuracy
- **Interactive dashboard** for real-time air quality classification and alerts
- **Deep learning** approaches (spatio-temporal models) for combined geographic and temporal prediction

## References

- [US EPA Air Quality Index (AQI) Basics](https://www.airnow.gov/aqi/aqi-basics/)
- [US EPA AQI Breakpoint Tables](https://www.epa.gov/criteria-air-pollutants)
- US Pollution Dataset: [Kaggle](https://www.kaggle.com/datasets/sogun3/uspollution)

## Author

**YShutko** — [GitHub](https://github.com/YShutko/in_process_US_pollution_analysis)

## License

This project is for educational and analytical purposes. The dataset is publicly available on Kaggle.
