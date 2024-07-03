from dataclasses import dataclass

@___
class Movie:
    title: str
    length: ___
    ___: float
    

hocus_pocus = Movie("Hocus Pocus", 96, 6.8)
nightmare = Movie("Nightmare before Christmas", 76, 7.9)

print(hocus_pocus.rating, "vs", nightmare.rating)