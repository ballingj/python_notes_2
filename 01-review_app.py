"""
My attempt of Ardit Sulce's 'Say something' problem.  The program will loop until a secret word '\end' is entered. 
At the end, the program prints everything that was said.  Adding punctuation of period for statement or question mark if a question. 
"""
# my solution:
statement = ""
while True:
    sentence = input("Say Something: ")
    if sentence != "\end":
        if sentence.lower().find('how') == -1 and sentence.lower().find('when') == -1 and sentence.lower().find('what') == -1 and sentence.lower().find('who') == -1 and sentence.lower().find('why') == -1:
            statement +=  sentence.capitalize() + '. '
        else:
            statement += sentence.capitalize() + '? '
    else:
        break
print(statement)


# Ardit's solution

def sentence_maker(phrase):
    interrogatives = ("how", "when", "what", "why", "who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))


"""
# new to me is the .format method inserting variable into {}

jeff = "Jeff Ballinger"               
print(" My name is {}.".format(jeff))
 # output: My name is Jeff Ballinger.

"""