#!/usr/bin/env python3

import sys
import multiprocessing as mp
import re

def modify_line(line, output, remove_symbols, remove_numbers, make_lowercase):
    modified = line.strip()

    if remove_symbols:
        # Remove all non-alphanumeric characters from the string
        modified = re.sub('[^0-9a-zA-Z]+', '', modified)

    if remove_numbers:
        # Remove all digits from the string
        modified = re.sub('[0-9]+', '', modified)

    if make_lowercase:
        # Convert the string to lowercase
        modified = modified.lower()

    with open(output, 'a') as out:
        out.write(modified + '\n')

if __name__ == '__main__':
    if len(sys.argv) < 3 or '-h' in sys.argv:
        print("Usage: combine_wordlists.py [-c] [-ns] [-nn] [-l] input.txt output.txt\n")
        print("Options:")
        print("-c       Clean the input file according to the provided options and output the modified file")
        print("-ns      Remove all symbols from the output")
        print("-nn      Remove all numbers from the output")
        print("-l       Make everything in the output lowercase")
        print("-h       Show this help menu")
        sys.exit()

    # Parse command-line arguments
    args = sys.argv[1:]
    clean_mode = '-c' in args
    remove_symbols = '-ns' in args
    remove_numbers = '-nn' in args
    make_lowercase = '-l' in args
    input_file, output_file = [arg for arg in args if arg not in ('-c', '-ns', '-nn', '-l', '-h')][0:2]

    if clean_mode:
        # Count the number of lines in the file
        with open(input_file) as f:
            num_lines = sum(1 for _ in f)

        # Get the maximum number of threads available on the system
        max_threads = mp.cpu_count()

        # Prompt the user for the number of threads to use
        num_threads = int(input(f"How many threads do you want to use (up to {max_threads})? "))

        # Check that the number of threads is not greater than the maximum
        if num_threads > max_threads:
            print(f"Error: the maximum number of threads available on this system is {max_threads}")
            sys.exit(1)

        print(f"Cleaning {input_file} into {output_file} using {num_threads} threads...")

        # Initialize the process pool and start the cleaning process
        with mp.Pool(num_threads) as pool:
            for line in open(input_file):
                pool.apply_async(modify_line, args=(line, output_file, remove_symbols, remove_numbers, make_lowercase))

            # Wait for all processes to finish before exiting
            pool.close()
            pool.join()

        print(f"Successfully cleaned {input_file} into {output_file}")
    else:
        print("No cleaning option selected. Please provide '-c' for cleaning.")
