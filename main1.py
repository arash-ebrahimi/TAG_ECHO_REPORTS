# This is a sample Python script.
import uuid


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def split_sections(filename, separator):
    with open(filename, 'r') as file:
        sections = file.read().split(separator)

    # Remove any leading or trailing whitespace from each section
    sections = [section.strip() for section in sections]

    return sections


def save_sections(sections, output_prefix):
    for i, section in enumerate(sections):
        output_filename = f"{output_prefix}_{i + 1}.txt"
        with open(output_filename, 'w') as file:
            file.write(section)


def print_hi(name):
    # file1 = open('D:/echosample/sample1.txt', 'r')
    # Lines = file1.readlines()
    # char_to_replace = {'\n': '', 'â€¢\t': ''}
    # lst = []
    # items=[]
    # for line in Lines:
    #     for key, value in char_to_replace.items():
    #         line = line.replace(key, value)
    #     if line.strip() != '':
    #         lst.append(line)
    ret=split_sections('D:/echosample/sample1.txt','________________________________________')
    str_=''
    for each in ret:
        str_+="________________________________________"+"\n\n"+"ID: "+str(uuid.uuid4())+"\n"+each+"\n\n"
    with open("D:/echosample/Output.txt", "w") as text_file:
        text_file.write(str_)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
