# 13
from delete_data import (
    RemoveData, women_clothing_info_list, men_clothing_info_list, 
    food_info_list, iphone_mobile_info_list, samsung_mobile_info_list, 
    books_info_list, movies_info_list
)
from tabulate import tabulate
from colorama import Fore
from pyfiglet import figlet_format
from time import sleep


class UserAccount(RemoveData):
    """
    Create user profile and display user information
    Receiving information from the user and checking its validity
    
    Args:
        RemoveData (class): Remove data a from database
    """
    
    def user_profile(self):
        """
        User full information
        """
        titles = ["Email", "Password"]
        user_info = [[self.email, self.password]]
        
        print(tabulate(user_info, headers=titles, tablefmt="double_grid"))
    
    
    def get_user_email(self):
        """
        email is received from the user
        and its validity checkl
        """
        
        while True:
                
            email = input("\nsample: Microsoft10@gmail.com\nEnter your email: ")
            
            capital_letter = [letter for letter in email if letter.isupper()]
            small_letter = [letter for letter in email if letter.islower()]
            numbers = [number for number in email if number.isnumeric()]
            symbols = list("{}[]<>?/\-*+=-()&^%#~:;,")
            

            if " " not in email:
                if len(email) > 15:
                    if len(capital_letter) >= 1:
                        if len(small_letter) >= 1:
                            if len(numbers) >= 1:
                                letters = [letter for letter in email if letter in symbols] 
                                if len(letters) == 0: 
                                    if email.endswith("@gmail.com") or email.endswith("@email.com"):                                       
                                        self.user_email = email
                                        break
                                    
                                    else:
                                        print("email must contain @gmail.com")    
                                else:
                                    print("There be should be not invalid symbol in the email")
                            else:
                                print("There must be a number in the email")    
                        else:
                            print("There must be a lowercase letter in the email") 
                    else:
                        print("There must be a capital letter in the email")                               
                else:
                    print("email must have more than 15 characters")                            
            else:
                print("There should be no space in the email") 
        
    
    def get_user_password(self):
        """
        password is received from the user
        and its validity check
            
        Args:
        password (string): user password
        """ 
                      
        while True:
                
            password = input("\nsample: Microsoft10\nEnter your password: ")
            
            capital_letter = [letter for letter in password if letter.isupper()]
            small_letter = [letter for letter in password if letter.islower()]
            numbers = [number for number in password if number.isnumeric()]
            symbols = list("{}[]<>?/\-*+=()&^%#~:;,")
        
            
            if " " not in password:
                if len(password) > 10:
                    if len(capital_letter) >= 1:
                        if len(small_letter) >= 1:
                            if len(numbers) >= 1:
                                letters = [letter for letter in password if letter in symbols] 
                                if len(letters) == 0:                                        
                                        self.user_password = password
                                        break
                                        
                                else:
                                    print("There be should be not invalid symbol in the password")
                            else:
                                print("There must be a number in the password")    
                        else:
                            print("There must be a lowercase letter in the password") 
                    else:
                        print("There must be a capital letter in the password")                               
                else:
                    print("password must have more than 10 characters")                            
            else:
                print("There should be no space in the password") 
                
                
    def check_availability_bank_account(self):
        """
        Checking whether the user already has a bank accoung or not
        If he already has a bank account , we will apply it.
        Returns:
            bool: Determining the result of having or not having a bank accountt
        """
        try:
            read_bank_account_info = f"SELECT * FROM {self.new_email}_bank_account"
            all_data = self.database_info.execute(read_bank_account_info)
            
            self.user_account = ""
            for data in all_data:
                self.user_account = data
                return True
        
        except:
            pass
    
    
    def show_user_order(self):
        """
        Displaying user purchase order in different sections
        """
        while True:
            order_sections = [
                "Women's clothing orders", "men's clothing orders", "Food orders", "iPhone phone orders", "Samsung phone orders", "Book orders", "Movie oreders", "All orders", "Delete an order", "Back"
            ]
            print(f"\n#---------- Fox Store orders section ----------#")
            
            number = 1
            for section in order_sections:
                print(f"[{Fore.GREEN + str(number) + Fore.RESET}] {section}")
                number += 1 
                    
            choose_order = input("\nSample: 1\nEnter an section order: ").lower()
            if choose_order in ["1", "women's clothing orders"]:
                self.purchased_women_clothing()
                if self.avilable_order == False: print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                    
            elif choose_order in ["2", "men's clothing orders"]:
                self.purchased_men_clothing()
                if self.avilable_order == False: print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                    
            elif choose_order in ["3", "Food orders"]:
                self.purchased_food()
                if self.avilable_order == False: print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                    
            elif choose_order in ["4", "iPhone phone orders"]:
                self.purchased_iphone_mobile()
                if self.avilable_order == False: print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                    
            elif choose_order in ["5", "Samsung phone orders"]:
                self.purchased_samsung_mobile()
                if self.avilable_order == False: print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                
            elif choose_order in ["6", "Book orders"]:
                self.purchased_book()
                if self.avilable_order == False: print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                
            elif choose_order in ["7", "Movie oreders"]:
                self.purchase_movie()
                if self.avilable_order == False: print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                
            elif choose_order in ["8", "All orders"]:
                all_orders = [
                    self.purchased_women_clothing, self.purchased_men_clothing, self.purchased_food, 
                    self.purchased_iphone_mobile, self.purchased_samsung_mobile, 
                    self.purchased_book, self.purchase_movie
                ]
                count_availabe_order = 0
                for order in all_orders:
                    order()
                    if self.avilable_order:
                        count_availabe_order += 1
                else:   
                    if count_availabe_order == 0:            
                        print(f"{Fore.RED + 'There is no order available' + Fore.RESET}")
                
            elif choose_order in ["9", "delete an order"]:
                self.delete_orders()
                
            elif choose_order in ["10", "back"]:
                break
            
            else:
                print("Enter a valid value...")
            sleep(1)
                
                
    def delete_orders(self):
        """
        Deleting an order from the user's order list and database
        """
        while True: 
            print(f"{Fore.RED + shape + Fore.RESET} if you want to go back, enter the word --> {Fore.GREEN + 'back' + Fore.RESET}")
            print(f"{Fore.RED + shape + Fore.RESET} if you want to delete an order, enter the --> {Fore.GREEN + ' your order ID' + Fore.RESET}\tSample:24231")
            order_id = input("Enter order ID: ").lower()
            
            if order_id == "back":
                break
            elif not order_id.isdigit():
                print("Enter valid value...Enter back or order id.\n")
                continue
            
            order_id = int(order_id)
                
            # Ccheck order id and delete an order
            self.delete_women_clothing_order(order_id)
            if self.delete_order: break
            
            self.delete_men_clothing_order(order_id)
            if self.delete_order: break
                
            self.delete_food_order(order_id)
            if self.delete_order: break
                
            self.delete_iphone_mobile_order(order_id)
            if self.delete_order: break
                
            self.delete_samsung_phone_order(order_id)
            if self.delete_order: break
                
            self.delete_book_order(order_id)
            if self.delete_order: break
                
            self.delete_movie_order(order_id)
            if self.delete_order: break
                
            
            if self.delete_order == False:
                print(f"{Fore.RED + 'This order does not exists' + Fore.RESET}")
            
            
