#This is the updated version of my Curve Calculator program

#curve Calculator
def Curve_Calculator():
    First_input = input("Inches of curvature or Feet or Miles?: ")
    if First_input.lower() == "inches":
        num1 = float(input("Distance in miles: "))
        Expected_curve_inches = 8 * (num1**2)
        print("Expected Curve: " + str(Expected_curve_inches) + " Inches")
    if First_input.lower() == "feet":
        num1 = float(input("Distance in miles: "))
        Expected_curve_feet = (8 * (num1**2)) / 12
        print("Expected Curve: " + str(Expected_curve_feet) + " Feet")
    if First_input.lower() == "miles":
        num1 = float(input("Distance in miles: "))
        Expected_curve_miles = ((8 * (num1**2)) / 12) / 5280
        print("Expected Curve: " + str(Expected_curve_miles) + " Miles")
        
        
def Missing_Blockage():
    First_input = input("In Inches, Feet or Miles of Blockage?: ")
    if First_input.lower() == "inches":
        distance = float(input("Distance in miles: "))
        height = input("Height of object in feet: ")
        elevation = input("Elevation in feet: ")
        height = float(height) * 12
        elevation = float(elevation) * 12
        true_height = float(elevation) + float(height)
        Expected_curve_inches = 8 * (distance**2)
        Missing_blockage = (Expected_curve_inches) - float(true_height)
        print("Missing Blockage: " + str(Missing_blockage) + " Inches")
    if First_input.lower() == "feet":
        distance = float(input("Distance in miles: "))
        height = float(input("Height of object in feet: "))
        elevation = input("Elevation in feet: ")
        Expected_curve_feet = (8 * (distance**2)) / 12
        true_height = float(elevation) + float(height)
        Missing_blockage = Expected_curve_feet - float(true_height)
        print("Missing Blockage: " + str(Missing_blockage) + " Feet")
    if First_input.lower() == "miles":
        distance = float(input("Distance in miles: "))
        height = float(input("Height in feet: "))
        elevation = input("Elevation in feet")
        Expected_curve_miles = ((8 * (distance**2)) / 12) / 5280
        true_height = float(elevation) + float(height)
        Missing_blockage = Expected_curve_miles - float(true_height / 5280)
        print("Missing Blockage: " + str(Missing_blockage) + " Miles")
        
        
question = input("What would you like to find out? Curvature or Missing Blockage?: ")
if question.lower() == "curvature":
    Curve_Calculator()
if question.lower() == "missing blockage":
    Missing_Blockage()