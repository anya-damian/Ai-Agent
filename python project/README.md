# Smart Student Decision System

## Overview
This project implements a deterministic decision tree to predict student performance (PASS/FAIL).

## Features
- Rule-based decision system
- Flask API for AI interaction
- Deterministic outputs (no randomness)

## Decision Logic
- Attendance < 75 → FAIL
- Else:
    - Study ≥ 4 and Sleep ≥ 6 → PASS
    - Else → FAIL

## How to Run
pip install -r requirements.txt
python app.py

## API Endpoint
POST /predict

## Example Input
{
  "attendance": 80,
  "study_hours": 5,
  "sleep_hours": 7
}
