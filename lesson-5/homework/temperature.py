#1
def convert_cel_to_far(celsius):
    fahrenheit = celsius*9/5+32
    fahrenheit = round(fahrenheit,2)
    return fahrenheit
#2
def convert_far_to_cel(fahrenheit):
    celsius = (fahrenheit-32)*5/9
    celsius = round(celsius, 2)
    return celsius

far = float(input("Enter a temperature in degrees F: "))
print(f"{far} degrees F = {convert_far_to_cel(far)} degrees C")
cel = float(input("Enter a temperature in degrees C: "))
print(f"{cel} degrees F = {convert_cel_to_far(cel)} degrees F")