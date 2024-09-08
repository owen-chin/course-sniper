# snipes = []

# with open('snipes.txt', 'r') as file:
#     # Read each line
#     for line in file:
#         # Remove newline character and add to list
#         snipes.append(line.strip())

# # Print the list
# print(snipes)

# def remove_course(course_number):
#     # Remove course from list
#     if course_number in snipes:
#         snipes.remove(course_number)

#     # Remove course from file
#     with open('snipes.txt', 'r') as file:
#         lines = file.readlines()
#     with open('snipes.txt', 'w') as file:
#         for line in lines:
#             if line.strip("\n") != course_number:
#                 file.write(line)

# # Usage
# remove_course('99999')
# print(snipes)


# s = "213"
# x = "1632"

def format_index(s):
    s = str(s)
    length = len(s)
    if length >= 1 and length < 5:
        #add zeros to front until len is 5
        for _ in range(5 - length):
            s = "0" + s
        
    return s
for x in [123, 1345]:
    x = format_index(x)
    print(x)