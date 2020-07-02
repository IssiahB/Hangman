from html.parser import HTMLParser

import mysql.connector
import random
import requests

wordsDB = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="P@sta3ters",
    database="hangmanDB"
)

cursor = wordsDB.cursor()


def get_ran_word():
    db_ran_id = str(random.randint(193, 366))
    cursor.execute("SELECT word FROM words WHERE id = " + db_ran_id)
    word_db = cursor.fetchone()
    word = word_db[0]
    word = word.replace("\n", "")

    return str(word).lower()


    # Code For Gathering Words Online
# class HTMLParser(HTMLParser):
#     isCorrectTag = False
#
#     def error(self, message):
#         print("There is an error...")
#
#     def handle_starttag(self, tag, attrs):
#         if tag == "li":
#             HTMLParser.isCorrectTag = True
#
#     def handle_data(self, data):
#         if HTMLParser.isCorrectTag:
#             file = open("temp.txt", "at")
#             file.write(data+"\n")
#             file.close()
#
#             HTMLParser.isCorrectTag = False
#
#
# def download_words():
#     words_list_url = "http://www.manythings.org/vocabulary/lists/l/words.php"
#     request = requests.get(words_list_url)  # Make a get request to url
#
#     html_web = str(request.content)  # Get all html
#     parser = HTMLParser()  # Create object of parser
#     parser.feed(html_web)  # Scan through file
#
#     file = open("temp.txt", "rt")
#     word_list = file.readlines()
#
#     for word in word_list:
#         formula = "INSERT INTO words(word) VALUES('"+word+"')"
#         cursor.execute(formula)
#         wordsDB.commit()
#
#         print("Successfully stored :"+word)
