import pickle
game_data = {'player-position': 'N23 E45', 'pockets': ['keys', 'pocket knife', 'polished stone'], 'backpack': ['rope', 'hammer', 'apple'], 'money': 158.50}
save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

load_file = open('save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()
print(loaded_game_data)
