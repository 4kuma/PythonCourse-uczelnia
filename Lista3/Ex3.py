def last_column(filename):
    with open(filename, 'r') as input_file:
        print(f'Całkowita liczba bajtów: {sum(int(line.split(" ")[-1]) for line in input_file)}')