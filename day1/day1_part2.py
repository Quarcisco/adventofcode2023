"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Your puzzle answer was 55429.
"""

clean_list = []

word_to_num = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open("input.txt") as file_contents:
    for line in file_contents:
        clean_str = ''

        # finding first number
        for index in range(len(line)):
            char = line[index]
            if char.isdigit(): 
                clean_str += char
            else:
                substring = line[index:]
                for word in word_to_num.keys():
                    if substring.startswith(word):
                        clean_str += word_to_num[word]               
        
        clean_list.append(int(clean_str[0]+clean_str[-1]))
            
print(sum(clean_list))