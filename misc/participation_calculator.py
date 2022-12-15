"""
Created on Wed Dec 14 17:02:10 2022

This program creates a database called 'participation.db', and reads from a CSV files, and
populates that database with entries from the CSV file. It does this process for two CSV files,
one with a list of articles and another with student and class information and class 
participation marks.

@author: FranksCodes
"""

#Import 'csv' to read CSV files and sqlite3 to edit the database
import csv
import sqlite3

#Connect to PGR database
connection = sqlite3.connect('participation.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

#Create participation tables "articles", "semester", "students", "entries"
create_table = '''DROP TABLE IF EXISTS articles; CREATE TABLE articles(
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "shortname" TEXT NOT NULL UNIQUE,
                "fullname" TEXT NOT NULL UNIQUE);

                DROP TABLE IF EXISTS semester; CREATE TABLE semester ( 
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "year_sem" TEXT UNIQUE);
                
                DROP TABLE IF EXISTS students; CREATE TABLE students (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "uid_no" TEXT NOT NULL UNIQUE);
                
                DROP TABLE IF EXISTS format; CREATE TABLE format (
                    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                    "format" TEXT NOT NULL UNIQUE);

                DROP TABLE IF EXISTS entries; CREATE TABLE entries(
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "student_id" INTEGER,
                "participate" BOOLEAN,
                "article_id" INTEGER,
                "semester_id" INTEGER,
                "format_id" INTEGE,
                "course_id" INTEGER);
                '''
cursor.executescript(create_table)

#populate "articles" table
insert_artname = "INSERT OR IGNORE INTO articles (shortname, fullname) VALUES ( ?, ? )"

fname = input('Input articles CSV file:')
if (len(fname) < 1): 
    fname = 'articles.csv'

#Open the CSV file
fh = open(fname, newline='') 

#Read the CSV file
contents = csv.reader(fh)

#populate table with articles
for row in contents:
    shortname = row[0]
    fullname = row[1]
    print(row)
    cursor.execute(insert_artname, ( shortname, fullname ))
connection.commit()


#Check results of Articles Table
res_arts = cursor.execute('''SELECT * FROM articles LIMIT 10''')
print(res_arts.fetchall())

#Success message and prompt to input the next CSV file.
print('\n Articles table populated. Please provide entries.')
fname = input('''Input 'participation' 'CSV file:''')
if (len(fname) < 1): 
    fname = 'participation.csv'

#Open the CSV file
fh = open(fname, newline='') 

#Read the CSV file
contents = csv.reader(fh)

#Variables for SQL insertion

#for insert semester data
insert_year_sem = "INSERT OR IGNORE INTO semester (year_sem) VALUES ( ? )"

#insert student data
insert_uid_no = "INSERT OR IGNORE INTO students (uid_no) VALUES ( ? )"

#insert format values
insert_format = "INSERT OR IGNORE INTO format (format) VALUES ( ? )"

#Insert participation values
insert_participate = "INSERT OR IGNORE INTO entries (student_id, participate, article_id, semester_id, format_id, course_id) VALUES ( ?, ?, ?, ?, ?, ? )"


#Get IDs for students, format, and semester
get_student_id = "SELECT id FROM students WHERE uid_no = ? "
get_semester_id = "SELECT id FROM semester WHERE year_sem = ?"
get_article_id = "SELECT id FROM article WHERE  = ? "
get_format_id = "SELECT id FROM format WHERE format = ? "

#Write rows of CSV to database
for row in contents:
    print(row)
#Identify row indices
    uid_no = row[0]
    oljar = row[1]
    rabbit = row[2]
    empath = row[3]
    fetish = row[5]
    logic = row[7]
    sober = row[11]
    hoss = row[12]
    haus = row[14]
    form = row[15]
    year_sem = row[16]
    course_id = row[17]
#add student uid to table 
    cursor.execute(insert_uid_no, ( uid_no, ) )
#add semester id to table 
    cursor.execute(insert_year_sem, ( year_sem, ) )
#add format id to table 
    cursor.execute(insert_format, ( form, ) )
#get student, uid, and format id
    cursor.execute(get_student_id, ( uid_no, ))
    student_id = cursor.fetchone()[0]
    cursor.execute(get_semester_id, ( year_sem, ))
    semester_id = cursor.fetchone()[0]
    cursor.execute(get_format_id, ( form, ))
    format_id = cursor.fetchone()[0]
#loop through the articles and mark participation in entries table
    arts = [oljar, rabbit, empath, fetish, logic, sober, hoss, haus]
    print(arts)
    article_id = 2
    for item in arts:
        if item == '1':
            cursor.execute(insert_participate, ( student_id, 1, article_id, semester_id, format_id, course_id ))
            article_id = article_id + 1
        else:
            cursor.execute(insert_participate, ( student_id, 0, article_id, semester_id, format_id, course_id ))
            article_id = article_id + 1
            continue

connection.commit()


#Check results of students table
res_student= cursor.execute('''SELECT * FROM students LIMIT 10''')
print(res_student.fetchall())
#Check results of format Table
res_format = cursor.execute('''SELECT * FROM format LIMIT 10''')
print(res_format.fetchall())
#Check results of semester table
res_semester = cursor.execute('''SELECT * FROM semester LIMIT 10''')
print(res_semester.fetchall())
#Check results of entries table
res_entries = cursor.execute('''SELECT * FROM entries LIMIT 10''')
print(res_entries.fetchall())

connection.close()

    
