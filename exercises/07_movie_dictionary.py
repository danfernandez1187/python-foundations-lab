movie = {}

title = input("What is the movie title? ")
year = input("What year did the movie come out? ")
rating = input("What rating would you give it out of 10? ")

movie["title"] = title
movie["year"] = year
movie["rating"] = rating

print("Movie summary:")
print(f"Title: {movie['title']}")
print(f"Year: {movie['year']}")
print(f"Rating: {movie['rating']}/10")
