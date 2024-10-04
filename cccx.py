import random

def main():
  
  quantity = [1, 1, 1, 2, 2, 2]
  tense = ["past", "present", "future", "past", "present", "future"]

  for i in range(len(quantity)):
     sentence = make_sentence(quantity[i], tense[i])
     print(sentence)
     
def get_determiner(quantity):
  if quantity == 1:
      words = ["a", "one", "the"]
  else: 
     words = ["some", "many", "the"]
  word = random.choice(words)
  return word

def get_noun(quantity):
  if quantity == 1:
     words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]     
  else:
     words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
  word = random.choice(words)
  return word  
  
def get_verb(quantity, tense):
  if tense == "past":
     words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]    
  elif tense == "present" and quantity == 1:
     words = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
  elif tense == "present" and quantity != 1:
     words =["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
  elif tense == "future":
     words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"] 
  word = random.choice(words)
  return word

def make_sentence(quantity, tense):
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  verb = get_verb(quantity, tense)
  phrase1 = get_prepositional_phrase(quantity)
  phrase2 = get_prepositional_phrase(quantity)
  adverb = get_adverb() 
  sentence = f"{determiner} {noun}, {phrase1}, {adverb} {verb} {determiner} {noun} {phrase2}." # added a comma for readability
  return sentence.capitalize()

def get_preposition():
  prepositions = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
  word = random.choice(prepositions)
  return word

def get_prepositional_phrase(quantity):
  preposition = get_preposition()
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  phrase = f"{preposition} {determiner} {noun}"
  return phrase

def get_adverb():
   """Return a randomly chosen adverb."""
   words = ["quickly", "slowly", "beautifully", "badly",
        "eagerly", "lazily", "happily", "sadly", "angrily", "calmly"]
   
   word = random.choice(words)
   return word


if __name__ == "__main__":
   main()