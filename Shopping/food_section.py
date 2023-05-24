# 7
from men_clothing_section import (
    MenClothe, women_clothing_info_list , men_clothing_info_list
)
from tabulate import tabulate
from colorama import Fore
from pyfiglet import figlet_format
from time import sleep
 
food_id = 30000

food_info_list = [
    {"Food": "Masala Grill", "Price": 51, "NumberOfFood" : 1, "Food ID": str(food_id + 1)},
    {"Food": "Chicken Grill", "Price": 44, "NumberOfFood" : 1, "Food ID": str(food_id + 2)},
    {"Food": "Chunky Paneer", "Price": 179, "NumberOfFood" : 1, "Food ID": str(food_id + 3)},
    {"Food": "Potato Crunch", "Price": 149, "NumberOfFood" : 1, "Food ID": str(food_id + 4)},
    {"Food": "Cheeseburger", "Price": 80, "NumberOfFood" : 1, "Food ID": str(food_id + 5)},
    {"Food": "Kids burger", "Price": 30, "NumberOfFood" : 1, "Food ID": str(food_id + 6)},
    {"Food": "Fries", "Price": 45, "NumberOfFood" : 1, "Food ID": str(food_id + 7)},
    {"Food": "Bacon cheese", "Price": 50, "NumberOfFood" : 1, "Food ID": str(food_id + 8)},
    {"Food": "Classic Cheese", "Price": 55, "NumberOfFood" : 1, "Food ID": str(food_id + 9)},
    {"Food": "Beer", "Price": 20, "NumberOfFood" : 1, "Food ID": str(food_id + 10)},
    {"Food": "Soft Drink", "Price": 18, "NumberOfFood" : 1, "Food ID": str(food_id + 11)},
    {"Food": "Lemonade", "Price": 18, "NumberOfFood" : 1, "Food ID": str(food_id + 12)},
    {"Food": "Water", "Price": 15, "NumberOfFood" : 1, "Food ID": str(food_id + 13)}
]


class Food(MenClothe):
    """
    Showing The food information table to the user
    And user can buy the food it needs
    
    Args:
        MenClothe (class): Men's clothing information is in this class
    """
    
    
    def food_table_info(self, food_info):
        """
        Food information is received
        And a table of food information is made to be displayed to the user
        
        Args:
            food_info (list): A list of  containing food information
        """
        
        self.food_info = food_info
        title_food = [info for info in self.food_info[0]]
        new_food_info = []
        for info in self.food_info:
            new_food_info.append([food for food in info.values()])
            
        # Create food table
        print(figlet_format("Food Table"))
        print(tabulate(new_food_info, headers=title_food, tablefmt="double_grid"))
    
    
    def buy_food(self):
        """
        Show food list and buying food by the user
        """
        while True:
            self.food_table_info(self.food_info)
            
            shape = "►"
            print(f"{Fore.RED + shape + Fore.RESET} if you want to go back, enter the word --> {Fore.GREEN + 'back' + Fore.RESET}")
            
            choose_food = " ".join([item.capitalize() for item in input("Enter Food name or Food ID: ").split()])
            user_order = list(filter(lambda data: data["Food"] == choose_food or data["Food ID"] == choose_food, self.food_info))
            
            if choose_food == "Back":
                break
            elif len(user_order) == 0:
                print(f"{Fore.RED + 'The food is not available...Enter a valid food' + Fore.RESET}\n")
                sleep(1)
            elif len(user_order)  > 0:
                self.food_count = int(input("How many foods do you want? ")) 
                if self.food_count < 1:
                    self.food_count = 1
                
                # change info in food
                new_user_order = [info for info in user_order[0].values()]
                new_user_order[1] *= self.food_count
                new_user_order[2] *= self.food_count
                
                self.paying_for_food(new_user_order)
                break
            
    
    def paying_for_food(self, final_food_info):
        """
        Paying for the purchase of food if a bank account is available
        And if the account balance is sufficient for the purchase.
        adding purchase information to the database.
        
        Args:
            final_food_info (list): User purchase information
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
            if final_food_info[1] <= self.account_balance["Balance"]:
                print(f"{Fore.GREEN + 'The purchase was made successfully !' + Fore.RESET}")
                self.add_food_info(tuple(final_food_info))
                
                # Decuting the purchase amount from ther user's bank account and database
                self.account_balance["Balance"] -= final_food_info[1]
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
                self.connect.commit()
                
            else:
                print(f"{Fore.RED + 'The purchase was not made...Account balance is not enough for purchase' + Fore.RESET}")
    
    
    def purchased_food(self):
        """
        Get information about user purchase from the database
        and display it to the user
        """
        self.avilable_order = False
        
        titles_food = ["Food", "Price", "NumberOfFood", "Food ID"]
        read_data = f"SELECT * FROM {self.new_email}_food"
        purchase_information = self.database_info.execute(read_data).fetchall()
        
        self.food_order = []
        for purchase in purchase_information:
            self.food_order.append([info for info in purchase])
        
        if len(self.food_order) == 0:
            return f"{Fore.RED + 'There are no purchases available' + Fore.RESET}"
        else:
            print(tabulate(self.food_order, titles_food, tablefmt="double_grid"))
            self.avilable_order = True
            print("-" * 90)