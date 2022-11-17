# ==========================================================
# 
# 
# name : Jules.HC
# date : 2022-11-17
# 
# last modification : 2022-11-17 by Jules.HC
# 
# ==========================================================

#import module
import argparse
from datetime import date

#add parse , --name, --file
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="write your name")
parser.add_argument("--file", help="write your output file")
args = parser.parse_args()

#variable
name = args.name
chemin = args.file
#ask user of the goal a this script
usefulness = input ("what is a goal of your script : ")
#detect extanstion
extension = chemin.split('.')[-1]
ext = ""

def write(ext, chemin, name, usefulness):
    
    #write in the file the acreditation
    today = date.today()
    f = open(chemin, "a")
    f.write(f"{ext} ==========================================================\n")
    f.write(f"{ext} \n")
    f.write(f"{ext} name : {name}\n")
    f.write(f"{ext} date : {today}\n")
    f.write(f"{ext} \n")
    f.write(f"{ext} last modification : {today} by {name}\n")
    f.write(f"{ext} Usefulness : {usefulness}\n")
    f.write(f"{ext} \n")
    f.write(f"{ext} ==========================================================")
    f.close()
    print("finish...")

#use_c use # for commentary
use_c = ["py", "rb"]
#use_b use // for commentary
use_b = ["java", "c", "cpp", "c#", "js", "php", "swift", "cs"]

for i in range(len(use_c)): 
    if use_c[i] == extension: ext = "#"

for i in range(len(use_b)): 
    if use_b[i] == extension: ext = "//"

#use write fonction
write(ext, chemin, name, usefulness)