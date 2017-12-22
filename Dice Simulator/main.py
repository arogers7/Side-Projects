import kivy
import pygame
import random
import starwars
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import random

class Game(GridLayout):
    def __init__(self,**kwargs):
        super(Game,self).__init__(**kwargs)
        #this is a dictionary of the pre-set dice (D20, D6 and D4) which are the
        #ones most commonly needed. Their values are initialized to zero but
        #will be changed to the value of the instance of the buttons that correspond
        #to the number of sides
        self.dice_needed = {20:0,6:0,4:0}
        #null is passed because an instance and self needs to be passed when menu is called by a button
        self.menu('null')
    def menu(self,instance):
        self.clear_widgets()
        self.cols=2
        #this sets the dictionary of pre-set die sides to the value of the instance of each button
        for die in self.dice_needed:
            temp_die = Button(text='D'+str(die))
            temp_die.bind(on_press=self.roll_die_general)
            self.add_widget(temp_die)
            self.dice_needed[die] = temp_die
        #a text input section is created for rolls of a custom range
        custom_entry = TextInput(multiline=False)
        custom_entry.bind(on_text_validate=self.custom_roll)
        self.add_widget(custom_entry)
    def custom_roll(self,value):
        #this is used for text entry
        #if the user enters a number, a random number between 1 and that number is chosen
        #otherwise, we return to the menu screen
        try:
            self.roll_die_range(1,int(value.text))
        except:
            self.menu('null')
    def roll_die_general(self,instance):
        #the die that is pressed corresponds to the instance in the dictionary
        #of pre-numbered die (D20, D6, and D4). The die that is clicked is
        #matched to the number of sides that it has
        for sides in self.dice_needed:
            if (self.dice_needed[sides] == instance):
                #once the number of sides has beeen identified, the die is 'rolled'
                #with a number between 1 and the number of sides
                self.roll_die_range(instance,sides)
                return
    def roll_die_range(self,instance,sides):
        #the menu with all the die are cleared
        self.clear_widgets()
        #the die is rolled, a random number between 1 and the number of sides is generated
        roll = random.randint(1,sides)
        #the text on the button generated at this step will have the result of the roll listed on it
        button_text = "You rolled a "+str(roll)+'.\n\n'
        #this generates a fact, with sw[0] being true if it is usable and false
        #if not while sw[1] is the string generated
        sw_fact = starwars.fact()
        if (sw_fact[0]):
            button_text += sw_fact[1]
        back_to_dice = Button(text=button_text)
        #when pressed, the button returns you to the 'choose die' menu
        back_to_dice.bind(on_press=self.menu)
        self.add_widget(back_to_dice)

class DiceSim(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    DiceSim().run()
