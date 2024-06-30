def calculate_bmi(weight_kg, height_m):
    """
    Calculates BMI given weight in kilograms and height in meters.
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi_value):
    """
    Interprets BMI value and provides context.
    """
    if bmi_value < 18.5:
        return "Your BMI is too low. Consider gaining weight."
    elif 18.5 <= bmi_value < 24.9:
        return "Your BMI is within a healthy range. Great job!"
    elif 25 <= bmi_value < 29.9:
        return "Your BMI is slightly high. Consider maintaining or losing weight."
    else:
        return "Your BMI is too high. Consider losing weight for better health."

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi_result)

print(f"Your BMI is: {bmi_result:.2f}")
print(interpretation)
