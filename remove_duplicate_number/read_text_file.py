import datetime

input_file_path = 'sample.txt'  # Replace with your input file path

# Generate a unique output file name using a timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
output_file_path = f'output_{timestamp}.txt'

unique_numbers = set()

with open(input_file_path, 'r') as input_file:
    for line in input_file:
        numbers = line.strip().split(',')
        for num in numbers:
            unique_numbers.add(int(num))

with open(output_file_path, 'w') as output_file:
    output_file.write(','.join(map(str, unique_numbers)))

print("Output saved to:", output_file_path)
