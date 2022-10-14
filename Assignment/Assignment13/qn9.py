#9. Write a Python script to create a list of city names taken from the user

city=[]

user=input("Enter a city name : ")

user=user.split(' ')

city.append(user)

print(city)