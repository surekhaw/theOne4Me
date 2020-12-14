# Dog Match Tool

# User is asked name 
x = input("Hello, what is your name:")
print("So, " + x + ", " + "you want to get a dog?  Ok, answer  the following questions:")

# Create an empty list to store MBTI type
MBTI = []

# Question 1
A = "A wild party (stimulus from the outside)"		 
B = "A secluded adventure by yourself or a small group of intimate friends"
Answer1 = input("Where do you get energy? \nA: A wild party (stimulus from the outside \nB: A secluded adventure by yourself or a small group of intimate friends \nAnswer: ")

if Answer1 == "A":
	MBTI.append("E")
elif Answer1 == "B":
	MBTI.append("I")
else:
	print("Invalid entry.  Please try again.") 

# Question 2
A = "Hard facts and Direct answers"	
B = "Rely on your intuition or feelings about a situaton"
Answer2 = input("How do you take in information? \nA: Hard facts and Direct answers \nB: Rely on your intuition or feelings about a situaton \nAnswer: ")

if Answer2 == "A":
	MBTI.append("S")
elif Answer2 == "B":
	MBTI.append("N")
else:
	print("Invalid entry.  Please try again.")

# Question 3
A = "Create a pros and cons list; Use logical reasoning" 
B = "Go with your gut feeling and rely on emotions"
Answer3 = input("How do you make decisions? \nA: Create a pros and cons list; Use logical reasoning \nB: Go with your gut feeling and rely on emotions. \nAnswer: ")


if Answer3 == "A":
	MBTI.append("T")
elif Answer3 == "B":
	MBTI.append("F")
else:
	print("Invalid entry.  Please try again.") 

# Question 4
A = "You have a detailed plan for most areas of your life or when you go on a trip"
B = "You flexible and like to go with the flow."
Answer4 = input("How do you organize your world? \nA: You have a detailed plan for most areas of your life or when you go on a trip \nB: You flexible and like to go with the flow. \nAnswer: ") 

if Answer4 == "A":
	MBTI.append("J")
elif Answer4 == "B":
	MBTI.append("P")
else:
	print("Invalid entry.  Please try again.")

# Join letters of string together
MBTI_test = "".join(MBTI)
print(MBTI_test)

# Establish MBTI dictionary key/value pairs 
MBTI_dict = {"ISTJ": "The Rhodesian Ridgeback", "ISFJ": "The Newfoundland", "INFJ": "The Tibetan Mastiff", "INTJ":"The Chinese Shar-Pei", "ISTP": "The Siberian Husky", 
"ISFP": "The Saluki", "INFP": "The English Toy Spaniel", "INTP": "The Schipperke", "ESTP": "The Dalmatian", "ESFP": "The Papillon", "ENFP": "The German Shorthaired Pointer", 
"ENTP": "The Standard Poodle", "ESTJ": "The Briard", "ESFJ": "The Labrador Retriever", "ENFJ": "The Collie", "ENTJ": "The Border Collie"} 

# Iterate through MBTI dictionary, match key/value with MBTI test, and print suggested dog
for key, value in MBTI_dict.items():
  if key == MBTI_test:
  	print(MBTI_dict[key])
  	print(f"Congratulations! You are a(n) {MBTI_test}.  We recommend the {MBTI_dict[key]}")


