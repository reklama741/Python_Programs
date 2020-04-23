from sys import argv, exit
import pandas as pd
import csv

if len(argv) != 3:
    print("Usage ./dna.py argument argument")
    exit(1)
else:
    with open(argv[1], 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open(argv[2], 'r') as dna_text_file:
            dna_reader = dna_text_file.read().rstrip("\n").upper()
            dna_list = ["AGATC", "TTTTTTCT", "AATG", "TCTAG", "GATA", "TATC", "GAAA", "TCTG"]
            dna_str = [0, 0, 0, 0, 0, 0, 0, 0]
            what_is_what_list = []

            n = 1
            counter = 0
            for dna in range(0, 8):
                n = 1
                counter = 0
                i = 0
                while i < len(dna_reader):
                    if dna_list[dna] == dna_reader[i:i+len(dna_list[dna])]:
                        counter += 1
                        n = len(dna_list[dna])
                    else:
                        if counter > dna_str[dna]:
                            dna_str[dna] = counter
                            counter = 0
                            n = 1
                        else:
                            counter = 0
                            n = 1
                    i += n
            line_count = 0
            for row in csv_reader:
                x = True
                if line_count == 0:
                    what_is_what_list = row
                    line_count += 1
                else:
                    for i in range(1, len(what_is_what_list)):
                        for y in range(0, 8):
                            if what_is_what_list[i] == dna_list[y]:
                                if dna_str[y] != int(row[i]):
                                    x = False
                if x == True and row[0] != 'name':
                    print(row[0])
            if x == False:
                print("No match")