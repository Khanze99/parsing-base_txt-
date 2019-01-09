import re

file_base = "base"
file_base_write = "result_parsing.txt"
input_file_base = open(file_base, mode='r', encoding='utf-8')
output_file_base = open(file_base_write, mode='w', encoding='utf-8')


lookfor = r"[\w.-]+@[A-Za-z-\d]+\.[\w.]+"  # (?!intel\.com) убрать из подстроки
lookfor_names = r""

text = input_file_base.read()
results = re.findall(lookfor, text)

for item in results:
    print(item)
    output_file_base.write(item +"\n")

print("Total - ", str(len(results)))

