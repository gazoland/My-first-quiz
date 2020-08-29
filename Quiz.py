

class NFL:

    def __init__(self, quest, ans1, ans2, tip1, tip2):
        self.quest = quest
        self.ans1 = ans1
        self.ans2 = ans2
        self.tip1 = tip1
        self.tip2 = tip2

class astronomy:

    def __init__(self, quest, ans1, ans2, tip1, tip2):
        self.quest = quest
        self.ans1 = ans1
        self.ans2 = ans2
        self.tip1 = tip1
        self.tip2 = tip2

class countries:

    def __init__(self, quest, ans1, ans2, tip1, tip2):
        self.quest = quest
        self.ans1 = ans1
        self.ans2 = ans2
        self.tip1 = tip1
        self.tip2 = tip2

class series:

    def __init__(self, quest, ans1, ans2, tip1, tip2):
        self.quest = quest
        self.ans1 = ans1
        self.ans2 = ans2
        self.tip1 = tip1
        self.tip2 = tip2

class music:

    def __init__(self, quest, ans1, ans2, tip1, tip2):
        self.quest = quest
        self.ans1 = ans1
        self.ans2 = ans2
        self.tip1 = tip1
        self.tip2 = tip2

cat1 = 'nfl'
cat2 = 'astronomy'
cat3 = 'countries'
cat4 = 'series'
cat5 = 'music'

q_n = [['How many super bowl titles do the 49ers have?', '5', 'five', 'It\'s one less than the Steelers.', 'Joe Montana won a few and Steve Young won one as the quarterbacks.'],
       ['Who is the only player to win 3 Defensive Player of the Year awards other than Lawrence Taylor?', 'jj watt', 'j.j. watt', 'He played at University of Wisconsin', 'He has 2 brothers playing in th NFL.'],
       ['How many seasons of 5000 passing yards Drew Brees has?', '5', 'five', 'He is the only player with more than one.', 'These seasons represent more than 25k passing yards for his career.' ],
       ['Who has the highest TD/Int ratio for his career?', 'aaron rodgers',  'rodgers', 'He played at the University of Califorina - Berkeley.', 'He was drafted in 2005.'],
       ['Who was the last running back to win the MVP award?', 'adrian peterson', 'peterson', 'It was in 2012.', 'He played for the Vikings.'],
       ['Which team plays in Soldier Field?', 'bears', 'chicago bears', 'It\'s one of NFL\'s oldest franchises.', 'It\'s from the state of Illinois.'],
       ['What was the 49ers\'s former iconic stadium called?', 'candlestick park', 'candlestick park', 'It hosted baseball games as well.', 'Its last game is known as "The Pick at the Stick".'],
       ['Who holds the record for most receiving yards in a season?', 'calvin johnson', 'calvin johnson', 'He was drafted from Georgia Tech University.', 'He played for the Lions.'],
       ['Which city hosted Super Bowl XLIX?', 'ny', 'new york', 'It was played in Metlife Stadium.', 'Largest city in the USA.'],
       ['At what round number was Tom Brady drafted?', '6', 'six', 'Position 199 overall.', 'Second to last round.']
]

