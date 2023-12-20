from bs4 import BeautifulSoup
import requests

MOVIESURL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=MOVIESURL)
movies_content = response.text


soup = BeautifulSoup(movies_content, "html.parser")

movie_title = soup.find_all(name="h3", class_="title")

title_list = []
for title in movie_title:
    title_text = title.getText()

    title_list.append(title_text)


   #reversing ---method 1
# rev_title_list = list(reversed(title_list))
# print(rev_title_list)
    

    
    #reversing ---method 2   ---using the splice
# rev_title_list = title_list[::-1]    
# print(rev_title_list)
    

# with open("movies.txt", "w") as file:
#     for item in rev_title_list:
#         align = f"{item}\n"
#         file.write(align)

    
    #reversing   ---method 3
mv_list = []
for num in range(len(title_list) - 1, -1, -1):
    movies = title_list[num]
    # print(movies)
    mv_list.append(movies)
    
print(mv_list)

with open("movies.txt", mode="w") as file:
    for movie in mv_list:
        file.write(f"{movie}\n")
        







# movies = ['1) The Godfather', '2) The Empire Strikes Back', '3) The Dark Knight', '4) The Shawshank Redemption', '5) Pulp Fiction', '6) Goodfellas', '7) Raiders Of The Lost Ark', '8) Jaws', '9) Star Wars', '10) The Lord Of The Rings: The Fellowship Of The Ring', 
#           '11) Back To The Future', '12: The Godfather Part II', '13) Blade Runner', '14) Alien', '15) Aliens', '16) The Lord Of The Rings: The Return Of The King', '17) Fight Club', '18) Inception', '19) Jurassic Park', '20) Die Hard', 
#           '21) 2001: A Space Odyssey', '22) Apocalypse Now', '23) The Lord Of The Rings: The Two Towers', '24) The Matrix', '25) Terminator 2: Judgment Day', '26) Heat', '27) The Good, The Bad And The Ugly', '28) Casablanca', '29) The Big Lebowski', '30) Seven', 
#           '31) Taxi Driver', '32) The Usual Suspects', "33) Schindler's List", '34) Guardians Of The Galaxy', '35) The Shining', '36) The Departed', '37) The Thing', '38) Mad Max: Fury Road', '39) Saving Private Ryan', '40) 12 Angry Men',
#             '41) Eternal Sunshine Of The Spotless Mind', '42) There Will Be Blood', "43) One Flew Over The Cuckoo's Nest", '44) Gladiator', '45) Drive', '46) Citizen Kane', '47) Interstellar', '48) The Silence Of The Lambs', '49) Trainspotting', '50) Lawrence Of Arabia', 
#             "51) It's A Wonderful Life", '52) Once Upon A Time In The West', '53) Psycho', '54) Vertigo', "55) Pan's Labyrinth", '56) Reservoir Dogs', '57) Whiplash', '58) Inglourious Basterds', '59) The Extra Terrestrial', '60) American Beauty', 
#             '61) Forrest Gump', '62) La La Land', '63) Donnie Darko', '64) L.A. Confidential', '65) Avengers Assemble', '66) Return Of The Jedi', '67) Memento', '68) Ghostbusters', "69) Singin' In The Rain", '70) The Lion King', 
#             '71) Hot Fuzz', '72) Rear Window', '73) Seven Samurai', '74) Mulholland Dr.', '75) Fargo', '76) A Clockwork Orange', '77) Toy Story', '78) Oldboy', '79) Captain America: Civil War', '15) Spirited Away', 
#             '81) The Social Network', '82) Some Like It Hot', '83) True Romance', '84) Rocky', '85) LÃ©on', '86) Indiana Jones And The Last Crusade', '87) Predator', '88) The Exorcist', '89) Shaun Of The Dead', '90) No Country For Old Men', 
#             '91) The Prestige', '92) The Terminator', '93) The Princess Bride', '94) Lost In Translation', '95) Arrival', '96) Good Will Hunting', '97) Titanic', '98) Amelie', '99) Raging Bull', '100) Stand By Me']

# with open("movies2.txt", "w") as file:
#     for mv in movies:
#         file.write(f"{mv}\n")




    
