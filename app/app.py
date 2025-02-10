from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the machine learning model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Map numeric predictions to flower names
flower_names = {0: 'Iris Setosa', 1: 'Iris Versicolor', 2: 'Iris Virginica'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    try:
        features = [float(x) for x in request.form.values()]
        # Make predictions using the model
        prediction = model.predict([features])
        result = flower_names.get(prediction[0], "Unknown flower")  # Map to flower name
    except ValueError:
        result = "Invalid input. Please enter numeric values."

    return render_template('result.html', prediction=result)  # Pass the result (flower name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5053)
