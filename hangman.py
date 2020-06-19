# A simple hangman game written in python
import random
print("Welcome to HangMan")
word_list = ["Youva","Jupyter","Speed","Function"]
word = list(random.choice(word_list))
guess_word = ['*']*len(word)
guess_count = len(word)+2
score = 0
while(('*' in guess_word) and guess_count>0):
    print("Word:%s \tscore:%d \tguesses left:%d"%(''.join(guess_word),score,guess_count))
    letter = input("Enter next character:")
    guess_count-=1
    if(letter in word):
        score += word.count(letter)
        for idx in range(len(word)):
            if word[idx] == letter:
                guess_word[idx] = letter
    if('*' not in guess_word):
        print("Congratulations!! you guessed the word:%s correctly!"%(''.join(guess_word)))
        break
else:
    print("Sorry you ran out of guesses :(( word was:%s"%(''.join(word)))
