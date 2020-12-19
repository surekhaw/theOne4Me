import pandas as pd

# introducion to site
print('Welcome to The One 4 Me!\nAnswer four basic questions to find the ideal dog breed to match your personality.\nYour soul pet is just a few clicks away!')

# # gather user input to determine user's MBTI
# energy = input('Where do you get your energy? \n\tIf you would prefer a wild party, enter "E."\n\tIf you would prefer a secluded adventure by yourself\n\t\tor a small group of intimate friends, enter I\t')
# information = input('How do you take in information?\n\tIf you prefer hard facts and direct answers, enter "S."\n\tIf you prefer to rely on your intuition\n\t\tor feelings about a situaton, enter N\t')
# decisions = input('How do you make decisions?\n\tIf you prefer to create a pros and cons list, enter "T."\n\tIf you prefer to go with your gut feeling and rely on emotions, enter F\t')
# organization = input('How do you organize your world?\n\tIf you prefer to have a detailed plan for most areas of your life, enter "J."\n\tIf you prefer to stay flexible and go with the flow, enter P\t')

# # concatenate user input into MBTI code
# user_MBTI = energy + information + decisions + organization

find_user_mbti = {
	'question': ['Where do you get your energy?\n\tIf you would prefer a wild party, enter "A"\n\tIf you would prefer a secluded adventure by yourself\n\t\tor a small group of intimate friends, enter "B" \t', 'How do you take in information?\n\tIf you prefer hard facts and direct answers, enter "A"\n\tIf you prefer to rely on your intuition\n\t\tor feelings about a situaton, enter "B"\t', 'How do you make decisions?\n\tIf you prefer to create a pros and cons list, enter "A"\n\tIf you prefer to go with your gut feeling and rely on emotions, enter "B"\t', 'How do you organize your world?\n\tIf you prefer to have a detailed plan for most areas of your life, enter "A"\n\tIf you prefer to stay flexible and go with the flow, enter "B"'],
	'A': ['E', 'S', 'T', 'J'],
	'B': ['I', 'N', 'F', 'P'],
}

def mbti_ques(mbti):
	user_response = ''
	for ques in mbti['question']:
		user_response += input(ques)
	user_response = user_response.upper()
	return mbti_ans(user_response)

def mbti_ans(ans):
	user_MBTI = ''
	for index, ltr in enumerate(ans):
		user_MBTI += find_user_mbti[ltr][index]
	return user_MBTI

user_MBTI = mbti_ques(find_user_mbti)

# Print user's MBTI and description of their personality
print(f'Your Myers Briggs Type Indicator is {user_MBTI}.')

# import dog MBTI dataset
dog_data = pd.read_csv('./dog_data_clean.csv', header=0, index_col=1).T.to_dict()
print(dog_data[user_MBTI]['dog_breed'])
print(dog_data[user_MBTI]['dog_personality'])

# find index of matching MBTI
# index = dog_data[dog_data['dog_MBTI']== user_MBTI].index.values
# index = index[0]		
# perfect_dog = dog_data.iloc[index, 3]
# personality = dog_data.iloc[index, 2]
# print(f'Your perfect dog is {perfect_dog}.\nYou and your dog share the following personality traits:\n\t{personality}')
					


