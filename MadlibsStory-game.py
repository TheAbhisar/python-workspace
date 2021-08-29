matrix=""
system=""
neo=""
print("Hi!User.")
print("Please tell me your name.")
neo=input("your name\n")
print("Hello! " + neo)
matrix=input("What would you like to know about?\n")
system = input("What noun would you like to categorise" + matrix + "as?\n")
enemy = input("Give me an opposing noun to " + system)
inside = input("give me any relaxing noun\n")
profession = []
print("give me 4 professions related to " + system)
for i in range(4):
    prof = input("enter the profession")
    profession.append(prof)

save = input("\ngive me some helo-related verbs\n")
unplugged = input ("give me a verb that makes you think about relief\n")

adj = ["", ""]
print("give me 2 dystopian adjectives")
for i in range(2):
    adj[i] = input("dystopian adjective")

fight = input("\nenter a verb\n")

madlibsStory = (f"The {matrix} is a {system}, {neo}.That {system} is our {enemy}. " +
f"But when you're {inside}, you look around, what do you see? " +
f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. The very minds " +
f"of the people we are trying to {save}. But until we do, " +
f"these people are still a part of that {system} and that makes " +
f"them our {enemy}. You have to understand, most of these people " +
f"are not ready to be {unplugged}. And many of them are so {adj[0]}, " +
f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

# Print Story
print(madlibsStory)