# 10
from samsung_mobile_section import (
    SamsungMobile, women_clothing_info_list, men_clothing_info_list, 
    food_info_list, iphone_mobile_info_list, samsung_mobile_info_list
)
from pyfiglet import figlet_format
from tabulate import tabulate
from colorama import Fore
from time import sleep


book_id = 60000
        
books_info_list = [
    {"Book name": "Atomic Habits", "Author": "Jmaes Clear", "Price": 12, "Number of books": 1, "Book ID": str(book_id + 1)},
    {"Book name": "The lost words", "Author": "Robert Macfalane", "Price": 17.49, "Number of books": 1, "Book ID": str(book_id + 2)},
    {"Book name": "Dad, I want to hear your story", "Author": "Jefferey Mason", "Price": 11.95, "Number of books": 1, "Book ID": str(book_id + 3)},
    {"Book name": "Mom, I want to hear your story", "Author": "Jefferey Mason", "Price": 11.95, "Number of books": 1, "Book ID": str(book_id + 4)},
    {"Book name": "Atlantis", "Author": "Ignatius Donnelly", "Price": 13.95, "Number of books": 1, "Book ID": str(book_id + 5)},
    {"Book name": "Ginderella", "Author": "Amelia Carruthers", "Price": 16.99, "Number of books": 1, "Book ID": str(book_id + 6)},
    {"Book name": "Simple and Delicious Vegan", "Author": "Michaela Vais", "Price": 31.49, "Number of books": 1, "Book ID": str(book_id + 7)},
    {"Book name": "Black Window", "Author": "Ryan Green", "Price": 11.99, "Number of books": 1, "Book ID": str(book_id + 8)},
    {"Book name": "What Now?", "Author": "Jan Canty", "Price": 19.95, "Number of books": 1, "Book ID": str(book_id + 9)},
    {"Book name": "Mini Habits", "Author": "Stephen Guise", "Price": 22.99, "Number of books": 1, "Book ID": str(book_id + 10)},
    {"Book name": "Sleep Smarter", "Author": "Shawn Stevenson", "Price": 19.90, "Number of books": 1, "Book ID": str(book_id + 11)},
    {"Book name": "Love You More", "Author": "Kerry Kerr MacAvoy", "Price": 15.95, "Number of books": 1, "Book ID": str(book_id + 12)},
    {"Book name": "Bad Karma", "Author": "Paul Wilson", "Price": 13.95, "Number of books": 1, "Book ID": str(book_id + 13)},
    {"Book name": "Cold Kill", "Author": "Jack Oslen", "Price": 19.95, "Number of books": 1, "Book ID": str(book_id + 14)}
]

class Book(SamsungMobile):
    """
    Display information of books 
    and the possibility of buying books by the user

    Args:
        SamsungMobile (class): Information and purchase of Samsung phones
    """
    
    def books_table_info(self, books_info):
        """
        Book information is received and displayed to the user
        Args:
            books_info (list): information list of book
        """
        self.books_info = books_info
        
        books_title = [title for title in self.books_info[0]]
        new_books_information = []
        
        for book in self.books_info:
            new_books_information.append([data for data in book.values()])
        
        # Create book table
        print(figlet_format("Books Table"))
        print(tabulate(new_books_information, headers=books_title, tablefmt="double_grid"))
        
        
    def buy_book(self):
        """
        Dispaly the list of books information
        and selection and buying books by the user
        """
        
        while True:
            self.books_table_info(self.books_info)
            
            shape = "►"
            print(f"{Fore.RED + shape + Fore.RESET} if you want to go back, enter the word --> {Fore.GREEN + 'back' + Fore.RESET}")
            
            choose_book = input("Enter Book name or Book ID from the table: ").lower()
            user_order = list(filter(lambda data: data["Book name"].lower() == choose_book or data["Book ID"] == choose_book, self.books_info))
            
            if choose_book == "back":
                break
            elif len(user_order) == 0:
                print(f"{Fore.RED + 'The Book is not available...Enter a valid book' + Fore.RESET}\n")
                sleep(1)
            else:
                book_count = int(input(f"Sample: {Fore.RED + '2' + Fore.RESET}\nHow many books do you want? "))
                
                if book_count < 1:
                    book_count = 1
                
                new_user_order = [info for info in user_order[0].values()]
                new_user_order[2] *= book_count
                new_user_order[3] *= book_count
                
                self.paying_for_book(new_user_order)
                break
                          
            
    def paying_for_book(self, book_list_info):
        """
        Paying for the purchase of book if a bank account is available
        And if the account balance is sufficient for the purchase.
        adding purchase information to the database.
        
        Args:
            book_list_info (list): user purchase information
        """
        self.available_account = False
        
        try:
            # check availability account if self.create_bank_account == True  or is available | self.available_account convert to True
            self.available_account = self.create_bank_account
        except:
            pass
        
        print(f"{Fore.GREEN + 'Shopping in progress...'}")
        sleep(1)
        
        if self.available_account == False:
            print(f"{Fore.RED + 'The purchase was canceled !...First you need to create a bank account.' + Fore.RESET}")
        
        else:
            if book_list_info[2] <= self.account_balance["Balance"]:
                print(f"{Fore.GREEN + 'The purchase was made successfully !' + Fore.RESET}")
                self.add_book_info(tuple(book_list_info))
                
                # Decuting the purchase amount from ther user's bank account and database
                self.account_balance["Balance"] -= book_list_info[2]
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
                self.connect.commit()
                
            else:
                print(f"{Fore.RED + 'The purchase was not made...Account balance is not enough for purchase' + Fore.RESET}")      
            
    
    def purchased_book(self):
        """
        Get information about user purchase from the database
        and display it to the user
        """
        self.avilable_order = False
        
        titles_book = ["Book name", "Author", "Price", "Number Of Books", "Book ID"]
        read_data = f"SELECT * FROM {self.new_email}_book"
        purchase_information = self.database_info.execute(read_data).fetchall()
        
        self.books_order = []
        for purchase in purchase_information:
            self.books_order.append([info for info in purchase])
        
        if len(self.books_order) == 0:
            return f"{Fore.RED + 'There are no purchases available' + Fore.RESET}"
        else:
            print(tabulate(self.books_order, titles_book, tablefmt="double_grid")) 
            self.avilable_order = True
            print("-" * 90)