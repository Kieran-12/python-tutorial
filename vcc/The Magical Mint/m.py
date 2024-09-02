electrum_weight = 0.343
dragon_bone_weight = 0.534
coin_weight = 30.991

most_dragon_bones_possible = int(coin_weight / dragon_bone_weight)  # 58

for number_of_dragon_bones in range(1, 59):
    electrum_coins = (
        coin_weight - dragon_bone_weight * number_of_dragon_bones
    )  # weight of all electrum coins
    number_of_electrums = electrum_coins / electrum_weight
    if number_of_electrums.is_integer() == True:
        e = int(number_of_electrums)  # 67 electrums

all_electrums = e * electrum_weight
all_dragon_bones = round(coin_weight - all_electrums, 3)
db = int(round(all_dragon_bones / dragon_bone_weight, 3))


print("There are " + str(e) + " electrums and " + str(db) + " dragon bones in the bag.")
