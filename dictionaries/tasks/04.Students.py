students_list={}

text = input()
while True:
    info = text.split(":")
    if len(info)<2:
        break
    name = info[0]
    ID = info[1]
    course = info[2]
    if course not in students_list:
        students_list[course]={}
    students_list[course][name]=ID
    text=input

course = " ".join(text.split("_"))

for key, value in students_list.items():
    if key == course:
        for sub_key,sub_value in value.items():
            print(f"{sub_key} - {sub_value}")