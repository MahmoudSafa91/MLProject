def preprocess_age (AGE):
        if AGE in range (16,25):
            return [0,0,0]
        elif AGE in range (26,39):
            return [1,0,0]
        elif AGE in range (40,64):
            return [0,1,0]
        else:
            return [0,0,1]
        
        
def preprocess_experience (DRIVING_EXPERIENCE):
    if DRIVING_EXPERIENCE in range (0,9):
        return [0,0,0]
    elif DRIVING_EXPERIENCE in range (10,19):
        return [1,0,0]
    elif DRIVING_EXPERIENCE in range (20,29):
        return [0,1,0]
    else:
        return [0,0,1]
    
    
def preprocess_education (EDUCATION):
    if EDUCATION.lower == 'none':
        return [1,0]
    elif EDUCATION.lower == 'university':
        return [0,1]
    else:
        return [0,0]
    
def preprocess_income(INCOME):
    if  INCOME. lower == 'poverty':
        return [1,0,0]
    elif INCOME. lower == 'upper class':
        return [0,1,0]
    elif INCOME. lower == ' working class ':
        return [0,0,1]
    else:
        return [0,0,0]
    

def preprocess_data(data):
    
    CREDIT_SCORE = data ['score']
    VEHICLE_OWNERSHIP = data ['ownership']
    ANNUAL_MILEAGE = data ['mileage']
    SPEEDING_VIOLATIONS = data ['violations']
    PAST_ACCIDENTS = data ['accidents']
    
    AGE = preprocess_age(data['AGE'])
    DRIVING_EXPERIENCE = preprocess_experience(data['DRIVING_EXPERIENCE'])
    EDUCATION =  preprocess_education(data['EDUCATION'])
    INCOME = preprocess_income (data['INCOME'])
    final_data = [ CREDIT_SCORE, VEHICLE_OWNERSHIP, ANNUAL_MILEAGE, SPEEDING_VIOLATIONS, PAST_ACCIDENTS]+ AGE + DRIVING_EXPERIENCE + EDUCATION + INCOME  
    return final_data 