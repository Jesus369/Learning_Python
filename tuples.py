# Create a tuple with a list that also includes tuples
# Tuples within a list ARE mutable objects
linkin = ("Linkin Park", "Meteora", 2003, [
          (1, "Foward"), (2, "Don't Stay"), (3, "Somewhere I Belong")])

astist, album, year, tracks = linkin
print(tracks)
tracks[0] = (1, "Foreward")
tracks.append((4, "Lying From You"))
tracks.append((5, "Hit the Floot"))
print(tracks)

for song in tracks:
    print("\t{0}".format(song))
