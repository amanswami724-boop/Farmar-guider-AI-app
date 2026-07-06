from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load crop recommendation models
crop_model = pickle.load(open('model/crop_recommendation_rf_model.pkl', 'rb')) 
crop_scaler = pickle.load(open('model/crop_recommendation_scaler.pkl', 'rb'))
crop_encoder = pickle.load(open('model/crop_recommendation_encoder.pkl', 'rb'))

# Load fertilizer recommendation models
fertilizer_model = pickle.load(open('model/fertilzer_recommandation_rf_model.pkl', 'rb'))
fertilizer_scaler = pickle.load(open('model/fertilizer_recommandation_scaler.pkl', 'rb'))
fertilizer_encoder = pickle.load(open('model/fertilizer_recommandation_encoder.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/crop')
def crop_page():
    return render_template('crop.html')


@app.route('/fertilizer')
def fertilizer_page():
    return render_template('fertilizer.html')


@app.route('/crop-predict', methods=['POST'])
def crop_predict():
    try:
        data = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]
        
        data = crop_scaler.transform(np.array(data).reshape(1, -1))
        prediction = crop_model.predict(data)
        predicted_crop = crop_encoder.inverse_transform(prediction)
        
        return render_template('result.html', prediction=predicted_crop[0], type='crop')
    except Exception as e:
        return render_template('result.html', error=str(e), type='crop')


@app.route('/fertilizer-predict', methods=['POST'])
def fertilizer_predict():
    try:
        data = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['moisture']),
            float(request.form['soil_type']),
            float(request.form['Urea'])
           
        ]
        
        data = fertilizer_scaler.transform(np.array(data).reshape(1, -1))
        prediction = fertilizer_model.predict(data)
        predicted_fertilizer = fertilizer_encoder.inverse_transform(prediction)
        
        return render_template('result.html', prediction=predicted_fertilizer[0], type='fertilizer')
    except Exception as e:
        return render_template('result.html', error=str(e), type='fertilizer')


if __name__ == '__main__':
    app.run(debug=True)   
    