# Instance | Object
user = UserAccount()

# Login or Sig up
while True:
    shapes = "-" * 20
    print(figlet_format("Fox  Store"))
    print(f"{Fore.GREEN + 'Welcom to Fox Store' + Fore.RESET}")
    print(f"{Fore.RED + shapes + Fore.RESET}")
    
    options = ["Login", "Sign up", "Exit"]
    shape = "►"
    
    for option in options:
        print(f"{Fore.RED + shape + Fore.RESET} {option}")
      
    run_web = True  
    choose_option = input("Enter an option: ").lower()
    
    if choose_option == "login":
        user.get_user_email()
        user.get_user_password()
        user.get_user_info(user.user_email, user.user_password)
        user.connect_database()
        user.create_user_info_table()
        user.account_login_check()
       
        if user.Login: # IF True --> Break
            break
    
    elif choose_option == "sign up":
        user.get_user_email()
        user.get_user_password()
        user.get_user_info(user.user_email, user.user_password)
        user.connect_database()
        user.create_user_info_table()
        user.check_account_registration()
        
        if user.sign_up:
            break
    
    elif choose_option == "exit":
        print(f"{Fore.GREEN + 'Have a nice day :)' + Fore.RESET}")
        run_web = False 
        break
        
    else:
        print(f"{Fore.GREEN + 'Enter a valid option...' + Fore.RESET}")
    sleep(1)
sleep(1)


# Check the availability of a bank account
check_user_account = user.check_availability_bank_account()

