import random

class Hangman:
    def __init__(self):
        ''' initialize variables '''
        self.guess = ''
        self.finish = False
        self.guessed_letters = []

    def draw_hangman(self, state):
        ''' function to draw hangman depending on the state '''
        self.draw_horizontal_bar()
        self.draw_double_pole()
        if state == 0: # draw empty scaffold
            for i in range(5):
                self.draw_single_pole()

        elif state == 1: # draw only head
            self.draw_hang_head()
            for i in range(4):
                self.draw_single_pole()

        elif state == 2: # draw only head and neck
            self.draw_hang_head()
            self.draw_double_pole()
            for i in range(3):
                self.draw_single_pole()

        elif state == 3: # draw only head, neck and left leg
            self.draw_hang_head()
            self.draw_double_pole()
            self.draw_hang_ll()
            for i in range(2):
                self.draw_single_pole()

        elif state == 4: # draw only head, neck and legs
            self.draw_hang_head()
            self.draw_double_pole()
            self.draw_hang_legs()
            for i in range(2):
                self.draw_single_pole()

        elif state == 5: # draw only head, neck, legs and left arm
            self.draw_hang_head()
            self.draw_hang_la()
            self.draw_hang_legs()
            for i in range(2):
                self.draw_single_pole()

        elif state == 6: # draw only head, neck, legs and arms
            self.draw_hang_head()
            self.draw_hang_arms()
            self.draw_hang_legs()
            for i in range(2):
                self.draw_single_pole()
            
    def print_hidden_secret(self, secret_word):
        ''' function to print secret word as hidden '''
        print('The secret word to guess is: ', '_' * len(secret_word))

    def add_guessed_letter(self, letter):
        ''' function to add the letter to the guessed_letters list if not added '''
        if letter in self.guessed_letters:
            print('You have already guessed the letter: ', letter)
            return False
        else:
            self.guessed_letters.append(letter)
            return True

    def check_guessed_letter(self, letter, secret_word):
        ''' function to check if the letter guessed exist in the secret_word or not '''
        if letter in secret_word:
            print('You guessed a correct letter: ', letter)
            return True
        else:
            print('The guessed letter is incorrect: ', letter)
            return False

    def print_guessed_word(self, secret_word):
        ''' function to recursively print the guessed word by user '''
        if len(secret_word): # if secret_word has letters left
            letter = secret_word[0] # select first letter of secret_word
            # check if letter exist in guessed letters, if yes, add it to guess
            if letter in self.guessed_letters:
                self.guess += letter
            # else add blank space to guess
            else:
                self.guess += '_'
            # call the same function with remaining words of secret_word
            return self.print_guessed_word(secret_word[1:])

        # if secret_word has no words left, check if there are any blanks in guess
        if '_' not in self.guess:
            # if no blanks, set finish to True to finish the hangman game
            self.finish = True

        # save the word to return it
        guessed_word = self.guess

        # reset the user guess
        self.guess = ''
        return guessed_word

    def draw_hang_arms(self):
        ''' function to print arms '''
        print("|        /|\\   ")

    def draw_hang_la(self):
        ''' function to print left arm '''
        print("|         |\\   ")

    def draw_hang_legs(self):
        ''' function to print legs '''
        print("|        / \\   ")

    def draw_hang_ll(self):
        ''' function to print left leg '''
        print("|          \\   ")

    def draw_hang_head(self):
        ''' function to print head '''
        print("|         0    ")

    def draw_horizontal_bar(self):
        ''' function to print platform bar '''
        print(" _________     ")
        
    def draw_double_pole(self):
        ''' function to print two poles '''
        print("|         |    ")

    def draw_single_pole(self):
        ''' function to print one pole '''
        print("|              ")


class EasierHangman(Hangman):
    ''' class for easier mode of hangman using inheritance, 
        where description of secret_word is shown '''
    def __init__(self, description):
        ''' initialize variable for parent class and then base class'''
        super().__init__()
        self.description = description

    def print_hidden_secret(self, secret_word):
        ''' function first shows the description of the secret_word as a hint, 
            and then calls the method from parent class'''
        super().print_hidden_secret(secret_word)
        print('Hint for you: ', self.description)

def main():
    play = True
    # create a list of different words to guess
    words_list = ['hello', 'goodbye', 'welcome', 'university', 'music', 'spotify']

    # link description to those words for easier mode
    description_list = {'hello': 'Used to say when meeting someone', 
                        'goodbye': 'Used to say when leaving someone', 
                        'welcome': 'Said as a response to thank you', 
                        'university': 'Place to study for higher levels',
                        'music': 'You listen to it',
                        'spotify': 'A software to listen music'}
    # sort the words to store them as in a dictionary 
    words_list = sorted(words_list)

    # play until user wants to
    while play:
        # randomly choose one of the word as secret_word
        secret_word = random.choice(words_list)

        # ask user to choose between easy and hard mode
        try:
            easier_mode = int(input('Do you want to play Easy or Hard mode: 1 for easy, 2 for hard: '))
            if easier_mode == 1:
                # make the hangman object
                hangman = EasierHangman(description_list[secret_word])

            elif easier_mode == 2:
                # make the easier hangman object
                hangman = Hangman()

            else:
                print('You entered incorrect input, try playing again.')
                break

        except:
            print('You entered incorrect input, try playing again.')
            break
        
        

        # starting state is 0, and losing state is 6 for hangman
        state = 0
        losing_state = 6
        print()

        # draw the empty hangman
        hangman.draw_hangman(state)
        hangman.print_hidden_secret(secret_word)

        # while the user has not guessed all letters and current state has not reached losing state
        while not hangman.finish and state != losing_state:
            # ask user for a letter and lower case
            letter = input('Please input a letter: ')
            letter = letter.lower()

            # add the letter to guessed list
            if hangman.add_guessed_letter(letter):
                # if letter is added, check if the letter is present in secret_word or not
                success = hangman.check_guessed_letter(letter, secret_word)

            # print the guessed_letters user has input
            print('Letters guessed so far: ', hangman.guessed_letters)

            # print the guessed_word by user
            guessed_word = hangman.print_guessed_word(secret_word)
            print('Guessed Word: ', guessed_word)

            # if the guessed letter is not in secret_word, increase the current state by 1, when current state reaches losing state, the user lost game
            if not success:
                state += 1

            # draw the hangman depending on the state
            hangman.draw_hangman(state)

            # print the remaining incorrect guesses user has left
            print('Total incorrect guesses left = ', losing_state - state)
            print()

        # the game has ended
        print('-' * 10)
        # if user finished the hangman, he won, else he lost
        if hangman.finish:
            print('You won!!!')
        else:
            print('You lost!!!')

        # print the secret word and the guessed word
        print('The secret word was: ', secret_word)
        print('You guessed: ', guessed_word)

        # ask user t play again
        play_again = input('Do you want to play again? (Y/N): ')
        if play_again.lower() != 'y':
            play = False

    # wait for user to to press any key to close window
    input()
main()
