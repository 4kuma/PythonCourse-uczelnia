import os, sys

file_path = os.getcwd() + "\\" + sys.argv[1]
print(f'Liczba bajtów: {os.path.getsize(file_path)}')
with open(sys.argv[1], 'r') as input_file:
    data = input_file.read()

print(f'Liczba słów: {len(data.split())}')
print(f'Liczba linii: {len(data.splitlines())}')
print(f'Maksymalna długość linii: {max([len(i) for i in data.splitlines()])}')
