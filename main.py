import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

ANIMALS = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'
COUNTRIES = 'Afghanistan Albania Algeria Andorra Angola Argentina Armenia Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bhutan Bolivia Botswana Brazil Brunei Bulgaria Burma Burundi Cambodia Cameroon Canada Chad Chile China Cambodia Comoros Congo Croatia Cuba Cyprus Denmark Djibouti Dominica Ecuador Egypt Eritrea Estonia Ethiopia Fiji Finland France Gabon Georgia Germany Ghana Greece Grenada Guatemala Guinea Guyana Haiti Honduras Hungary Iceland India Indonesia Iran Iraq Ireland Israel Italy Jamaica Japan Jordan Kazakhstan Kenya Kiribati Kuwait Kyrgyzstan Laos Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg Macedonia Madagascar Malawi Malaysia Maldives Mali Malta Mauritania Mauritius Mexico Micronesia Moldova Monaco Mongolia Montenegro Morocco Mozambique Namibia Nauru Nepal Netherlands Nicaragua Niger Nigeria Norway Oman Pakistan Palau Panama Paraguay Peru Philippines Poland Portugal Qatar Romania Russia Rwanda Samoa Senegal Serbia Seychelles Singapore Slovakia Slovenia Somalia Spain Sudan Suriname Swaziland Sweden Switzerland Syria Tajikistan Tanzania Thailand Togo Tonga Tunisia Turkey Turkmenistan Tuvalu Uganda Ukraine Uruguay Uzbekistan Vanuatu Venezuela Vietnam Yemen Zambia Zimbabwe'
FEELINGS = 'acceptance admiration adoration affection afraid agitation agreeable aggressive aggravation agony alarm alienation amazement amusement anger angry anguish annoyance anticipation anxiety apprehension assertive assured astonishment attachment attraction awe beleaguered bewitched bitterness bliss blue boredom calculating calm capricious caring cautious charmed cheerful closeness compassion complacent compliant composed contempt conceited concerned content contentment crabby crazed crazy cross cruel defeated defiance delighted dependence depressed desire disappointment disapproval discontent disenchanted disgust disillusioned dislike dismay displeasure dissatisfied distraction distress disturbed dread eager earnest easy-going ecstasy ecstatic elation embarrassment emotion emotional enamored enchanted enjoyment enraged enraptured enthralled enthusiasm envious envy equanimity euphoria exasperation excited exhausted extroverted exuberant fascinated fatalistic fear fearful ferocity flummoxed flustered fondness fright frightened frustration furious fury generous glad gloating gloomy glum greedy grief grim grouchy grumpy guilt happiness happy harried homesick hopeless horror hostility humiliation hurt hysteria infatuated insecurity insulted interested introverted irritation isolation jaded jealous jittery jolliness jolly joviality jubilation joy keen kind kindhearted kindly laid back lazy like liking loathing lonely longing loneliness love lulled lust mad merry misery modesty mortification naughty neediness neglected nervous nirvana open optimism ornery outgoing outrage panic passion passive peaceful pensive pessimism pity placid pleased pride proud pushy quarrelsome queasy querulous quick-witted quiet quirky rage rapture rejection relief relieved remorse repentance resentment resigned revulsion roused sad sadness sarcastic sardonic satisfaction scared scorn self-assured self-congratulatory self-satisfied sentimentality serenity shame shock smug sorrow sorry spellbound spite stingy stoical stressed subdued submission suffering surprise sympathy tenderness tense terror threatening thrill timidity torment tranquil triumphant trust uncomfortable unhappiness unhappy upset vain vanity venal vengeful vexed vigilance vivacious wary watchfulness weariness weary woe wonder worried wrathful zeal zest'
SHAPES = 'annulus arc asymmetry bipyramid cardioid circle cone crescent cube cuboid curve cylinder decagon disc dodecahedron dot ellipse ellipsoid gnomon heart helix heptagon hexaflexagon hexagon hexahedron hyperboloid hypersphere icosahedron interval kite line lozenge nonagon octagon octahedron orb oval paraboloid parallelepiped parallelogram pentagon plane point polygon polyhedra prism pyramid quadrilateral ray rectangle rhombus round sector semicircle shape shapeless sphere spheroid square star symmetry tetrahedron tesseract torus trapezium trapezoid triangle wedge'
SPORTS = 'aerobics archery badminton baseball basketball biathlon bicycling billiards bowling boxing canoeing crew cricket croquet cycling darts discus diving dodgeball fencing football frisbee golf gymnastics handball hanggliding hockey horseriding hurdle iceskating javelin jogging judo jumprope karate kayaking kite lacrosse luge netball orienteering paddling parasailing parkour pickleball pingpong polo pool racing racquetball rafting rockclimbing rollerskating rowing rugby running sailing scubadiving skating skiing sledding snorkling snowboarding snowshoeing soccer softball squash surfing swimming taekwondo tag tennis throwing toboggan track trampoline triathlon ultramarathon unicycle vault volleyball wakeboarding walking waterskiing weightlifting windsurfing wrestling'

def intro():
	print(""" ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▀▀▄    ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀▄ ▀▄ 
█  █   ▄▀ ▐ ▄▀ ▀▄ █  █ █ █ █         █  █ ▀  █ ▐ ▄▀ ▀▄ █  █ █ █ 
▐  █▄▄▄█    █▄▄▄█ ▐  █  ▀█ █    ▀▄▄  ▐  █    █   █▄▄▄█ ▐  █  ▀█ 
   █   █   ▄▀   █   █   █  █     █ █   █    █   ▄▀   █   █   █  
  ▄▀  ▄▀  █   ▄▀  ▄▀   █   ▐▀▄▄▄▄▀ ▐ ▄▀   ▄▀   █   ▄▀  ▄▀   █   
 █   █    ▐   ▐   █    ▐   ▐         █    █    ▐   ▐   █    ▐   
 ▐   ▐            ▐                  ▐    ▐            ▐        
Instructions:
1. Guess a letter that belongs to the magic word.
2. If you guessed it correct, the correct letter will show on the screen.
3. If you guessed it wrong, you will get a body part hanged on the gallows.
	""")

def get_magic_word(category):
	word_list = category.split()
	magic_word = random.choice(word_list)
	return magic_word

def get_guess(already_guessed):
	guess = input("Please guess a letter:")
	while len(guess) != 1 or (not guess.isalpha()):
		guess = input("Please guess a letter:")
	if guess in already_guessed:
		print("This alphabet has been guessed before.")
	elif guess in magic_word:
		for i in range(len(magic_word)):
			if guess == magic_word[i]:
				correct_guess[i] = guess
	else:
		wrong_guess.append(guess)

def game_end_check(correct_guess, wrong_guess, magic_word):
	if "".join(correct_guess) == magic_word:
		print(f"Congratulations! You have guessed the word correctly before being hanged. The word is {magic_word}.")
		return True
	elif len(wrong_guess) == 5:
		print(f"Boohoo, you have been hanged. The magic word is {magic_word}.")
		return True
	return False

magic_word = get_magic_word(ANIMALS)
correct_guess = ["_"] * len(magic_word)
wrong_guess = []
intro()
while True:
	print(f"Guess an animal name with {len(magic_word)} letters.")
	get_guess(correct_guess + wrong_guess)
	print(f"Correct Guesses: {' '.join(correct_guess)}")
	print(f"Wrong Guesses: {' '.join(wrong_guess)}")
	print(HANGMANPICS[len(wrong_guess)])
	if game_end_check(correct_guess, wrong_guess, magic_word):
		break