create_account = 0
# Use Fox Store services
if run_web:
    
    options = ["My profile", "Create bank account", "Women's Clothing", "Men's Clothing", "Food", "iPhone Phone", "Samsung Phone", "Book", "Movie", "My Order List", "About Us", "Exit"]
    while True:
        
        try:
            # If the bank account is already available, there is no need to create a new account
            if check_user_account and create_account == 0:  
                options[1] = "My bank account"
                user.user_private_account(user.user_account[0], user.user_account[1], user.user_account[2])
                create_account += 1
        except:
            pass

        if options[1] == "Create bank account":
            print(f"\n{Fore.RED + 'Note: To buy and use the services of the Fox Store, you must create a bank account' + Fore.RESET}")
        print(f"\n#---------- Fox Store Services ----------#")
        
        number = 1
        for option in options:
            print(f"[{Fore.RED + str(number) + Fore.RESET}] {option}")
            number += 1 
                
        choose_option = input("\nSample: 1\nEnter an option: ").lower()
        if choose_option in ["1", "my profile"]:
            user.user_profile()
                
        elif choose_option in ["2", "create bank account", "my bank account"]:
                
            if options[1] == "Create bank account":
                your_name = input("Enter your name: ")
                your_last_name = input("Enter your last name: ")
                    
                print(user.user_private_account(your_name, your_last_name))
                    
                options[1] = "My bank account"
                
            else:
                user.account_services()
                
        elif choose_option in ["3", "women's clothing"]:        
            while True:
                user.women_clothe_table_info(women_clothing_info_list)
                    
                question = input("Do you want to buy clothes(yes/no)? ").lower()
                if question == "yes":
                    user.buy_women_clothe()
                    break
                elif question == "no":
                    break
                else:
                    print("Enter valid value...yes or no.")
                        
        elif choose_option in ["4", "men's clothing"]:
            while True:
                user.men_clothe_table_info(men_clothing_info_list)
                    
                question = input("Do you want to buy clothes(yes/no)? ").lower()
                if question == "yes":
                    user.buy_men_clothe()
                    break
                elif question == "no":
                    break
                else:
                    print("Enter valid value...yes or no.")
            
        elif choose_option in ["5", "food"]:
            while True:
                user.food_table_info(food_info_list)
                
                question = input("Do you want to buy food(yes/no)? ").lower()
                if question == "yes":
                    user.buy_food()
                    break
                elif question == "no":
                    break
                else:
                    print("Enter valid value...yes or no.")
                    
            
        elif choose_option in ["6", "iphone phone"]:
            while True:
                user.iphone_table_info(iphone_mobile_info_list)
                
                question = input("Do you want to buy iPhone phone(yes/no)? ").lower()
                if question == "yes":
                    user.buy_iphone_mobile()
                    break
                elif question == "no":
                    break
                else:
                    print("Enter valid value...yes or no.")
                
        elif choose_option in ["7", "samsung phone"]:
            while True:
                user.samsung_table_info(samsung_mobile_info_list)
                
                question = input("Do you want to buy Samsung phone(yes/no)? ").lower()
                if question == "yes":
                    user.buy_samsung_mobile()
                    break
                elif question == "no":
                    break
                else:
                    print("Enter valid value...yes or no.")
                
            
        elif choose_option in ["8", "book"]:
            while True:
                user.books_table_info(books_info_list)
                
                question = input("Do you want to buy book(yes/no)? ").lower()
                if question == "yes":
                    user.buy_book()
                    break
                elif question == "no":
                    break
                else:
                    print("Enter valid value...yes or no.")
                    
        elif choose_option in ["9", "movie"]:
            while True:
                user.movie_table_info(movies_info_list)
                
                question = input("Do you want to buy movie(yes/no)? ").lower()
                if question == "yes":
                    user.buy_movie()
                    break
                elif question == "no":
                    break
                else:
                    print("Enter valid value...yes or no.")
            
        elif choose_option in ["10", "my order list"]:
            
            if options[1] == "Create bank account":
                print("There is no purchase available")
            else: 
                user.show_user_order() 
            
        elif choose_option in ["11", "About Us"]:
            
            with open(r"temp\AboutUs.txt", encoding="UTF-8") as website_info:
                print(website_info.read())
                sleep(1)
        
        elif choose_option in ["12", "exit"]:
            print(f"{Fore.GREEN + 'Have a nice day :)' + Fore.RESET}")
            user.connect.close()
            break
            
        else:
            print("Enter a valid value...")

        sleep(1)