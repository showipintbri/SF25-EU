import csv

with open('coords.csv', newline='') as infile:
    reader = csv.reader(infile)
    rows = [row for row in reader if row]  # skip empty rows

# If the first line is a header:
header = None
if rows and not rows[0][0].isdigit():  # simple check for header row
    header = rows.pop(0)

# Sort by first column (convert to int safely)
rows.sort(key=lambda row: int(row[0]))

with open('sorted.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    if header:
        writer.writerow(header)
    writer.writerows(rows)

