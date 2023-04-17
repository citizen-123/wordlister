#!/usr/bin/env python3

import sys
import multiprocessing as mp
from tqdm import tqdm
import re

def combine_lines(line1, file2, output, remove_symbols, remove_numbers, make_lowercase):
    with open(file2) as f2, open(output, 'a') as out:
        for line2 in f2:
            combined = line1.strip() + line2.strip()

            if remove_symbols:
                # Remove all non-alphanumeric characters from the string
                combined = re.sub('[^0-9a-zA-Z]+', '', combined)

            if remove_numbers:
                # Remove all digits from the string
                combined = re.sub('[0-9]+', '', combined)

            if make_lowercase:
                # Convert the string to lowercase
                combined = combined.lower()

            out.write(combined + '\n')

if __name__ == '__main__':
    if len(sys.argv) < 4 or '-h' in sys.argv:
        print("Usage: combine_wordlists.py [-ns] [-nn] [-l] file1.txt file2.txt output.txt\n")
        print("Options:")
        print("-ns      Remove all symbols from the output")
        print("-nn      Remove all numbers from the output")
        print("-l       Make everything in the output lowercase")
        print("-h       Show this help menu")
        sys.exit()

    # Parse command-line arguments
    args = sys.argv[1:]
    remove_symbols = '-ns' in args
    remove_numbers = '-nn' in args
    make_lowercase = '-l' in args
    file1, file2, output = [arg for arg in args if arg not in ('-ns', '-nn', '-l', '-h')][0:3]

    # Count the number of lines in each file
    with open(file1) as f1:
        num_lines1 = sum(1 for _ in f1)
    with open(file2) as f2:
        num_lines2 = sum(1 for _ in f2)

    # Determine the total number of combinations
    total_combinations = num_lines1 * num_lines2

    # Get the maximum number of threads available on the system
    max_threads = mp.cpu_count()

    # Prompt the user for the number of threads to use
    num_threads = int(input(f"How many threads do you want to use (up to {max_threads})? "))

    # Check that the number of threads is not greater than the maximum
    if num_threads > max_threads:
        print(f"Error: the maximum number of threads available on this system is {max_threads}")
        sys.exit(1)

    print(f"Combining {file1} and {file2} into {output} using {num_threads} threads...")

    # Initialize the process pool and start the combination process
    with mp.Pool(num_threads) as pool, tqdm(total=total_combinations) as pbar:
        for line1 in open(file1):
            pool.apply_async(combine_lines, args=(line1, file2, output, remove_symbols, remove_numbers, make_lowercase), callback=lambda _: pbar.update(num_lines2))

        # Wait for all processes to finish before exiting
        pool.close()
        pool.join()

    print(f"Successfully combined {file1} and {file2} into {output}")
