name = input("Hi. What's your name? ")
age = input("And how old are you? ")
weigh = input("Okay, last question. How many kg do you weigh? ")

dogAge = int(age) / 7
age_sec = int(age) * 365 * 24* 60 * 60

print("\nDid you know that you're just %d in dog years?\n" % dogAge)
print("But you're also over %d seconds old.\n" % age_sec)
print("If a small child weere trying to get your attention, your name wouldbecome:")
print("%s" % name*5)
print("\nDid you know on the moon you would weight only %.1f pounds?" %float(float(weigh) / 6))
print("But on the sun, you'd weigh %.1f (but, ah... not for long).\n\n" %float(float(weigh) *27.1))
print("Press the enter key to exit.")



