import pandas as pd

file_name = input("Enter csv file name: ")
info_data = pd.read_csv(file_name)

output_file_name = input("Enter json file name: ")
info_data.to_json(output_file_name, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

print('json file created successfully...')