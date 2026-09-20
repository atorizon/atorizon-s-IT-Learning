# My first exercise that really tested my knowledge on Python structures especially if-elif-else statements.

classes = ["ASSASSIN","MAGE","FIGHTER"]
ranks = ["IRON","BRONZE","SILVER","GOLD","PLATINUM","DIAMOND","CHAMPION"]

adv_matchup = False
even_matchup = False
disadv_matchup = False
def enemy_hero_info():
    print(f'YOUR CLASS: {hero_class}')
    print(f'ENEMY HERO CLASS: {enemy_class}')
def advantage_print():
    print("MATCHUP STATUS: You counter their pick, you have the ADVANTAGE.")
def disadvantage_print():
    print("MATCHUP STATUS: They counter you, you are at a DISADVANTAGE.")
def even_print():
    print("MATCHUP STATUS: Even matchup.")

def hero_info():
    print("=== User's Hero Information ===")
    print(f'Hero Class: {hero_class}')
    print(f'Hero Level: Level {hero_level}')

def class_input():
    return input("Enter your hero class (Assassin/Mage/Fighter): ").upper()
def level_input():
    return int(input("Enter your current hero level (1-18): "))
def rank_input():
    return input("Enter your current rank (Iron/Bronze/Silver/Gold/Platinum/Diamond/Champion): ").upper()
def enemy_input():
    return input("Enter your enemy's hero class (Assassin/Mage/Fighter): ").upper()

print("=== Welcome to the MOBA Ranked Game Simulator! ===")
hero_class=class_input()
hero_level=level_input()

while hero_class not in classes or hero_level < 1 or hero_level > 18:
    if hero_class not in classes:
        print("Hero Class Invalid.")
        hero_class=class_input()
        hero_level=level_input()
    elif hero_level < 1 or hero_level > 18:
        print("Hero Level Invalid.")
        hero_class=class_input()
        hero_level=level_input()

hero_info()

if hero_class == "ASSASSIN":
    print(f'\n||| ASSASSINS must snowball early and pick off isolated targets. |||')
elif hero_class == "MAGE":
    print(f'\n||| MAGES must scale through poke damage and cooldown reduction. |||')
else:
    print("\n||| FIGHTERS must extend trades and durability in skirmishes. |||")

if hero_level >= 16 and hero_level <=18:
    print(f'||| GAME PHASE: Full Build (Level {hero_level}) — You are at your strongest form. ||| \n')
elif hero_level >=12:
    print(f'||| GAME PHASE: Late Game (Level {hero_level}) — Objectives decide the match now. ||| \n')
elif hero_level >= 6:
    print(f'||| GAME PHASE: Mid Game (Level {hero_level}) — Teamfights are starting to matter. ||| \n')
else:
    print(f'||| GAME PHASE: Laning (Level {hero_level}) — Play safe, focus on farming. ||| \n')

user_rank=rank_input()

while user_rank not in ranks:
    if user_rank not in ranks:
        print("Rank Invalid.")
        user_rank=rank_input()

print("\n=== USER RANK INFORMATION ===")
match user_rank:
    case "IRON" | "BRONZE":
        print(f'USER RANK: {user_rank} — Wins give flat +20 Points, Losses -15 Points.\n')
    case "SILVER" | "GOLD":
        print(f'USER RANK: {user_rank} — Wins give +18 Points, Losses -18 Points.\n')
    case "PLATINUM" | "DIAMOND":
        print(f'USER RANK: {user_rank} — Points depend on MMR. Wins may give 25+ points.\n')
    case "CHAMPION":
        print(f'USER RANK: {user_rank} — Points are MMR-driven.\n')

enemy_class=enemy_input()

while enemy_class not in classes:
    if enemy_class not in classes:
        print("Hero Class Invalid.")
        enemy_class=enemy_input()





enemy_hero_info()
if hero_class == "ASSASSIN":
    if enemy_class == "ASSASSIN":
        even_print()
        even_matchup=True
    elif enemy_class == "MAGE":
        advantage_print()
        adv_matchup=True
        even_matchup=False
    else:
        disadvantage_print()
        adv_matchup=False
        even_matchup=False
        disadv_matchup=True
        

elif hero_class == "MAGE":
    if enemy_class == "MAGE":
        even_print()
        even_matchup=True
    elif enemy_class == "FIGHTER":
        advantage_print()
        adv_matchup=True
        even_matchup=False
    else:
        disadvantage_print()
        adv_matchup=False
        even_matchup=False
        disadv_matchup=True

else:
    if enemy_class == "FIGHTER":
        even_print()
        even_matchup=True
    elif enemy_class == "ASSASSIN":
        advantage_print()
        adv_matchup=True
        even_matchup=False
    else:
        disadvantage_print()
        adv_matchup=False
        even_matchup=False
        disadv_matchup=True

print("\n=== USER'S GAME REPORT ===")
print(f"User's Current Rank: {user_rank}")
print(f"User's Hero Level: {hero_level}")
print(f"User's Hero Class: {hero_class}")
print(f"Enemy Hero Class: {enemy_class}")

if adv_matchup == True and hero_level > 6:
    print("PREDICTED RANK RESULT: RANK-UP! You have the CLASS ADVANTAGE.")
elif even_matchup == True and hero_level > 6:
    print("PREDICTED RANK RESULT: STALEMATE. You are in an EVEN MATCHUP.")
elif disadv_matchup==True and hero_level < 6:
    print("PREDICTED RANK RESULT: DERANK... You are at a DISADVANTAGE.")
else:
    print("PREDICTED RANK RESULT: Uncertain")

