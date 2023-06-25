#string concatenation
#If we want to create a sting that says "subscribe to ______"
#youtuber = "" # some string variable

# a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}"format(youtuber))
#print(f"subscribe to {youtuber}")
def main():

    adj = input("Adjective: ")

    verb1 = input("Verb: ")
    verb2 = input("Verb: ")
    famous_person = input("Famous Person: ")

    madlib = f"Computer programming is so {adj}! It makes me so exited all the time because\
        I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

    print(madlib)

main()
