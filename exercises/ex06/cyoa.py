"""EX06 - Choose your own adventure!"""

__author__ = "730576293"

import random

"""main stuff dont forgor"""

points: int = 10
player: str = ""

MOJ_ACTION = "\U0001F4A5"
MOJ_STAR = "\U00002B50"
MOJ_STATS = "\U0001F4D5"
MOJ_GREENSQ = "\U0001F7E9"
MOJ_REDSQ = "\U0001F7E5"
moj_orangesq = "\U0001F7E7"
moj_yellowsq = "\U0001F7E8"


def greet() -> None:
    print(f"---Hello and welcome to the UNC Freshman Experience RPG!--- \n\nBattle through the hurdles of freshman year with text based battles and story progression!")
    print(f"Our journey begins with an acceptance letter adressed to you!")
    global player
    player = input("What name would we find this letter adressed to? Please note that this is what you'll be referred as for the duration of the game, so choose wisely! ")
    print(f"It's a pleasure to meet you {player}! Let's learn the ropes before we get started! \n{MOJ_STAR} - Notates tutorial text \n{MOJ_ACTION} - Notates actions that can be taken \n{MOJ_STATS} - Will appear around your stats")
    print(f"To take an action, type the name of the action into the program. Actions will always appear with an emoji on either side")
    print(f"So, have you declared your major yet? What you end up choosing tends to have a pretty big effect on your experience here!")

def health_display(hp: int, total_hp: int):
    display: str = ""
    damage: int = (total_hp - hp)
    for elem in range(0, damage):
        display += MOJ_REDSQ
    for elem in range(0, hp):
        display += MOJ_GREENSQ
    return display


def battle_bot(hp: int, moves: dict[str, int]):
    enemy_strength: int = hp
    player_strength: int = points
    enemy_health: int = enemy_strength
    player_health: int = player_strength
    turn: int = 1
    damage = 3

    print(f"Turn {turn} \nEnemy HP:{health_display(enemy_health, enemy_strength)}\nPlayer HP:{health_display(player_health, player_strength)}")
    print(f"put actions here")
    enemy_health -= damage
    print(f"enemy uses attack")
    player_health -= damage
    turn += 1

    if player_health <= 0:
        print("lol loser")
    if enemy_health <=0:
        "yay winner"

def battle_actions(moves: dict[str,int]):
    for key in moves:
        print(key, ":", moves[key])



moves: dict[str, int] = {"f{MOJ_REDSQ} hit1 {MOJ_REDSQ}":5, "f{moj_orangesq}hit2{moj_orangesq}":10, "f{moj_yellowsq}hit3{moj_yellowsq}":20, "f{MOJ_GREENSQ}hit4{MOJ_GREENSQ}":30}


def registration() -> None:
    print(f"Here comes a challenge, ")

def housing() -> None:
    "lol"

def classes() -> None:
    "lol"

print(battle_actions(moves))