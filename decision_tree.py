def student_result(attendance, study_hours, sleep_hours):
    if attendance < 75:
        return "FAIL"
    else:
        if study_hours >= 4 and sleep_hours >= 6:
            return "PASS"
        else:
            return "FAIL"


if __name__ == "__main__":
    
    attendance = float(input("Enter attendance (%): "))
    study_hours = float(input("Enter study hours per day: "))
    sleep_hours = float(input("Enter sleep hours: "))

    result = student_result(attendance, study_hours, sleep_hours)
    print("Result:", result)
