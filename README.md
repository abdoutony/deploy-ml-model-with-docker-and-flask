## Deploying ML Model using Flask

This is a simple project to elaborate how to deploy a Machine Learning model using Flask API

### Prerequisites

You need to have Docker installed

### Project Structure

This project has four major parts :

1. src/modles/code - This Directory contains machine learning models training functions.
2. src/app.py - This project entry file contains Flask app that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. src/templates - This folder contains the HTML template (index.html) to allow user to enter employee detail and displays the predicted employee salary.
4. src/static - This folder contains the css folder with style.css file which has the styling required for out index.html file.

### Running the project

1. Ensure that you are in the project home directory Create the machine learning model by running below command from command prompt -

```
python src/models/model.py
```

This would create a serialized version of our model into a file model.joblib

2. Run app.py using below command to start Flask API

```
python src/app.py
```

By default, flask will run on port 5000.

3. Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

You should be able to view the homepage.

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should be able to see the predcited salary vaule on the HTML page!
check the output here: http://127.0.0.1:5000/predict
