import csv



def read_subjects(filename: str):
    
    list_of_averages = []
    with open(filename, "r") as file:
        
        reader = csv.reader(file)
        subjects = [x[1] for x in reader[1:]]
        unique_subjects = set(subjects)
        
        for subject in unique_subjects:
            
            total=sum([int(row[2]) for row in reader if row[1]==subject])
            list_of_averages.append([subject, total/subjects.count(subject)])
    return list_of_averages
