from flask import Flask, request, render_template
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('multiple.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract and convert form values to integers
        area = int(request.form['area'])
        bathrooms = int(request.form['bathrooms'])
        stories = int(request.form['stories'])
        airconditioning = int(request.form['airconditioning'])
        prefarea = int(request.form['prefarea'])

        # Add constant term (like statsmodels does)
        input_data = [1, area, bathrooms, stories, airconditioning, prefarea]

        # Prediction
        predicted_price = model.predict([input_data])[0]

        return render_template('index.html', prediction_text=f'🏠 Predicted House Price: {round(predicted_price, 2)}')

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=9000)