q_a = [['What is the name of the black hole in the center of the Milky Way?','sagittarius a', 'sagittarius a', 'It is the name of a zodiac sign + letter', 'Nov-Dec sign + 1st letter of the alphabet'],
       ['Who proposed the Theory of Relativity, which models how the Universe behaves?', 'einstein', 'albert einstein', 'He was a german physicist.', 'He has a famous picture with his tongue out.'],
       ['What is the name of the telescope NASA launched in 2001?', 'hubble', 'hubble', 'It is in Earth\'s orbit.', 'Its name was given in honor of an important astronomist called "Edwin".'],
       ['What is the biggest planet in the Solar System?', 'jupiter', 'jupiter', 'It does not have rings.', 'It\'s the fifth closest planet from the Sun.'],
       ['What is the name of the other major galaxy inside the Local Group, other than the Milky Way?', 'andromeda', 'andromeda', 'It\'s the biggest galaxy in the Local Group.', 'It\'s going to collide with the Milky Way in the future and form a supergalaxy named "Milkdromeda".'],
       ['What is the brightest star seen in the night sky?', 'sirius', 'sirius', 'It\'s the closest star to the Sun.', 'Has the name of a Harry Potter character.'],
       ['Where can you measure the hottest temperature in the Solar System other than the Sun?', 'venus', 'venus', 'It\'s also the brighest object in the night sky other than the Moon.', 'Second closest planet to the Sun.'],
       ['What type of object has the strongest gravitational field in the Universe?', 'black hole', 'black holes', 'They are found mostly in the center of galaxies.', '"Not even light can escape it".'],
       ['At what year did the first human landed on the Moon?', '1969', '1969', 'It was Neil Armstrong.', 'Its 50 year anniversary was in 2019.'],
       ['Which planet in the Solar System is the fastest?', 'mercury', 'mercury', 'Its name is also a chemical element.','It\'s the closest planet to the Sun.']
]

q_c = [['Which country is home of the Uluru?', 'australia', 'australia', 'Has a big desert called "Outback".', 'It\'s home of the kangaroos as well.'],
       ['Which country has the highest HDI?', 'norway', 'norway', 'It\'s one of the Nordic countries.', 'Starts with N.'],
       ['What is the smallest country in the World?', 'vatican', 'vatican city', 'It\'s located inside of Italy.','It\'s the headquarters of christianism.'],
       ['What is the largest country in the World?', 'russia', 'russia', 'Its capital is Moscow.', 'Its official language is russian.'],
       ['What country the Aztecs are from?', 'mexico', 'mexico', 'This country is famous for its skulls.', 'It was colonized by Spain.'],
       ['What country was bread invented in?', 'egypt', 'egypt', 'Its capital is Cairo.', 'It\'s home of the Great Pyramid og Giza.'],
       ['What country is the most visited in the World?', 'france', 'france', 'The Seine is an important river that crosses its capital.', 'Mona Lisa is displayed in one of this country\'s museums.'],
       ['What country has the only non-quadrilateral (not a square neither a rectangle) flag?', 'nepal', 'nepal', 'It\'s home of the highest mountain on the planet.', 'Its capital is Kathmandu.'],
       ['What country has the driest place on Earth?', 'chile', 'chile', 'The place is known as Atacama Desert.', 'The Easter Island belongs to this country.'],
       ['What country has the unicorn as its national animal?', 'scotland', 'scotland', 'It\'s part of the UK.', 'The Loch Ness Monster is supposedly living in one of its lakes.']
]

q_s = [['In the series "Friends", what country Chandler goes to escape Janet?', 'yemen', 'iemen', 'It is on the Arabian Peninsula.', 'Starts with the letter Y.'],
       ['In the series "The Walking Dead", who kills Shane after he turned to a walker?', 'carl', 'carl grimes', 'It\'s one of the youngest characters.', 'It\'s Rick\'s son.'],
       ['In the series "This Is Us", where was William born?', 'memphis', 'memphis', 'It\'s the capital of Tennessee.', 'Randall goes there with him in the episode of the same name.'],
       ['In the series "Prison Break", how many inmates escaped from Fox River Penitentiary?', '8', 'eight', 'It\'s between 5 and 10.', 'Don\'t forget about Patoshik, C-Note and Tweener.' ],
       ['In the series "13 Reasons Why", who is the first person Hannah kisses?', 'justin', 'justin foley', 'He is one of the school\'s basketball team\'s stars.', 'He later has a complicated relationship with Jessica.'],
       ['In the series "La Casa de Papel", who is the second in charge after the Professor?', 'berlin', 'berlim', 'He is the most experienced of the group.', 'German capital.'],
       ['In the series "Avatar: The Last Airbender", who does Toph encounter on the road when she decides to give up on teaching Aang?', 'iroh', 'uncle iroh', 'He is known as The Dragon of the West', 'He loves tea.'],
       ['In the series "How I Met Your Mother", who is addicted to guns?', 'robin', 'robin scherbatzky', 'It\'s one of the main characters.' , 'She is from Canada.'],
       ['In the series "This Is Us", who started the family\'s Thanksgiving traditions?', 'jack', 'jack pearson', 'This story is told in the episode "Pilgrim Rick".', 'It\'s one of the parents.'],
       ['In the series "Avatar: The Last Airbender", who saves Aang from the prison when he is captured by Admiral Zhao?', 'zuko', 'prince zuko', 'It\'s someone unexpected.', 'Later is known as "The Blue Spirit".']
]

