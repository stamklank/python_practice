
from os import system
import locale
locale.setlocale( locale.LC_ALL, '' )

print( 
"""
                         __                                             
                        /  |                                            
 __   __   __   ______  $$ |  _______   ______   _____  ____    ______  
/  | /  | /  | /      \ $$ | /       | /      \ /     \/    \  /      \ 
$$ | $$ | $$ |/$$$$$$  |$$ |/$$$$$$$/ /$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |
$$ | $$ | $$ |$$    $$ |$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$    $$ |
$$ \_$$ \_$$ |$$$$$$$$/ $$ |$$ \_____ $$ \__$$ |$$ | $$ | $$ |$$$$$$$$/ 
$$   $$   $$/ $$       |$$ |$$       |$$    $$/ $$ | $$ | $$ |$$       |
 $$$$$/$$$$/   $$$$$$$/ $$/  $$$$$$$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$/ 


                                                                        """ 
    
 )

print( 
"""
    __               
  /  |              
 _$$ |_     ______  
/ $$   |   /      \ 
$$$$$$/   /$$$$$$  |
  $$ | __ $$ |  $$ |
  $$ |/  |$$ \__$$ |
  $$  $$/ $$    $$/ 
   $$$$/   $$$$$$/  

                                                                        """ 
    
 )




print( 
"""

/        |/      \ /  |  /  |/        | /      \ /  |
$$$$$$$$//$$$$$$  |$$ |  $$ |$$$$$$$$/ /$$$$$$  |$$ |
   $$ |  $$ |__$$ |$$  \/$$/ $$ |__    $$ \__$$/ $$ |
   $$ |  $$    $$ | $$  $$<  $$    |   $$      \ $$ |
   $$ |  $$$$$$$$ |  $$$$  \ $$$$$/     $$$$$$  |$$/ 
   $$ |  $$ |  $$ | $$ /$$  |$$ |_____ /  \__$$ | __ 
   $$ |  $$ |  $$ |$$ |  $$ |$$       |$$    $$/ /  |
   $$/   $$/   $$/ $$/   $$/ $$$$$$$$/  $$$$$$/  $$/ 
                                        
 
 This program will calculate your taxes over 2020... poorly so.
 Do NOT use this program to calculate your taxes, better yet, don´t use the program at all.

                                                                        """ 
    
 )

class Tax():
    def __init___(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income
    error_counter = 0
    check_info_counter = 0
    
    def pass_name(self):
        print("""
I am most confident you can handle this: what is your name?""")
        self.name = input()
        print("""
Welcome {}.""".format(self.name) )
        if self.check_info_counter > 0:
            self.check_information()
        else: 
            self.check_info_counter = 1 

    def pass_age(self):
        print("""
Your age please?""")
        try:
            val = int(input())
            if val > 64 or val < 18 and val > 0:
                print("""
Your age is currently unsupported.""")
                self.pass_age()
            elif val < 0:
                print("""
You have yet to be born, I don´t talk with the unborn.""")
                self.pass_age()

            else:
                print("""
There you go, you did it! Pat yourself on your back champ!""")
                self.age = val
                
                if self.check_info_counter > 1:
                    self.check_information()
                else: 
                    self.check_info_counter = 2 
                               
        except ValueError:
            print("""
I wish I got to learn how to count with letters, not everyone had this superior education you had. So if you don´t mind, your highness, please enter your age in a numerical fashion.""")
            self.pass_age()

    

    def pass_income(self):
        val = None
        print("""
Please enter your income:""")
        
        val = input()
        
        if val == "your income":
            if self.error_counter == 0:
                print("""
Haha very funny. Not.""")
                self.error_counter += 1
                
                self.pass_income()
            elif self.error_counter == 1:
                print("""
Still not funny...""")
                self.error_counter += 1
                self.pass_income()
            elif self.error_counter == 2:
                print("""
Listen here you little shit...""")
                self.error_counter += 1
                self.pass_income()
            else:
                print("""
Fuck you too""")
                self.pass_income()
                    
        else:
            
            try:
            
                val = int(val)
                if val < 0:
                    print("""
We don´t tax losses in our country... yet""")
                    self.pass_income()
                elif val < 20000:
                    self.income = val
                    print("""
*tries to hold laugh in* Ok.""")
                    if self.check_info_counter > 2:
                        self.check_information()
                    else: 
                        self.check_info_counter = 3 
                else:
                    self.income = val
                    if self.check_info_counter > 2:
                        self.check_information()
                    else: 
                        self.check_info_counter = 3 
                    


            except ValueError:
                try:
                    val = float(val)
                    if val < 0:
                        print("""
We don´t tax losses in our country...yet""")
                        self.pass_income()
                    else:
                        self.income = val
                        if self.check_info_counter > 2:
                            self.check_information()
                        else: 
                            self.check_info_counter += 1  
                        

                except ValueError:
                    print("""
You talentless dick, have you ever spent €{}- ?""".format(val))
                       
                    self.pass_income()
 
    def check_information(self):
        print("""1. Your name is {}.
2. Your age is {}.
3. Your income over 2020 is {}. 
Is this correct? Y,N,N1,N2,N3""".format(self.name, self.age, locale.currency(self.income, grouping=True)))
        val = input()

        if val.upper() == "Y":
            self.check_info_counter = 0
            print("""
Well done monkey brains!""")
        elif val.upper() == "N":
            self.check_info_counter = 0
            self.pass_name()
            self.pass_age()
            self.pass_income()
            self.check_information()
        elif val.upper() == "N1":
            self.pass_name()
            
        elif val.upper() == "N2":
            self.pass_age()
            
        elif val.upper() == "N3":
            self.pass_income()
            
        else:
            print("""
Are you fat? That wasn´t an option presented to you. No wonder your parents think you're a dissapointment. 
You can try again below you piece of shit:""")
            self.check_information()


    def calculate_tax(self):
        first_bracket = (0.3710*self.income)-2837
        first_bracket_max = (0.3710*21043)-2837
        second_bracket = 0.3710*(self.income - 21043) - (2837-(0.05977*(self.income-21043)))
        second_bracket_max = 0.3710*(68507 - 21043) - (2837-(0.05977*(68507-21043)))
        third_bracket = 0.4950 * (self.income - 68507)
        if self.income < 21044:
            print("""
You paid {} of taxes this year, you almost contributed to society in a meaningful way.""".format(locale.currency(first_bracket), grouping=True))
        
        elif self.income < 68508:
            print("""
You paid {} in 2020, the goverment is proud to deliver you its services.""".format(locale.currency(first_bracket_max+second_bracket), grouping=True))
        
        else:
            print("""
You paid {}, maybe consider tax fraud?""".format(locale.currency(first_bracket_max+second_bracket_max+third_bracket), grouping=True))         

            



        

        
        





user1 = Tax()
user1.pass_name()
user1.pass_age()
user1.pass_income()
user1.check_information()
user1.calculate_tax()

