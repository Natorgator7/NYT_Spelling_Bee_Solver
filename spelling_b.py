f = open('scrabble_dict.txt', 'r')
words = list(map(str.strip, f.readlines()))
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",\
"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = []
center_letter = input("Please enter the center letter in caps. Press ENTER when complete.\n")
for x in range(0,6):
	letters.append(input("Please enter the outer 6 letters in caps. Press ENTER after each input.\n"))
for i in letters: 
    try: 
        alphabet.remove(i)
        alphabet.remove(center_letter)
    except ValueError: 
        pass
shortened_list = [i for i in words if center_letter in i]
shorter_list = [i for i in shortened_list if not any(x in i for x in alphabet)]
even_shorter_list = [i for i in shorter_list if len(i) >= 4]
panagram = [i for i in even_shorter_list if all(x in i for x in letters)]
print("Here's a list of all possible words: " + (', '.join(map(str, even_shorter_list))))
print("Panagram(s): " + (', '.join(map(str, panagram))))