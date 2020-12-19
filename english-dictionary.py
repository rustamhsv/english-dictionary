import mysql.connector
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

def translate(word):
	con = mysql.connector.connect(
	user = "ardit700_student",
	password = "ardit700_student",
	host = "108.167.140.122",
	database = "ardit700_pm1database"
	)

	cursor = con.cursor()
	expression_query = cursor.execute("SELECT Expression FROM Dictionary")
	expressions = []
	list_of_tuples = cursor.fetchall()
	for i in range(len(list_of_tuples)):
		expressions.append(list_of_tuples[i][0])

	word = word.lower()
	if word in expressions:
		query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
		definitions = cursor.fetchall()
		return definitions
	elif word.title() in expressions:
		query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.title())
		definitions = cursor.fetchall()
		return definitions
	elif word.upper() in expressions:
		query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.upper())
		definitions = cursor.fetchall()
		return definitions
	elif len(get_close_matches(word, expressions)) > 0:
		best_match = get_close_matches(word, expressions)[0]
		user_answer = input("Did you mean %s instead? Enter Y or N:  " % best_match)
		user_answer = user_answer.upper()
		if user_answer == 'Y':
			query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % best_match)
			definitions = cursor.fetchall()
			return definitions
		elif user_answer == 'N':
			return("The word doesn't exist!")
		else:
			return "No such entry"
	else:
		return("The word doesn't exist!")


word = input("Enter a word: ")
output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)

