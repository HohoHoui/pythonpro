import pickle
import _pickle as cPickle
import shelve

print("Picling lists.")

variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

pickle_file = open("pickles1.dat", "wb")
cPickle.dump(variety, pickle_file)
cPickle.dump(shape, pickle_file)
cPickle.dump(brand, pickle_file)
pickle_file.close

pickle_file = open("pickles1.dat", "rb")
variety = pickle.load(pickle_file)
print("\nUnpickling lists.")
print(variety)
print(shape)
print(brand)
pickle_file.close

pickles = shelve.open("pickles2.dat")
print("\nShelving lists.\n")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]
pickles.sync()
pickles.close

pickles_file = open("pickles2.dat")
print("Retrieving the lists from a shelved file:")
for key in pickles.keys():
    print(key, "-", pickles[key])
pickles_file.close

print("\n")

while True:
    ans = input("Press the enter key to exit.")
    if ans == '':
        break
