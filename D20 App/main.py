import kivy
import pygame
import random
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import random

class Game(GridLayout):
    def __init__(self,**kwargs):
        super(Game,self).__init__(**kwargs)
        self.dice_needed = {20:0,6:0,4:0}
        self.menu()
    def menu(self):
        self.clear_widgets()
        self.cols=2
        for die in self.dice_needed:
            temp_die = Button(text='d'+str(die))
            temp_die.bind(on_press=self.roll_die_general)
            self.add_widget(temp_die)
            self.dice_needed[die] = temp_die
        custom_entry = TextInput(multiline=False)
        custom_entry.bind(on_text_validate=self.custom_roll)
        self.add_widget(custom_entry)

    def custom_roll(self,value):
        print('custom roll',value.text)
        string_value = str(value.text)
        try:
            self.roll_die_range(1,int(value.text))
        except:
            self.menu()
    def roll_die_range(self,instance,sides):
        print('roll die range',sides)
        roll = random.randint(1,sides)
        back_to_dice = Button(text='You rolled a '+str(roll)+'. Click this button to roll again')
        back_to_dice.bind(on_press=self.menu)
        self.clear_widgets()
        self.add_widget(back_to_dice)
    def roll_die_general(self,instance):
        for sides in self.dice_needed:
            if (self.dice_needed[sides] == instance):
                self.roll_die_range(1,sides)
                print(sides)
                return

class TestApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    TestApp().run()
