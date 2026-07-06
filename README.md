# Farmer Guider AI

A Flask-based web application that helps farmers with crop recommendation and fertilizer recommendation using machine learning models.

## Overview

`Farmer_Guider_AI` provides two prediction tools:

- **Crop Prediction**: Recommends the best crop to grow based on soil nutrients and weather conditions.
- **Fertilizer Recommendation**: Suggests a fertilizer based on soil nutrient levels, moisture, temperature, humidity, soil type, and urea input.

The application uses pre-trained sklearn models loaded from the `model/` directory.

## Features

- Easy-to-use Flask web interface
- Crop recommendation based on N, P, K, temperature, humidity, pH, and rainfall
- Fertilizer recommendation based on N, P, K, temperature, humidity, moisture, soil type, and urea
- Responsive HTML templates for navigation and results

## Tech Stack

- Python
- Flask
- NumPy
- scikit-learn
- HTML/CSS

## Repository Structure

- `app.py` - Main Flask application
- `requirements.txt` - Python dependency list
- `run_app.bat` - Windows batch file to launch the app
- `templates/` - HTML pages for home, crop prediction, fertilizer prediction, and results
- `static/` - CSS files
- `datasets/` - Raw datasets used for training
- `model/` - Pre-trained model and preprocessing objects

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

> Note: `pickle` is included in `requirements.txt`, but it is also part of the Python standard library.

## Running the App

From the project folder, run:

```bash
python app.py
```

Or use the Windows batch file:

```bash
run_app.bat
```

Then open the browser at:

```text
http://127.0.0.1:5000/
```

## Usage

### Crop Prediction

Navigate to the Crop Prediction page and enter:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH level
- Rainfall (mm)

### Fertilizer Recommendation

Navigate to the Fertilizer Recommendation page and enter:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil moisture (%)
- Soil type (numeric code)
- Urea (kg/ha)

## Model Files

The application expects the following files under `model/`:

- `crop_recommendation_rf_model.pkl`
- `crop_recommendation_scaler.pkl`
- `crop_recommendation_encoder.pkl`
- `fertilzer_recommandation_rf_model.pkl`
- `fertilizer_recommandation_scaler.pkl`
- `fertilizer_recommandation_encoder.pkl`

## Notes

- Make sure the required model files are present in the `model/` folder before starting the app.
- If you encounter input or prediction errors, check that all form values are provided and valid numbers.

## License

This project is provided as-is for educational use and experimentation.
