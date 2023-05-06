import random

#jokes list
jokes = ["What has ears but cannot hear? A cornfield.",
'What’s a cat’s favorite dessert? A bowl full of mice-cream.',
'Where did the music teacher leave her keys? In the piano!',
'What did the policeman say to his hungry stomach? “Freeze. You’re under a vest.”',
'What did the left eye say to the right eye? Between us, something smells!',
'What do you call a guy who’s really loud? Mike.',
'Why do birds fly south in the winter? It’s faster than walking!',
'What did the lava say to his girlfriend? “I lava you!”',
'Why did the student eat his homework? Because the teacher told him it was a piece of cake.',
'What did Yoda say when he saw himself in 4k? HDMI.',
'Which superhero hits home runs? Batman!',
'What’s Thanos’ favorite app on his phone? Snapchat.',
'Sandy’s mum has four kids; North, West, East. What is the name of the fourth child? Sandy, obviously!',
'What is a room with no walls? A mushroom.',
'Why did the blue jay get in trouble at school? For tweeting on a test!',
'What social event do spiders love to attend? Webbings.',
'What did one pickle say to the other? Dill with it.']

#select joke from list
joke = random.randint(0, len(jokes))
#output
print(jokes[joke])