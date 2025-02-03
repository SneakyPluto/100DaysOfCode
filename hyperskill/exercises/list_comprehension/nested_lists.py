school = [["Mary", "Jack", "Tiffany"], 
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]

student_list = []
for class_group in school: # (nested lists)["Mary", "Jack", "Tiffany"]..
    for student in class_group: #Elements within each list
        student_list.append(student) #Appending each elements into student_list
print(student_list)
