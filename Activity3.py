def test(list):
    result={}
    for item in list:
        result[item[0]]=item[1:]
    return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print(f"Orignal list was {students}")
print(f"Converted list to dictionary is {test(students)}")