q_m = [['Who sings "Poker Face"?', 'lady gaga', 'gaga', 'It\'s a woman.', 'She also sings "Bad Romance".'],
       ['Which band sings "Moves Like Jagger"?', 'maroon 5', 'maroon five', 'They\'re from L.A.', 'The singer is Adam Levine.'],
       ['Which band sings "Live Forever?"', 'oasis', 'oasis', 'There were 2 polemic brothers in the band.', 'They are from England.'],
       ['Who sings "Needed Me"?', 'rihanna', 'rhianna', 'She also has a makeup brand called "Fenty".', 'She started with Def Jam Records.'],
       ['Who sings "Hot"?', 'avril lavigne', 'avril lavign', 'She\'s also a fashion designer.', 'She is from Canada.'],
       ['Which band sings "Let It Be?"', 'beatles', 'the beatles', 'They are considered the most popular band of all time.', 'The band had 4 members.'],
       ['Who sings "Sorry"?', 'justin bieber', 'justin', 'His first single was "Baby".', 'He used to have a really famous haircut.'],
       ['Which band sings "Sucker"?', 'jonas brothers', 'the jonas brothers', 'They used to have a TV show.', 'They were in the movie "Camp Rock".'],
       ['Who sings "Ocean Eyes"?', 'billie eilish', 'bilie eilish', 'She also sings "Bad Guy".', 'She has won 5 grammy awards.'],
       ['Who sings "Obsessed"?', 'mariah carey', 'maria carey', 'She has one of the highest vocal ranges.', 'She also sings "All I Want For Christmas Is You".']

]

qn1 = NFL(q_n[0][0],q_n[0][1],q_n[0][2],q_n[0][3],q_n[0][4])
qn2 = NFL(q_n[1][0],q_n[1][1],q_n[1][2],q_n[1][3],q_n[1][4])
qn3 = NFL(q_n[2][0],q_n[2][1],q_n[2][2],q_n[2][3],q_n[2][4])
qn4 = NFL(q_n[3][0],q_n[3][1],q_n[3][2],q_n[3][3],q_n[3][4])
qn5 = NFL(q_n[4][0],q_n[4][1],q_n[4][2],q_n[4][3],q_n[4][4])
qn6 = NFL(q_n[5][0],q_n[5][1],q_n[5][2],q_n[5][3],q_n[5][4])
qn7 = NFL(q_n[6][0],q_n[6][1],q_n[6][2],q_n[6][3],q_n[6][4])
qn8 = NFL(q_n[7][0],q_n[7][1],q_n[7][2],q_n[7][3],q_n[7][4])
qn9 = NFL(q_n[8][0],q_n[8][1],q_n[8][2],q_n[8][3],q_n[8][4])
qn10 = NFL(q_n[9][0],q_n[9][1],q_n[9][2],q_n[9][3],q_n[9][4])

qa1 = astronomy(q_a[0][0],q_a[0][1],q_a[0][2],q_a[0][3],q_a[0][4])
qa2 = astronomy(q_a[1][0],q_a[1][1],q_a[1][2],q_a[1][3],q_a[1][4])
qa3 = astronomy(q_a[2][0],q_a[2][1],q_a[2][2],q_a[2][3],q_a[2][4])
qa4 = astronomy(q_a[3][0],q_a[3][1],q_a[3][2],q_a[3][3],q_a[3][4])
qa5 = astronomy(q_a[4][0],q_a[4][1],q_a[4][2],q_a[4][3],q_a[4][4])
qa6 = astronomy(q_a[5][0],q_a[5][1],q_a[5][2],q_a[5][3],q_a[5][4])
qa7 = astronomy(q_a[6][0],q_a[6][1],q_a[6][2],q_a[6][3],q_a[6][4])
qa8 = astronomy(q_a[7][0],q_a[7][1],q_a[7][2],q_a[7][3],q_a[7][4])
qa9 = astronomy(q_a[8][0],q_a[8][1],q_a[8][2],q_a[8][3],q_a[8][4])
qa10 = astronomy(q_a[9][0],q_a[9][1],q_a[9][2],q_a[9][3],q_a[9][4])

