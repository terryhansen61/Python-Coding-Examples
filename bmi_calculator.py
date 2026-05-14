# BMI Calculator

# Convert feet to meters
def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters * 0.3048

def bmi(weight, height_feet):
    return round(weight / (feet_to_meters(height_feet) ** 2), 2)

if __name__ == '__main__':
    weight = float(input('Enter weight (kg): '))
    height = float(input('Enter height (ft): '))
    BMI = bmi(weight, height)
    print('Your BMI is: ', BMI)
