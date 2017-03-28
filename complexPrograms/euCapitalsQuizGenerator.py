#! python2
#Program which will use dictionary and generate random quiz files with
#questions and answers in random order along with answer key

import random, os

#The quiz data.
dictionary={'United Kingdom' : 'London', 'Albania' : 'Tirana',
            'Andorra' : 'Andorra la Vella', 'Austria' : 'Vienna',
            'Belgium' : 'Brussels', 'Bosnia and Herzegovina' : 'Sarajevo',
            'Bulgaria' : 'Sofia', 'Croatia' : 'Zagreb', 'Cyprus' : 'Nicosia',
            'Czech Republic' : 'Prague', 'Denmark' : 'Copenhagen',
            'Estonia' : 'Tallin', 'Finland' : 'Helsinki', 'France' : 'Paris',
            'Germany' : 'Berlin', 'Greece' : 'Athens', 'Hungary' : 'Budapest',
            'Iceland' : 'Reykjavik', 'Ireland' : 'Dublin', 'Italy' : 'Rome',
            'Kosovo' : 'Pristina', 'Latvia' : 'Riga', 'Liechtenstein' : 'Vaduz',
            'Lithuania' : 'Vilnius', 'Luxembourg' : 'Luxembourg',
            'Macedonia' : 'Skopje', 'Malta' : 'Valetta', 'Moldova' : 'Chisinau',
            'Monaco' : 'Monaco', 'Montenegro' : 'Podgorica', 'Norway' : 'Oslo',
            'Netherlands' : 'Amsterdam', 'Poland' : 'Warsaw', 'Portugal' : 'Lisbon',
            'Romania' : 'Bucharest', 'San Marino' : 'San Marino',
            'Serbia' : 'Belgrade', 'Slovakia' : 'Bratislava', 'Slovenia' : 'ljubljana',
            'Spain' : 'Madrid', 'Sweden' : 'Stockholm', 'Switzerland' : 'Bern',
            'Vatican City' : 'Vatican City'}

os.makedirs('EU_Quiz_Questions')
os.makedirs('EU_Quiz_Answers')

#Generate quiz files
for quizNumber in range(43):
    quizFile = open('EU_Quiz_Questions/eucapitals%s.txt' % (quizNumber + 1), 'w')
    answerKey = open('EU_Quiz_Answers/eucapitals_answers%s.txt' % (quizNumber + 1), 'w')

    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 20) + 'EU Capitals Quiz %s' % (quizNumber + 1))
    quizFile.write('\n\n')

    countries = list(dictionary.keys())
    random.shuffle(countries)

    for questionNumber in range(len(dictionary.keys())):
        correctAnswer = dictionary[countries[questionNumber]]
        wrongAnswers = list(dictionary.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the capital of %s?\n' % (questionNumber + 1,
            countries[questionNumber]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKey.write('%s. %s\n' % (questionNumber + 1, 'ABCD'[
            answerOptions.index(correctAnswer)]))

quizFile.close()
answerKey.close()
