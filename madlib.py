# Creating a madlib begginer project. Madlib is a word game where one player prompts another for a list of words to substitute for blanks in a story.
#The story i'll be choosing today is that of a advertisment of a zombie camp.

print("ZOMBIE CAMP MADLIB")
verb1 = input("Enter a verb: ")
num = int(input("Enter a number larger than 1: "))
verb2 = input("Enter another verb: ")
noun = input("Enter a noun: ")
pl_noun = input("Enter a plural noun: ")
adj = input("Enter an adjective: ")
advb = input("Enter an adverb: ")

print(f"How well can you {verb1}? For only {num} dollars you can spend a week at the zombie camp. At zombie camp you get to stay up all night and stay up all night and {verb2} all day. you'll get to play {noun} games and eat {adj} {pl_noun}. So get your application in our man office.")
