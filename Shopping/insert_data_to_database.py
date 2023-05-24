# 2
from create_database import Database
from colorama import Fore

class InsertData(Database):
    """
    Receiving various information and adding it to the relevant files in the database
    Recaiving information such as:
        user information,
        user purchases, 
        user bank account info,
        etc.
      
    Args: 
        Database (class): The data table is available in that class(Database) and the receive information is entered into the tables in this class(Database)
    """
    
    def add_new_user_info(self):

        private_info = (self.email, self.password)

        self.database_info.execute(f"INSERT INTO UserInfo VALUES {private_info}")
        self.connect.commit()
      
        print(f"{Fore.GREEN + 'Your account has been created.' + Fore.RESET}")
    
    
    def add_user_bank_account_info(self, user_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_bank_account VALUES {user_info}")
        self.connect.commit()
    
    
    def add_women_clothing_info(self, women_clothe_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_women_clothe VALUES {women_clothe_info}")
        self.connect.commit()
    
    def add_men_clothing_info(self, men_clothe_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_men_clothe VALUES {men_clothe_info}")
        self.connect.commit()
    
    
    def add_food_info(self, food_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_food VALUES {food_info}") 
        self.connect.commit()
    
    
    def add_iphone_mobile_info(self, iphone_mobile_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_iphone_mobile VALUES {iphone_mobile_info}")
        self.connect.commit()
    
    
    def add_samsung_mobile_info(self, samsung_mobile_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_samsung_mobile VALUES {samsung_mobile_info}")
        self.connect.commit()
    
    
    def add_book_info(self, book_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_book VALUES {book_info}")
        self.connect.commit()
    
    
    def add_movie_info(self, movie_info):
        self.database_info.execute(f"INSERT INTO {self.new_email}_movie VALUES {movie_info}")
        self.connect.commit()