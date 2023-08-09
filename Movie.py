# J Programming
# Movie rating
movie = input("What movie did you watch?") 
print("Thank you for watching, " + movie)
print("Please rate on a 1-5 scale")
rating = eval(input("Rating:",))
if rating > 5:
    print("error, try again with 1-5")
    rating = eval(input("Rating:",))
else:
    myRating = "5"
    print("Awsome, I gave it " + myRating, "stars")
print("That is a", 5-rating, "star difference")
