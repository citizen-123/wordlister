# Wordlister
## Combine multiple wordlists into a single wordlist.


This is a Python script that can be used to clean a single wordlist, removing symbols, numbers, spaces, and converting the case to lowercase. Or to generate a wordlist from two .txt files. The resulting wordlist will contain every combination of words between the two files. 

# Usage

By default the script is setup to combine two files into one. If you only want to modify a single file, check the section for the -c option below. To use the script, simply run the wordlister.py script in your terminal, followed by the two filenames you wish to combine and the name of the output file.

```
Python3 wordlister.py input1.txt input2.txt output.txt
```

This will generate a wordlist that contains every combination of words between input1.txt and input2.txt. The resulting wordlist will be saved to output.txt.

# Options

The script also includes several options that can be used to modify the output of the wordlist.

## -c

The `-c` option is used to modify a single input file according to the provided options, rather than combining two files. The cleaned, modified output will be saved in the specified output file. This option can be used in combination with the `-ns`, `-nn`, and `-l` options to remove symbols, remove numbers, and make everything lowercase, respectively.

To use this option, simply add `-c` to the beginning of the command:

```
Python3 wordlister.py -c input.txt output.txt
```

This will clean the input.txt file and save the cleaned file as output.txt.

If you wish to remove symbols, remove numbers, and convert everything to lowercase, you can combine these options with `-c`:

```
Python3 wordlister.py -c -ns -nn -l input.txt output.txt
```

This will clean the input.txt file by removing symbols, removing numbers, and converting everything to lowercase. The resulting cleaned file will be saved to output.txt.

# Examples with `-c`

Here are a few examples of how to use the script with the `-c` option:

```
Python3 wordlister.py -c input.txt output.txt
```

This will clean the input.txt file and save the cleaned file as output.txt.

```
Python3 wordlister.py -c -ns input.txt output.txt
```

This will clean the input.txt file, remove all symbols, and save the cleaned file as output.txt.

```
Python3 wordlister.py -c -ns -l input.txt output.txt
```

This will clean the input.txt file, remove all symbols, convert everything to lowercase, and save the cleaned file as output.txt.

```
Python3 wordlister.py -c -ns -nn -l input.txt output.txt
```

This will clean the input.txt file by removing symbols, removing numbers, and converting everything to lowercase. The resulting cleaned file will be saved to output.txt.


## -ns

This option removes all symbols from the output. To use it, simply add -ns to the beginning of the command:

```
Python3 wordlister.py -ns input1.txt input2.txt output.txt 
```

## -l

This option makes everything in the output lowercase. To use it, simply add -l to the beginning of the command:

```
Python3 wordlister.py -l input1.txt input2.txt output.txt
```

## -nn

This option removes all numbers from the output. To use it, simply add -nn to the beginning of the command:

```
Python3 wordlister.py -nn input1.txt input2.txt output.txt
```

## -h

To view a list of all available options and their descriptions, simply add -h to the beginning of the command:

```
Python3 wordlister.py -h 
```

# Examples

Here are a few examples of how to use the script:

```
Python3 wordlister.py input1.txt input2.txt output.txt
```

This will generate a wordlist that contains every combination of words between input1.txt and input2.txt and save it to a file called output.txt.

```
Python3 wordlister.py -ns -l input1.txt input2.txt output.txt
```

This will generate a wordlist that contains every combination of words between input1.txt and input2.txt, remove all symbols, and convert the output to lowercase. The resulting wordlist will be saved to a file called output.txt.
