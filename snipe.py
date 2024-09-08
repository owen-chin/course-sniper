import requests
import time
import random
import register

specs = {
  "year": "2024",
  "term": "1",
  "campus": "NB"
}

url = "https://sis.rutgers.edu/soc/api/openSections.json?year={}&term={}&campus={}".format(
    specs["year"],
    specs["term"],
    specs["campus"]
)

snipes = []
# Reads course indexs in snipes.txt and adds to list
with open('snipes.txt', 'r') as file:
    for line in file:
        snipes.append(line.strip())
# Converts list to ints
for i in range(len(snipes)):
    snipes[i] = int(snipes[i])

def remove_course(index):
    # Remove course from list
    if index in snipes:
        snipes.remove(index)

    # Remove course from file
    with open('snipes.txt', 'r') as file:
        lines = file.readlines()
    with open('snipes.txt', 'w') as file:
        for line in lines:
            if line.strip("\n") != index:
                file.write(line)
      
def binary_search(course_list, target_course):
    left, right = 0, len(course_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if int(course_list[mid]) < target_course:
            left = mid + 1
        elif int(course_list[mid]) > target_course:
            right = mid - 1
        else:
            return mid
    return -1

def index_to_string(i):
    i = str(i)
    length = len(i)
    if length >= 1 and length < 5:
        #add zeros to front until len is 5
        for _ in range(5 - length):
            i = "0" + i
    return i

while True:
    #sleeptime = random.randint(1, 4)
    sleeptime = 1
    response = requests.get(url).json()
    for course in snipes:
        if binary_search(response, course) != -1:
            c = index_to_string(course)
            print(f"found {c}")
            # Also think about sending an email before it registers so the user knows the duo notification is safe
            # if register.auto_register(c):
            #     remove_course(course)

            register.auto_register(c)
            remove_course(course)
        else: 
            print(f"did not find {course}")
    time.sleep(sleeptime)