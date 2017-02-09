def words(str):
  counts = dict()
  wordsZote = str.split()
  for i, word in enumerate(wordsZote):
      if word.isdigit():
        wordsZote[i] = int(word)

  for word in wordsZote:
    if word in counts:
      counts[word]+=1
    else:
      counts[word] = 1
  for key in counts:
    if key == " ":
      del counts[key]
    else:
      return counts
      
def main():
   return words
main()