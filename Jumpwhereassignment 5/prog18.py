
sample_string = "32.054,23"

swapped_string = sample_string.replace(',', '|').replace('.', ',').replace('|', '.')
print(swapped_string)
