patient_data_list = []          #Serhat Akbulut 2210356052
result_file_data = []

def save_file(line):
    """ this function is saving file"""
    file1 = open("doctors_aid_output.txt","w", encoding="utf-8")
    file1.writelines(line)
    file1.close()


def calculate_probability(patient):    
    """ this function is calculating probability"""
    accuracy = patient[1]
    count = patient[3].split('/')[0]
    total = patient[3].split('/')[1]
    probability = (float(accuracy)*int(count)) / (float(accuracy)*int(count) + (int(total)-int(count))*(1-float(accuracy))) * 100 
    return probability

def recommendation(line):
    """ this function is recommendation for patient"""
    result = False
    for patient in patient_data_list:
        if patient[0] == line[0]:
            result  = True
            probability = calculate_probability(patient)
            treatment_risk = float(patient[5]) * 100
            if probability >= treatment_risk:
                print("System suggests", patient[0], "to have the treatment")
            else:
                 print("System suggests", patient[0], "NOT to have the treatment")
            break
    if result == False:
        print("Recommendation for", line[0], "cannot be calculated due to absence")

def disease_probability(line):
    """ this function is return probability result """
    result = False
    for patient in patient_data_list:
        if patient[0] == line[0]:
            probability = calculate_probability(patient)
            print("Patient" , patient[0], "has a probability", probability, " of having", patient[2])
            result  = True
            break        
    if result == False:
        print('Probability for', line[0], 'cannot be calculated due to absence')

def listing(line):
    """ this function is listing patients"""
    print('work in progress list method')

def create_patient(line):
    """ this function is creating patient"""    
    result = ""
    if line in patient_data_list:
        result = " Patient " + line[0] + " already exists.\n"        
    else:                                              
        patient_data_list.append(line)  
        result = " Patient " + line[0] + " is recorded.\n"        
    
    result_file_data.append(result)

def remove_patient(line):    
    """ this function is removing patient"""  
    for patient in patient_data_list:
        if patient[0] == line[0]:
            patient_data_list.remove(patient)
            print("Patient", line[0], "is removed.")
            break
    else:
        print("Patient", line[0], "cannot be removed due to absence")
            

def read_file():
    """ this function is reading file"""
    with open('doctors_aid_inputs.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        main(lines)


def main(data):

    for line in data:                
        if line.startswith('create'):                     
            removed_command = line.replace('create ', '')
            splitted_line = removed_command.replace("\n", "").split(', ')  
            create_patient(splitted_line)            
        elif line.startswith('remove'):  
            removed_command = line.replace('remove ', '')             
            splitted_line = removed_command.replace("\n", "").split(', ')  
            remove_patient(splitted_line)
        elif line.startswith('list'):                  
            splitted_line = "list".replace("\n", "").split(', ') 
            listing(splitted_line)
        elif line.startswith('probability'):
            removed_command = line.replace('probability ', '')             
            splitted_line = removed_command.replace("\n", "").split(', ') 
            disease_probability(splitted_line)
        elif line.startswith('recommendation'):
            removed_command = line.replace('recommendation ', '')             
            splitted_line = removed_command.replace("\n", "").split(', ') 
            recommendation(splitted_line)    
    save_file(result_file_data)

read_file()
#Serhat Akbulut 2210356052

