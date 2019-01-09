import re

file_base = "base"
file_base_write = "result_parsing.txt"
input_file_base = open(file_base, mode='r', encoding='utf-8')
output_file_base = open(file_base_write, mode='w', encoding='utf-8')


look_for = r"[\w.-]+@[A-Za-z-\d]+\.[\w.]+"  # (?!intel\.com) убрать из подстроки
look_for_names_and_city = r"(?![A-Z][a-z]+@)[A-Z][\w-]+@?"

text = input_file_base.read()
results = re.findall(look_for, text)
results_names_city = re.findall(look_for_names_and_city, text)

for item in results:
    print(item)
    output_file_base.write(item + "\n")

for item in results_names_city:
    print(item)

print("Total - ", str(len(results)))

