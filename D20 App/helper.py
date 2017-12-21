import random

class Results(GridLayout):
    def __init__(self,oldself,results):
        self.build(oldself,results)
    def build(self,oldself,die_results):
        self.cols = 1
        result = Button(text='you rolled a '+str(die_results)+'. Click to roll again')
        result.bind(on_press=self.to_home)
        print('build')
        oldself.add_widget(result)
        return result
    def to_home(self,instance):
        return ChooseDie().build()

def roll_die_range(self,sides):
    total = random.randint(1,sides)
    print(total)
    return Results(self,total)

class ChooseDie(GridLayout):
    def __init__(self):
        super(ChooseDie,self).__init__()
        app = self
        self.build()
    def build(self):
        self.clear_widgets()
        self.add_widget(Label(text="test"))
        """
        self.clear_widgets()
        d20 = Button(text='d20')
        d20.bind(on_press=self.roll_d20)
        self.cols=2
        self.add_widget(d20)
        """
    def roll_d20(self,instance):
        self.clear_widgets()
        return roll_die_range(self,20)



class TestApp(App):
    def build(self):
        return ChooseDie()
