
from operator import indexOf


def main():
    # with open("provinces.txt", "rt") as text_file
    text_list = provinces("week9/provinces.txt")
    print(text_list)


def provinces(filename):
    # empty list that will store the lines
    # of the text file
    text_list = []

    # open text file for reading, an store a
    # reference to the opened file in a variable
    # named text_file
    with open(filename, "rt") as text_file:
        counter = 0
        # read the contents of the text
        # file one line at a time
        for line in text_file:

            # remove white space, if any,
            # from beginning and from end
            clean_line = line.strip()

            if clean_line == "AB":
                clean_line = "Alberta"
            if clean_line == "Alberta":
                counter += 1

            # append the clean line of text
            # onto the end of the list
            text_list.append(clean_line)

        first_element = text_list[0]
        last_element = text_list[-1]
        text_list.remove(first_element)
        text_list = text_list[:-1]

    print(f"There are {counter} Alberta's.")

    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()
