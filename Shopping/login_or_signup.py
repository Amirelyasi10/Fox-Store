# 3
from insert_data_to_database import InsertData
from colorama import Fore

class Login(InsertData): 
    """
    The availability of user accounts in the database is checked
    And the user account will be logged in or signed up.

    Args:
        InsertData (class): Send user account info for InsertData 
        And InsertData stores user info in the database
    """
     
    def account_login_check(self):
        read_users_info = "SELECT * FROM UserInfo"
        users_info_list = self.database_info.execute(read_users_info)
                 
        self.Login = False
        for info in users_info_list:
            count = 0
            if self.email.lower() in info:
                count += 1
            if self.password in info:
                count +=1
            
            # Checking the presence of account information in the database
            if count == 2:
                print(f"{Fore.CYAN + 'Login to your account completed.' + Fore.RESET}")
                
                # Login user account
                self.Login = True
                break
        else:
            print(f"{Fore.RED + 'Invalid Login...This account does not exist.' + Fore.RESET}")
    
    def check_account_registration(self):
        read_users_info = "SELECT * FROM UserInfo"
        users_info_list = self.database_info.execute(read_users_info)
        
        self.sign_up = False
        for info in users_info_list:
            count = 0
            correct_email = 0
            
            if self.email in info:
               count += 1
               correct_email += 1
            if self.password in info:
                count +=1
            
            if correct_email == 1:
                print(f"{Fore.RED + 'Email is already registtered.' + Fore.RESET}")
                break
        else:
            self.add_new_user_info()
            self.sign_up = True
            
            # Create tables in database
            self.create_women_clothing_table_info()
            self.create_men_clothing_table_info()
            self.create_food_table_info()
            self.create_iphone_mobile_table_info()
            self.create_samsung_mobile_table_info()
            self.create_book_table_info()
            self.create_movie_table_info()