qc1 = countries(q_c[0][0],q_c[0][1],q_c[0][2],q_c[0][3],q_c[0][4])
qc2 = countries(q_c[1][0],q_c[1][1],q_c[1][2],q_c[1][3],q_c[1][4])
qc3 = countries(q_c[2][0],q_c[2][1],q_c[2][2],q_c[2][3],q_c[2][4])
qc4 = countries(q_c[3][0],q_c[3][1],q_c[3][2],q_c[3][3],q_c[3][4])
qc5 = countries(q_c[4][0],q_c[4][1],q_c[4][2],q_c[4][3],q_c[4][4])
qc6 = countries(q_c[5][0],q_c[5][1],q_c[5][2],q_c[5][3],q_c[5][4])
qc7 = countries(q_c[6][0],q_c[6][1],q_c[6][2],q_c[6][3],q_c[6][4])
qc8 = countries(q_c[7][0],q_c[7][1],q_c[7][2],q_c[7][3],q_c[7][4])
qc9 = countries(q_c[8][0],q_c[8][1],q_c[8][2],q_c[8][3],q_c[8][4])
qc10 = countries(q_c[9][0],q_c[9][1],q_c[9][2],q_c[9][3],q_c[9][4])

qs1 = series(q_s[0][0],q_s[0][1],q_s[0][2],q_s[0][3],q_s[0][4])
qs2 = series(q_s[1][0],q_s[1][1],q_s[1][2],q_s[1][3],q_s[1][4])
qs3 = series(q_s[2][0],q_s[2][1],q_s[2][2],q_s[2][3],q_s[2][4])
qs4 = series(q_s[3][0],q_s[3][1],q_s[3][2],q_s[3][3],q_s[3][4])
qs5 = series(q_s[4][0],q_s[4][1],q_s[4][2],q_s[4][3],q_s[4][4])
qs6 = series(q_s[5][0],q_s[5][1],q_s[5][2],q_s[5][3],q_s[5][4])
qs7 = series(q_s[6][0],q_s[6][1],q_s[6][2],q_s[6][3],q_s[6][4])
qs8 = series(q_s[7][0],q_s[7][1],q_s[7][2],q_s[7][3],q_s[7][4])
qs9 = series(q_s[8][0],q_s[8][1],q_s[8][2],q_s[8][3],q_s[8][4])
qs10 = series(q_s[9][0],q_s[9][1],q_s[9][2],q_s[9][3],q_s[9][4])

qm1 = NFL(q_m[0][0],q_m[0][1],q_m[0][2],q_m[0][3],q_m[0][4])
qm2 = NFL(q_m[1][0],q_m[1][1],q_m[1][2],q_m[1][3],q_m[1][4])
qm3 = NFL(q_m[2][0],q_m[2][1],q_m[2][2],q_m[2][3],q_m[2][4])
qm4 = NFL(q_m[3][0],q_m[3][1],q_m[3][2],q_m[3][3],q_m[3][4])
qm5 = NFL(q_m[4][0],q_m[4][1],q_m[4][2],q_m[4][3],q_m[4][4])
qm6 = NFL(q_m[5][0],q_m[5][1],q_m[5][2],q_m[5][3],q_m[5][4])
qm7 = NFL(q_m[6][0],q_m[6][1],q_m[6][2],q_m[6][3],q_m[6][4])
qm8 = NFL(q_m[7][0],q_m[7][1],q_m[7][2],q_m[7][3],q_m[7][4])
qm9 = NFL(q_m[8][0],q_m[8][1],q_m[8][2],q_m[8][3],q_m[8][4])
qm10 = NFL(q_m[9][0],q_m[9][1],q_m[9][2],q_m[9][3],q_m[9][4])

