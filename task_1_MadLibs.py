proper_noun = input("Input name (propar noun): ")
adjective = input("Input an adjective: ")
color = input("Input color: ")
animal = input("Input an animal: ")
place = input("Input a place: ")
adjective2 = input("Input an adjective: ")
magical_creature = input("Input a magical creature (plural): ")
adjective3 = input("Input an adjective: ")
magical_creature2 = input("Input a magical creature (plural): ")
room = input("Input room in a house: ")
noun = input("Input a noun: ")


template1 = f"""Dear {proper_noun}, I am writing to you from a {adjective} castle in an enchanted forest. 
            I found myself here one day after going for a ride on a {color} {animal} in {place}. 
            There are {adjective2} {magical_creature} and {adjective3} {magical_creature2} here! 
            In the {room} there is a pool full of {noun}."""

print("Text: ", template1)