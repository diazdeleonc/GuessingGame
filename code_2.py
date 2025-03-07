import random
#Do not remove the parameter from the main function
def main(random_number=None):
    #Do not remove line 4, 5, or 6
    if random_number is None:
        random_number = random.randint(1,10)
    
    #Your code starts here.
    #Remember your code needs to be outside the if statement
    print("\nWelcome to the Guessing Game")
    counter = 0
    while counter < 3:
        x = int(input("\nEnter your guess from one to ten: "))
    
        counter += 1
        if x == random_number:
            print("Hooray! You guessed the number: %s "%(random_number))
            break
            
        elif x > random_number:
            
            print("Your guess (%s) was a little too high. Try lower."%(x))
            
        elif x < random_number:
            print("Your guess (%s) was a little too low, Try higer ."%(x)) 
           
    if counter == 3:
            print("Your failed to guess the number (%s) in three attempts."%(random_number))
            
    


if __name__ == "__main__":
    main()
