# Tuples are immutable, they can not be changed
# Tuples are not the same as a list. Can not containt
# Items such as a grocery list, they are to be used for
# Tuples are meant to contain diverse content(music album, etc)
tuples = "a", "b", "c"
print(tuples)
print(("a", "b", "c"))

# Updating the tuple.
astros = ("Astros", "Houston", "TX")
print(astros)
astros = astros[0], astros[1], "Texas"
print(astros)
rockets = ("Rockets", "Houston", "Texas")
spurs = ("Spurs", "San Anton", "Texas")
print(spurs)
spurs = spurs[0], "San Antonio", spurs[2]
print spurs

# Unpacking the tuple
team, city, state = astros
print(team)
print(city)
print(state)

# Create tuples within a tuple and unpack the tuple
peppers = ("Red Hot Chilli Peppers", "Stadium Arcadium", "May 5, 2006",
           ((1, "Dani California"), (2, "Snow"), (3, "Charlie")))
band, album, releaseDate, tracks = peppers
print(band)
print(album)
print(releaseDate)
# Unpacking tracks using a for loop
for song in tracks:
    track, title = song
    print("\tTrack #: {0}, Title: {1}".format(track, title))
# Unpacking tracks based on index
print(tracks[0])
print(tracks[1])
print(tracks[2])
# Unpacking all tracks in a single print
print(tracks[0], tracks[1], tracks[2])

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
