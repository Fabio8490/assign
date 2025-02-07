import sys
import os

# Function to read data from a file
def read_input_file(file_path):
    """
    Reads numeric data from the input file.
    Each line in the file should contain a single number.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        with open(file_path, 'r') as file:
            data = [float(line.strip()) for line in file if line.strip()]
            if len(data) < 3:
                raise ValueError("Input file must contain at least three data values.")
            return data
    except ValueError as e:
        raise ValueError(f"Error reading file '{file_path}': {e}")

#  calculations on the input data
def perform_calculations(data):
    """
    Perform two calculations: average and sum of the data.
    """
    data_sum = sum(data)
    data_average = data_sum / len(data)
    return data_sum, data_average

# Write the results to an output file
def write_output_file(file_path, data_sum, data_average):
    """
    Writes the calculation results to an output file.
    """
    with open(file_path, 'w') as file:
        file.write(f"Sum of data: {data_sum}\n")
        file.write(f"Average of data: {data_average}\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python data_processing.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
       
        data = read_input_file(input_file)
        #  calculations
        data_sum, data_average = perform_calculations(data)
        
        write_output_file(output_file, data_sum, data_average)
        print(f"Results successfully written to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
