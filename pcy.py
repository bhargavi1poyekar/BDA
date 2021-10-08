# importing libraries
import random
import numpy
import pandas as pd
import csv
from itertools import combinations

file_name = input("Enter the csv file name:")
# getting input values from csv file
with open(file_name, mode='r') as file:
    csv_reader = csv.reader(file)  # generating the reader
    l_count = 0  # initializing line count to 0
    trans = []  # array for measurement values
    for row in csv_reader:  # taking a row at a time
        trans.append(row)  # append to transactions
        l_count += 1  # increment line count

trans = [list(map(int, i)) for i in trans]
no_trans = len(trans)
len_trans = len(trans[0])

items = []
for i in range(no_trans):
    for j in range(len_trans):
        items.append(trans[i][j])

set_items = list(set(items))

counts = [0 for i in range(len(set_items))]
for i in range(len(set_items)):
    counts[i] = items.count(set_items[i])

s_count = int(input("\nEnter the support count: "))

freq_items = []
for i in range(len(counts)):
    if counts[i] >= s_count:
        freq_items.append(set_items[i])

print(f'freq_items: {freq_items}')

combo = []
for i in range(no_trans):
    item_list = []
    for j in range(len_trans):
        if trans[i][j] in freq_items:
            item_list.append(trans[i][j])
    combo.append(list(combinations(item_list, 2)))

combo_items = []
for i in range(len(combo)):
    for j in range(len(combo[i])):
        combo_items.append(combo[i][j])

set_combo = [t for t in (set(tuple(i) for i in combo_items))]

counts_combo = [0 for i in range(len(set_combo))]
for i in range(len(set_combo)):
    counts_combo[i] = combo_items.count(set_combo[i])

freq_combo = []
for i in range(len(counts_combo)):
    if counts_combo[i] >= s_count:
        freq_combo.append(list(set_combo[i]))

print(f'freq_combinations: {freq_combo}')

n_buckets = 4
buckets = [[]for i in range(4)]
bitmap_bucket = [0 for i in range(n_buckets)]
count_bucket = [0 for i in range(n_buckets)]

for i in range(len(freq_combo)):
    if (freq_combo[i][0]*freq_combo[i][1]) % 4 == 0:
        buckets[0].append(freq_combo[i])
        count_bucket[0] += 1
    elif (freq_combo[i][0]*freq_combo[i][1]) % 4 == 1:
        buckets[1].append(freq_combo[i])
        count_bucket[1] += 1
    elif (freq_combo[i][0]*freq_combo[i][1]) % 4 == 2:
        buckets[2].append(freq_combo[i])
        count_bucket[2] += 1
    elif (freq_combo[i][0]*freq_combo[i][1]) % 4 == 3:
        buckets[3].append(freq_combo[i])
        count_bucket[3] += 1

print(f'Buckets: {buckets}')
print(f'Bucket Count: {count_bucket}')

freq_itemsets = []
for i in range(4):
    if count_bucket[i] >= s_count:
        bitmap_bucket[i] = 1
        freq_itemsets.append(buckets[i])

print(f'bitmap_bucket: {bitmap_bucket}')
frequent_itemsets = [j for sub in freq_itemsets for j in sub]
print(f'frequent_itemsets: {frequent_itemsets}')
