# Wordlister
## Combine multiple wordlists into a single wordlist.


This is a Python script that can be used to generate a wordlist from two .txt files. The resulting wordlist will contain every combination of words between the two files.

# Usage

To use the script, simply run the wordlister.py script in your terminal, followed by the two filenames you wish to combine and the name of the output file.

```
./wordlister.py input1.txt input2.txt output.txt
```

This will generate a wordlist that contains every combination of words between input1.txt and input2.txt. The resulting wordlist will be saved to output.txt.

# Options

The script also includes several options that can be used to modify the output of the wordlist.

## -ns

This option removes all symbols from the output. To use it, simply add -ns to the beginning of the command:

```
./wordlister.py -ns input1.txt input2.txt output.txt 
```

## -l

This option makes everything in the output lowercase. To use it, simply add -l to the beginning of the command:

```
./wordlister.py -l input1.txt input2.txt output.txt
```

## -nn

This option removes all numbers from the output. To use it, simply add -nn to the beginning of the command:

```
./wordlister.py -nn input1.txt input2.txt output.txt
```

## -h

To view a list of all available options and their descriptions, simply add -h to the beginning of the command:

```
./wordlister.py -h 
```

# Examples

Here are a few examples of how to use the script:

```
./wordlister.py input1.txt input2.txt output.txt
```

This will generate a wordlist that contains every combination of words between input1.txt and input2.txt and save it to a file called output.txt.

```
./wordlister.py -ns -l input1.txt input2.txt output.txt
```

This will generate a wordlist that contains every combination of words between input1.txt and input2.txt, remove all symbols, and convert the output to lowercase. The resulting wordlist will be saved to a file called output.txt.
