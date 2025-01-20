import operator

student_list = {
    "English": ['Tim', 'Carl', 'Dean', 'Jane'],
    "Maths": ['Jane', 'Mike', 'Ann', 'Kate', 'Nick', 'Jenny'],
    "Chemistry": ['Tim', 'Carl', 'Dean']
}

# Not a good practice to sort a dictionary. Only allowable because its Python
student_list_by_count = dict(sorted(student_list.items(), key=operator.itemgetter(0)))
print(max(student_list_by_count, key=student_list_by_count.get))

print(student_list.keys())
