# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 08:54:44 2024

@author: PaganM
"""



class bmifunction:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
        
        self.bmi_result = None
        
        
    def bmi_calculator(self):
        pounds_to_kilograms = self.weight / 2.205
        inches_to_meters = self.height*0.0254
        height_squared = inches_to_meters**2
        bmi = (pounds_to_kilograms/height_squared) 
        if bmi < 18.5:
            return ('Underweight. \nCurrent BMI is: \n' + str(bmi))
        elif bmi >= 18.5 and bmi <= 24.9:
            return ('Normal. \nCurrent BMI is: \n' + str(bmi))
        elif bmi >= 25 and bmi <= 29.9:
            return ('Overweight. \nCurrent BMI is: \n' + str(bmi))
        elif bmi >= 30 and bmi <= 34.9:
            return ('Obese. \nCurrent BMI is: \n' + str(bmi))
        elif bmi >= 35:
            return ('Extremely Obese. \nCurrent BMI is: \n' + str(bmi))
        else:
            return ('Not working.')


           
    def runbmi(self):
        '''
        self.bmi_calculator()
        '''
        
        self.bmi_result = self.bmi_calculator()