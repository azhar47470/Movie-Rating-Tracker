# movies = ["The Godfather" ,"The Dark Knight" ,"Inception" ,"Avengers Infinity War" ,"Avengers Endgame"]
# ratings = []
# for movie in movies:
#     rating = float(input(f"On a Scale of 1-10 What will you rate {movie} : "))
#     ratings.append(rating)

# average_rating = round((sum(ratings)/len(ratings)),2)

# highest_rated = []
# for h in range(len(ratings)):
#     if ratings[h] == max(ratings):
#         highest_rated.append(movies[h])

# lowest_rated = []
# for l in range(len(ratings)):
#     if ratings[l] == min(ratings):
#         lowest_rated.append(movies[l])

# eight_plus_rated = []
# for e in range(len(ratings)):
#     if ratings[e] >= 8:
#         eight_plus_rated.append(movies[e])

# print(f"Average Ratings : {average_rating}")
# print(f"Highest Rated : {'-'.join(highest_rated)}")
# print(f"lowest Rated : {'-'.join(lowest_rated)}")
# if eight_plus_rated:
#  print(f"8+ Rated : {' & '.join(eight_plus_rated)}")




movies = ["The Godfather" ,"The Dark Knight" ,"Inception"]
movies_rating = {}
for movie in movies:
    rating = float(input(f"On a Scale of 1-10 What will you rate {movie} : "))
    movies_rating[movie] = rating 

max_movie = max(movies_rating, key=movies_rating.get)
max_rating = movies_rating[max_movie]

min_movie = min(movies_rating, key=movies_rating.get)
min_rating = movies_rating[min_movie]

for movie, rating in movies_rating.items():
 print(f"{movie} : {rating}")

print(f"Highest Rated Movie : {max_movie} ({max_rating})")
print(f"lowest Rated Movie : {min_movie} ({min_rating})")

print(f"\n8+ Rated Movies : ")
for movie, rating in movies_rating.items():
   if rating >= 8:
      print(f"  • {movie} ({rating})")