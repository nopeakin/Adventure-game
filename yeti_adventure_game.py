import time
import random


def main():
    items = []
    weapons = ["Great spear of Norway", "Antarctic blade", "Swedish sword"]
    your_weapon = random.choice(weapons)

    def print_pause(a):
        print(a)
        time.sleep(2)

    def valid_input1(prompt, option1, option2):
        while True:
            fight_run = input(prompt).lower()
            if option1 == fight_run:
                break
            elif option2 == fight_run:
                break
            else:
                print("Sorry, I don't understand.")
        return fight_run

    def valid_input2(prompt, option1, option2):
        while True:
            cave_house = input(prompt).lower()
            if option1 == cave_house:
                break
            elif option2 == cave_house:
                break
            else:
                print("Sorry I don't understand.")
        return cave_house

    def valid_input3(prompt, option1, option2):
        while True:
            play_again = input(prompt).lower()
            if option1 == play_again:
                break
            elif option2 == play_again:
                break
            else:
                print("Sorry I don't understand.")
        return play_again

    def intro():
        print_pause("You find yourself standing in an open plain.")
        print_pause("with patches of snow and brush on the horizon.")
        print_pause("There's a yeti in the vicinity that has been terrorizing")
        print_pause("the villagers and you have been sent to investigate.")
        print_pause("In front of you is an ancient house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand you hold a small dagger,")
        print_pause("most effective against smaller opposition.")

    def house():
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens...")
        print_pause("and out steps the yeti.")
        print_pause("Yoink this is the Yeti's house!")
        print_pause("The Yeti attacks you!")

        fight_run = valid_input1("Press 1 to fight. "
                                 "Press 2 to run.\n",
                                 "1", "2")
        if your_weapon in items:
            if fight_run == '1':
                print_pause("As the yeti moves to attack")
                print_pause("you raise your weapon.")
                print_pause("The yeti takes one look at your")
                print_pause("powerful weapon and runs away!")
                print_pause("Congratulations!")
                print_pause("You have rid the town of the Yeti.")

            elif fight_run == '2':
                print_pause("You run back into the field.")
                print_pause("Luckily, you don't appear to have been followed.")
                choose_action()

        else:
            if fight_run == '1':
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the Yeti")
                print_pause("you have been defeated")

            elif fight_run == '2':
                print_pause("You run back into the field.")
                print_pause("Luckily, you don't appear to have been followed.")
                choose_action()

    def cave():

        if your_weapon in items:
            print_pause("You have already picked up the weapon and")
            print_pause("there is nothing else here.")
            print_pause("You walk back out to the plains")
            choose_action()

        else:
            print_pause("You peer cautiously into the cave.")
            print_pause("It turns out to be a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause("You have found the...")
            print_pause(your_weapon)
            print_pause("You replace your small dagger with the mighty weapon")
            print_pause("You walk back out to the plains.")

            items.append(your_weapon)
            choose_action()

    def choose_action():
        cave_house = valid_input2("Enter 1 to knock on the door of the house. "
                                  "Enter 2 to peer into the cave.\n",
                                  "1", "2")
        if cave_house == '1':
            house()
        elif cave_house == '2':
            cave()

    def again():
        play_again = valid_input3("Would you like to play again? "
                                  "Please answer 'yes' or 'no'.\n",
                                  "yes", "no")
        if play_again == "no":
            print_pause("Goodbye!")
            exit()

        elif play_again == "yes":
            print_pause("Restarting Game")
            main()

    def play_game():
        items = []
        intro()
        choose_action()
        again()

    play_game()


main()
