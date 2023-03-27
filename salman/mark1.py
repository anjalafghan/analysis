import pandas as pandas

data_file = pandas.read_excel(r'~/Downloads/MainSheet.xlsx')
print(data_file)

skill = data_file[data_file["Skill"] == "CSAT"]

print(skill)


