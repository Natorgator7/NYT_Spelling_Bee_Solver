f = open('scrabble_dict.txt', 'r') #text file containing scrabble word list
words = list(map(str.strip, f.readlines()))
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
center_letter = input("Please enter the center letter in caps. Press ENTER when complete.\n")
letters = [input("Please enter the outer 6 letters in caps. Press ENTER after each input.\n") for x in range(0,6)]
alphabet = [i for i in alphabet if i not in letters and i not in center_letter]
shortened_list = [i for i in words if center_letter in i and not any(x in i for x in alphabet) and len(i) >= 4]
panagram = [i for i in shortened_list if all(x in i for x in letters)] #words that use all 7 letters
print("Here's a list of all possible words: " + (', '.join(map(str, shortened_list))))
print("Panagram(s): " + (', '.join(map(str, panagram))))