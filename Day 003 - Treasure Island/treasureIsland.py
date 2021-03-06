print('''
         __________
        /\____;;___\.
       | /         /
       `. ())oo() .
        |\(%()*^^()^\.
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

if direction == "left":
    action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across \n").lower()
    if action == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()
        if color == "yellow":
            print('''
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
          ''')
            print("You find the shiny, golden Treasure. You Win!")
        elif color == "red":
            print("You walk into a burning room. Game Over.")
        else:
            print("You get eaten by a blue dragon. Game Over.")
    else:
        print("You get eaten by a shark. Game Over.")
else:
    print("You fell into a hole. Game Over.")
