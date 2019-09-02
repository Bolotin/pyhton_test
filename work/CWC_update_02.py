before = []
after = []

filename_before = 'CWC_before_02.txt'
filename_after = 'CWC_after.txt'


with open(filename_before) as file_before, open(filename_after) as file_after:
    for line in file_before:
        before.append(line.strip().split(',')[0])
    for line in file_after:
        after.append(line.strip().split(',')[0])

for device in before:
    if device not in after:
        print(device)
