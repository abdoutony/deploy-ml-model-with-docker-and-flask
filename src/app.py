import numpy as np
from flask import Flask, request, jsonify, render_template
import os
import joblib

app = Flask(__name__,template_folder='templates') #Initialize the flask App




@app.route('/')
def home():
    """
    A function to handle the home route.

    Returns:
        str: The rendered template for the index.html.
    """
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Endpoint for predicting employee salary based on input form data.

    Args:
        None

    Returns:
        str: HTML rendering of the index.html template with the predicted salary displayed.

    '''
    # load saved model from disk
    model_output_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'models',"output"))
    model_output_file =  os.path.join(model_output_directory, 'model.joblib')
    model = joblib.load(model_output_file)
    # Extract the integer features from the form values
    int_features = [int(x) for x in request.form.values()]

    # Create a numpy array from the integer features
    array_features = [np.array(int_features)]

    # Use the model to make a prediction based on the final features
    prediction = model.predict(array_features)

    # Round the prediction to 2 decimal places
    result = round(prediction[0], 2)

    # Render the index.html template with the predicted salary displayed
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(result))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)