import csv
dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
with open("week9/products.csv", "rt") as csv_file:

    # Use the csv module to create a reader object
    # that will read from the opened CSV file.
    reader = csv.reader(csv_file)

    # The first row of the CSV file contains column
    # headings and not data, so this statement skips
    # the first row of the CSV file.
    next(reader)

    # Read the rows in the CSV file one row at a time.
    # The reader object returns each row as a list.
    for row_list in reader:

        # From the current row, retrieve the data
        # from the column that contains the key.
        # This will use the column that will be used as key
        key = row_list[0]

        # Store the data from the current row
        # into the dictionary.
        dictionary[key] = row_list

        #print all the elements
        print(row_list)

        #print just the key
        print(key)

