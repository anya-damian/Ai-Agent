from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

def student_result(attendance, study_hours, sleep_hours):
    if attendance < 75:
        return "FAIL"
    else:
        if study_hours >= 4 and sleep_hours >= 6:
            return "PASS"
        else:
            return "FAIL"

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    attendance = data.get('attendance')
    study_hours = data.get('study_hours')
    sleep_hours = data.get('sleep_hours')

    result = student_result(attendance, study_hours, sleep_hours)

    return jsonify({
        "prediction": result,
        "message": f"Based on your inputs, the result is {result}"
    })

if __name__ == '__main__':
    app.run(debug=True)
