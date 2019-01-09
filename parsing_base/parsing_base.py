import re

file_base = "base"
file_base_write = "result_parsing.txt"
input_file_base = open(file_base, mode='r', encoding='utf-8')
output_file_base = open(file_base_write, mode='w', encoding='utf-8')


lookfor = r"[\w.-]+@[A-Za-z-\d]+\.[\w.]+"

text = input_file_base.read()
results = re.findall(lookfor, text)

for item in results:
    print(item)

print("Total - ", str(len(results)))

