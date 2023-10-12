import numpy as np
import joblib
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load("final_score.pkl")


inspirational_messages = [
    "Study hard",
    "Work hard",
    "Aim high",
    "Your dreams are worth it",
    "Good luck"
]




@app.route('/')
def hp():
    return render_template('index.html', inspirational_messages=inspirational_messages)

@app.route('/predict', methods=['POST'])
def predict():


    try:
        study_hours = float(request.form['studyHours'])
        if study_hours < 0 or study_hours > 24:
            raise ValueError("Study hours must be between 0 and 24.")
        prediction = model.predict([[study_hours]])[0].round(2)

        # Create a pyramid of inspirational messages
        pyramid_messages = []
        for message in inspirational_messages:
            pyramid_messages.append(f'"{message}"')

        # Concatenate all inspirational messages with line breaks
        formatted_messages = '\n'.join(pyramid_messages)
    


        return render_template('index.html', prediction_text=f'You Will get {prediction}% marks when you study {study_hours} hours per day.\n\n{formatted_messages}')
    
    
    except ValueError as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)



    
 