Q_GRID = [
    [qn1, qn2, qn3, qn4, qn5, qn6, qn7, qn8, qn9, qn10],
    [qa1, qa2, qa3, qa4, qa5, qa6, qa7, qa8, qa9, qa10],
    [qc1, qc2, qc3, qc4, qc5, qc6, qc7, qc8, qc9, qc10],
    [qs1, qs2, qs3, qs4, qs5, qs6, qs7, qs8, qs9, qs10],
    [qm1, qm2, qm3, qm4, qm5, qm6, qm7, qm8, qm9, qm10]
]


def quiz(question):
    print('\nCategory: ' + cat.upper())
    global score
    score = 0
    tip = 't'
    ind = 1
    for element in Q_GRID[x]:
        print('\nQuestion ' + str(ind) + ': ')
        print('>>> ' + element.quest)
        print('Tips left: 2')
        print('Press "T" for tip.')
        an = input('Answer: ').lower()
        if an == tip:
            print('\n>>> ' + element.quest)
            print('Tip 1: ' + element.tip1)
            print('Tips left: 1')
            print('Press "T" for tip.')
            an = input('Answer: ').lower()
            if an == tip:
                print('\n>>> ' + element.quest)
                print('Tip 1: ' + element.tip1)
                print('Tip 2: ' + element.tip2)
                an = input('Answer: ').lower()
                if an == element.ans1 or an == element.ans2:
                    score = score + 50
                else:
                    print('Wrong.')
            elif an == element.ans1 or an == element.ans2:
                score = score + 75
            else:
                print('Wrong.')
        elif an == element.ans1 or an == element.ans2:
            score += 100
        else:
            print('Wrong.')
        ind += 1
    return score



again = True

while again:
    print('\nWelcome to the Quiz game\nSelect one of the categories below and try getting right the most questions you can!\nPlease type the letter of the corresponding category:')
    print('a) NFL\nb) Astronomy\nc) Countries\nd) Series\ne) Music')
    cat = input('Choose category: ').lower()
    while cat != 'a' and cat != 'b' and cat != 'c' and cat != 'd' and cat != 'e':
        print('\nCategories: \na) NFL\nb) Astronomy\nc) Countries\nd) Series\ne) Music')
        print('Please type "a", "b", "c", "d" or "e":')
        cat = input('Choose category: ').lower()

    if cat == 'a':
        cat = cat1
        x = 0
        quiz(Q_GRID)

    if cat == 'b':
        cat = cat2
        x = 1
        quiz(Q_GRID)

    if cat == 'c':
        cat = cat3
        x = 2
        quiz(Q_GRID)

    if cat == 'd':
        cat = cat4
        x = 3
        quiz(Q_GRID)

    if cat == 'e':
        cat = cat5
        x = 4
        quiz(Q_GRID)

    y = 'y'
    yes = 'yes'
    n = 'n'
    no = 'no'

    if score == 1000:
        pri = '\nAmazing! Perfect score! \nCongratulations!'
    elif score >= 800 and score < 1000:
        pri = '\nGreat score!\nCongratulations!'
    elif score >= 600 and score < 800:
        pri = '\nPretty good score!\nWell done!'
    elif score >= 400 and score < 600:
        pri = '\nThat´s a decent score!\nBut you can do better next time!'
    elif score < 400:
        pri = '\nNot that good...\nBetter luck next time!'

    print('\nYour final score is: ' + str(score))
    print(pri)
    again = input ('\nWould you like to play again?\nType "Y" for yes or "N" for no: ').lower()
    while again != y and again != yes and again != n and again != no:
        again = input('\nWould you like to play again?\nPlease type "Y" for yes or "N" for no: ').lower()
    if again == y or again == yes:
        again = True
    elif again == n or again == no:
        again = False

print('\nThanks for playing!')

