def calculate_bmi(weight_kg, height_m):
    """
    Calculates BMI given weight in kilograms and height in meters.
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi_result:.2f}")
