# 1 file
import sqlite3

class Database:
    """
    Create database
    Get user information and create a table realted to user information in the database
    
    Create table related to different parts of the shop in the database
    and saving the user's purchase the shop information in the database
    There is also the ability to remove purchases
    """ 
     
    
    def get_user_info(self, email, password):
        self.email = email.lower()
        self.password = password
        
        find_atsign = self.email.find("@")
        self.new_email = self.email[:find_atsign]
        
         
    def connect_database(self):
        self.connect = sqlite3.connect(r"temp\FoxStore.db")
        self.database_info = self.connect.cursor()
        self.create_user_info_table()
        
    
    def create_user_info_table(self):
        self.database_info.execute("CREATE TABLE IF NOT EXISTS UserInfo (Email VARCHAR(30), Password VARCHAR(30))")
        
    
    def create_user_bank_account(self):
        self.database_info.execute(f"DROP TABLE IF EXISTS {self.new_email}_bank_account")
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_bank_account (FirstName VARCHAR(30), LastName VARCHAR(30), Balance INTEGER)")
         
    
    def create_women_clothing_table_info(self):
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_women_clothe (Clothe VARCHAR(30), size INTEGER, Color VARCHAR(10),  Price INTEGER, NumberOfClothes INTEGER, ClotheID INTEGER)")
    
    
    def create_men_clothing_table_info(self):
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_men_clothe (Clothe VARCHAR(30), size INTEGER, Color VARCHAR(10),  Price INTEGER, NumberOfClothes INTEGER, ClotheID INTEGER)")
    
    
    def create_food_table_info(self):
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_food (NameFood VARCHAR(30), Price INTEGER, NumberOfFood INTEGER, FoodID INTEGER)")
    
    
    def create_iphone_mobile_table_info(self):
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_iphone_mobile (Brand VARCHAR(20), Model VARCHAR (20), Size_Inches INTEGER, Color VARCHAR(20), MemoryStorage_GB INTEGER, Price INTEGER, iPhoneID INTEGER)")
    
     
    def create_samsung_mobile_table_info(self):
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_samsung_mobile (Brand VARCHAR(20), Model VARCHAR (20), Size_Inches INTEGER, Color VARCHAR(20), MemoryStorage_GB INTEGER, Price INTEGER, SamsungID INTEGER)")
    
    
    def create_book_table_info(self):
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_book (BookName VARCHAR(30), Author VARCHAR(30), Price INTEGER, NumberOfBook INTEGER, BookID INTEGER)")
    
    
    def create_movie_table_info(self):
        self.database_info.execute(f"CREATE TABLE IF NOT EXISTS {self.new_email}_movie (MovieName VARCHAR(30), Genre VARCHAR(20), DateOfRelease INTEGER, RunTime INTEGER, Price INTEGER, MovieID INTEGER)")