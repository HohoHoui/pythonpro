import shelve
import pickle
import _pickle as cPickle
import random

questions = [
	{"ans1" : "ant", "ans2" : "spider", "ans3" : "dragon fly", "cans": "ladybug",
        "question" : "what is the strongest bug? ",
        "explain" : "because spiders make a string."},
	
	{"ans1": "coffee", "ans2" : "coke", "ans3" : "milk", "cans" : "water",
        "question" : "what is my favorite drink?",
        "explain" : "because water is fundamental."},

	{"ans1" : "cookie", "ans2" : "candy", "ans3" : "jelly", "cans" : "chocolate",
        "question" : "what is my favorite snack?",
        "explain" : "because chocolate is my fav snack."}
]

with open("prob5.dat", "wb") as pickle_file:
	cPickle.dump(questions, pickle_file)

with open("prob5.dat", "rb") as pickle_file:
	questions = cPickle.load(pickle_file)
	sel_que = random.choice(questions)
	
	
print("question : ", end = "")
print(sel_que.get("question"))
print("answer1 : ", sel_que.get("ans1"))
print("answer2 : ", sel_que.get("ans2"))
print("answer3 : ", sel_que.get("ans3"))
print("answer4 : ", sel_que.get("cans"))

ans = input("What is answer? : ")
while True:
	if ans == sel_que.get("cans"):
		print("correct")
		break
	elif ans in [sel_que.get("ans1"), sel_que.get("ans2"), sel_que.get("ans3")]:
		print("wrong ans")
		print("answer is", sel_que.get("cans"), "\n", sel_que.get("explain"))
		break
	else:
		print("please type according to the format")
		ans = input("what is answer? : ")
		print()
pickle_file.close()

