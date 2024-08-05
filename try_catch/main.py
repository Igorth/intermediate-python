# # FileNotFound
# with open('a_main.txt') as file:
#     file.read()
#
# # KeyError
# a_dict = {'key': 'value'}
# value = a_dict['non_existent_key']
#
# # IndexError
# fruit_list = ['apple', 'banana', 'cherry']
# fruit = fruit_list[10]
#
# # TypeError
# text = "abc"
# print(text + 123)


# try:
#     # FileNotFound
#     with open('a_main.txt') as file:
#         file.read()
#     a_dict = {'key': 'value'}
#     print(a_dict['key'])
#
# except FileNotFoundError:
#     file = open('a_main.txt', 'w')
#     file.write("This is a test file.")
#
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist in the dictionary.")
#
# raise KeyError('This is a custom error message.')


# height = float(input("Enter your height (in meters): "))
# weight = int(input("Enter your weight (in kilograms): "))
#
# if height > 3:
#     raise ValueError("Height must be less than or equal to 3 meters.")
#
# bmi = weight / (height ** 2)
# print(f"Your BMI is: {bmi:.2f}")


# fruits = ["Apple", "Pear", "Orange"]
# # Catch the exception and make sure the code runs without crashing.
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(f"{fruit} pie.")
#
#
# make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
#
# def count_likes(posts):
#     total_likes = 0
#     for post in posts:
#         try:
#             total_likes = total_likes + post['Likes']
#         except KeyError:
#             print("Likes not provided for this post.")
#
#     return total_likes
#
#
# count_likes(facebook_posts)

#--------------------------------------------------------------

# User Input Validation
# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("That's not a valid number.")
# else:
#     print(f"Your age is {age}.")

#--------------------------------------------------------------
# Network Communication
import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.ConnectionError as err:
    print(f"Connection error occurred: {err}")
else:
    print("Success!")