print("Title of program: Encouragement bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append("I see that you are excited. That's cool!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("It doesn't mean that its over. Take a rest and put yourself back on a slingshot. You can do it!")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("Do you need someone to talk to? I may be a bot but I'll be here!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Your smile is beautiful. Keep smiling! It brightens up my day!")
      counter += 1


  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
