# 11
from book_section import (
    Book, women_clothing_info_list, men_clothing_info_list, food_info_list, 
    iphone_mobile_info_list, samsung_mobile_info_list, books_info_list
)
from pyfiglet import figlet_format
from tabulate import tabulate
from colorama import Fore
from time import sleep

movie_id = 70000
        
movies_info_list = [
    {"Movie name": "Martin Roumagnac", "Genre": "Drama", "Date of relese": 1946, "Run time(minutes)": 108, "price": 25.49, "Movie ID": str(movie_id + 1)},
    {"Movie name": "Detectorists", "Genre": "Tv comedy", "Date of relese": 2023, "Run time(minutes)": 612, "price": 55.99, "Movie ID": str(movie_id + 2)},
    {"Movie name": "A Man called Otto", "Genre": "Comedy, Drama", "Date of relese": 2022, "Run time(minutes)": 128, "price": 24.99, "Movie ID": str(movie_id + 3)},
    {"Movie name": "The Lost City", "Genre": "Comedy, Action", "Date of relese": 2022, "Run time(minutes)": 130, "price": 16.99, "Movie ID": str(movie_id + 4)},
    {"Movie name": "The Whale", "Genre": "Drama", "Date of relese": 2022, "Run time(minutes)": 117, "price": 15.99, "Movie ID": str(movie_id + 5)},
    {"Movie name": "Jesus Revolution", "Genre": "Drama", "Date of relese": 2023, "Run time(minutes)": 120, "price": 23.99, "Movie ID": str(movie_id + 6)},
    {"Movie name": "One Upon A Time In Hollywood", "Genre": "Comedy, Drama", "Date of relese": 2019, "Run time(minutes)": 162, "price": 12.74, "Movie ID": str(movie_id + 7)},
    {"Movie name": "Groundswell", "Genre": "Drama", "Date of relese": 2022, "Run time(minutes)":84, "price": 11.99, "Movie ID": str(movie_id + 8)},
    {"Movie name": "Kung Fu Yoga", "Genre": "Action", "Date of relese": 2017, "Run time(minutes)": 107, "price": 17.49, "Movie ID": str(movie_id + 9)},
    {"Movie name": "Johnny English Strikes Again", "Genre": "Comedy", "Date of relese": 2018, "Run time(minutes)": 88, "price": 10.99, "Movie ID": str(movie_id + 10)},
    {"Movie name": "M3GAN", "Genre": "Horror", "Date of relese": 2022, "Run time(minutes)": 102, "price": 25.49, "Movie ID": str(movie_id + 11)},
    {"Movie name": "Jeepers Creepers", "Genre": "Horror", "Date of relese": 2022, "Run time(minutes)": 88, "price": 20.99, "Movie ID": str(movie_id + 12)},
    {"Movie name": "Infinity Pool", "Genre": "Horro", "Date of relese": 2023, "Run time(minutes)": 118, "price": 12.99, "Movie ID": str(movie_id + 13)},
    {"Movie name": "The Pursuit Of Happyness", "Genre": "Drama", "Date of relese": 2006, "Run time(minutes)": 117, "price": 13.99, "Movie ID": str(movie_id + 14)}

]

class Movie(Book):
    """
    Display information of Movies 
    and the possibility of buying movies by the user

    Args:
        Book (class): Information and purchase of Books
    """
    
    def movie_table_info(self, movies_info):
        """
        Movie information is received and displayed to the user
        Args:
            movies_info (list): Information list of movies
        """
        self.movies_info = movies_info
        
        movie_title = [title for title in self.movies_info[0]]
        new_books_information = []
        
        for book in self.movies_info:
            new_books_information.append([data for data in book.values()])
        
        # Create book table
        print(figlet_format("Movies Table"))
        print(tabulate(new_books_information, headers=movie_title, tablefmt="double_grid"))
        
        
    def buy_movie(self):
        """
        Dispaly the list of Movies information
        and selection and buying Movies by the user
        """
        while True:
            self.movie_table_info(self.movies_info)
            
            shape = "►"
            print(f"{Fore.RED + shape + Fore.RESET} if you want to go back, enter the word --> {Fore.GREEN + 'back' + Fore.RESET}")
            
            choose_movie = input("Enter Movie name or Movie ID from the table: ").lower()
            user_order = list(filter(lambda data: data["Movie name"].lower() == choose_movie or data["Movie ID"] == choose_movie, self.movies_info))
            
            if choose_movie == "back":
                break
            elif len(user_order) == 0:
                print(f"{Fore.RED + 'The Movie is not available...Enter a valid Movie' + Fore.RESET}\n")
                sleep(1)
            else:
                new_user_order = [info for info in user_order[0].values()]
                
                self.paying_for_movie(new_user_order)
                break
            
        
    def paying_for_movie(self, movie_list_info):
        """
        Paying for the purchase of Movie if a bank account is available
        And if the account balance is sufficient for the purchase.
        adding purchase information to the database.

        Args:
            movie_list_info (list): User purchase inromation
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
            if movie_list_info[4] <= self.account_balance["Balance"]:
                print(f"{Fore.GREEN + 'The purchase was made successfully !' + Fore.RESET}")
                self.add_movie_info(tuple(movie_list_info))
                
                # Decuting the purchase amount from ther user's bank account and database
                self.account_balance["Balance"] -= movie_list_info[4]
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
                self.connect.commit()
                
            else:
                print(f"{Fore.RED + 'The purchase was not made...Account balance is not enough for purchase' + Fore.RESET}")   
        
        
    def purchase_movie(self):
        """
        Get information about user purchase from the database
        and display it to the user
        """
        self.avilable_order = False
        
        titles_movie = ["Movie name", "Genre", "Date of relese", "Run time(minutes)", "Price", "Movie ID"]
        read_data = f"SELECT * FROM {self.new_email}_movie"
        purchase_information = self.database_info.execute(read_data).fetchall()
        
        self.movie_order = []
        for purchase in purchase_information:
            self.movie_order.append([info for info in purchase])
        
        if len(self.movie_order) == 0:
            return f"{Fore.RED + 'There are no purchases available' + Fore.RESET}"
        else:
            print(tabulate(purchase_information, headers=titles_movie, tablefmt="double_grid")) 
            self.avilable_order = True
            print("-" * 90)