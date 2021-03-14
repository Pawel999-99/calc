from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size

Window.size = (500, 700)

# Designate our .kv design file
Builder.load_file('calc2.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # Creating button pressing function
    def button_press(self, button):
        # Create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # Test for error first
        if "Error" in prior:
            prior = '' 

        # Determine if 0 is sitting there
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # Create Function to remove the last character in the textbox
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove the last item in the textbox
        prior = prior[:-1]
        # Output to the textbox
        self.ids.calc_input.text = prior

    # Create function to make textbox positive or negetive
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there's a '-' sign already
        if '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
        
    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split textbox by +
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1] :
            # Add decimal to the end of the text
            prior = f'{prior}.'
            # Output back to the text box
            self.ids.calc_input.text = prior

        elif '.' in prior:
            pass
        else:
            # Add decimal to the end of the text
            prior = f'{prior}.'
            # Output back to the text box
            self.ids.calc_input.text = prior

    # Create addition function
    def math_sign(self, sign):
        # Create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'

    # Create equals to function
    def equals(self):
        prior = self.ids.calc_input.text
        
        try:
            # Evaluate the math from the text box
            answer = eval(prior)
            # Output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"

        '''
        # Addition   --> inna wczesniejsza wersja
        if "+" in prior:
            num_list = prior.split('+')
            answer = 0.0

            # Loop thru our list
            for number in num_list:
                answer += float(number)

        self.ids.calc_input.text = f'{answer}'
        '''



class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()