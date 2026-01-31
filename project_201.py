import requests
from colorama import init,Fore, Back, Style
init()
your_input=input("Which pokemon you wanna talk about?")
req=requests.get(f"https://pokeapi.co/api/v2/pokemon/{your_input}")
if req.status_code==200:
    pokemon=req.json()
    print( Fore.MAGENTA +  f"Its name is {pokemon['name']}")
    print( Fore.MAGENTA +  f"Its height is {pokemon['height']}")
    front_look=pokemon['sprites'].get('front_default',None)
    front_shiny=pokemon['sprites'].get('front_shiny',None)
    front_default_dream_world=pokemon['sprites'].get('other',None).get('dream_world',None).get('front_default',None)
    front_default_home=pokemon['sprites'].get('other', None).get('home',None).get('front_default',None)
    front_default_official=pokemon['sprites'].get('other', None).get('official-artwork',None).get('front_default',None)
    front_default_showdown=pokemon['sprites'].get('other', None).get('showdown',None).get('front_default',None)
    print(Fore.MAGENTA + f"You can find its default sprite here:"+ Fore.BLUE+f"{front_look}")
    print(Fore.MAGENTA + f"You can find its shiny sprite here:"+ Fore.BLUE+f"{front_shiny}")
    print(Fore.MAGENTA +f"You can find its dream world artwork here:" + Fore.BLUE+f"{front_default_dream_world}" )
    print(Fore.MAGENTA + f"You can find its home artwork here:" + Fore.BLUE+f"{front_default_home}")
    print(Fore.MAGENTA + f"You can find its official artwork here:" + Fore.BLUE+f"{front_default_official}")
    print(Fore.MAGENTA + f"You can find its Pokémon Showdown  battle sprite here:" + Fore.BLUE+f"{front_default_showdown}")
    print(Fore.MAGENTA + "Its abilities are:")
    for abilities in pokemon['abilities']:
        ability_name=abilities.get('ability',None).get('name',None)
        ability_url=abilities.get('ability',None).get('url',None)
        print(Fore.MAGENTA + "name:" + Fore.BLUE + f"{ability_name} \t" + Fore.MAGENTA + f"url:" + Fore.BLUE + f"{ability_url} ")
    latest_cry=pokemon['cries'].get('latest',None)
    legacy_cry=pokemon['cries'].get('legacy',None)
    print(Fore.MAGENTA + f"Its latest cry you can find on this url:" + Fore.BLUE +f"{latest_cry}")
    print(Fore.MAGENTA + f"Its legacy cry you can find on this url:" + Fore.BLUE +f" {legacy_cry}")
            
else:
    req=requests.get(f"https://pokeapi.co/api/v2/pokemon/?offset=20&limit=120")
    pokemons=req.json()
    print( Fore.MAGENTA+ "You didn't type correct name of pokemon.You can choose one of these pokemons:")
    for pokemon in pokemons['results']:
        print(Fore.BLUE + pokemon['name'])
    

   

