
try:
  with open('myfile.txt') as fh:
    file_data = fh.read()
  print(file_data)
#except FileNotFoundError:
#  print('File Missing...')
except PermissionError:
  print('This is not allowed...')
except Exception as err:
  print('Some other error ocurred:', str(err))
