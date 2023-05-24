# 5
from create_bank_account import BankAccount
from tabulate import tabulate
from colorama import Fore
from time import sleep
from pyfiglet import figlet_format
 
clothe_id = 10000

women_clothing_info_list = [
    {"Clothe": "Mini skirt", "Size": "S-M-L-XL", "Color": "Pink", "Price": 40, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 1)},
    {"Clothe": "Pants", "Size": "S-M-L-XL", "Color": "Black", "Price": 45, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 2)},
    {"Clothe": "Dress", "Size": "S-M-L-XL", "Color": "Grey", "Price": 43, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 3)},
    {"Clothe": "Bag", "Size": "Free size", "Color": "Grey", "Price": 25, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 4)},
    {"Clothe": "Coat", "Size": "S-M", "Color": "Cyan", "Price": 52, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 5)},
    {"Clothe": "Shirt", "Size": "S-M-L-XL", "Color": "White", "Price": 38.70, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 6)},
    {"Clothe": "T-shirt", "Size": "S-M-L-XL", "Color": "White", "Price": 28.50, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 7)},
    {"Clothe": "Hat", "Size": "Free size", "Color": "Red", "Price": 17.20, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 8)},
    {"Clothe": "Shoes", "Size": "34-45", "Color": "White", "Price": 54, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 9)},
    {"Clothe": "Shorts", "Size": "S-M-L-XL", "Color": "Brown", "Price": 43, "NumberOfClothes": 1, "Clothe ID": str(clothe_id + 10)}
]


class WomenClothe(BankAccount):
    """
    Showing women's clothes purchase of clothes by the user
    and adding purchase information to the database
    Args:
        BankAccount (class): Create User bank account
    """
        
    def women_clothe_table_info(self, women_clothe_info):
        """
        Table of women's clothes available in store
        The user can view the clothes and buy them 
        
        Args:
            women_clothe_info (list): clothing information list

        Returns:
            str: Full dispaly of clothing information
        """
        self.women_clothe_info = women_clothe_info
        
        title_women_info = [title for title in women_clothe_info[0]]
        new_women_info_clothe = []
        
        for clothe_info in women_clothe_info:
            new_women_info_clothe.append([info for info in clothe_info.values()])
        
        # Create men clothe table
        text = "Women's Clothe"
        print(f"{figlet_format(text)}\n{tabulate(new_women_info_clothe, headers=title_women_info, tablefmt='double_grid')}")
    
    
    def buy_women_clothe(self):
        """
        Choosing clothes and choosing the number of clothes and buying them
        And choosing the size of clothes
        """
        
        while True:
            self.women_clothe_table_info(self.women_clothe_info)
            
            shape = "►"
            print(f"{Fore.RED + shape + Fore.RESET} if you want to go back, enter the word --> {Fore.GREEN + 'back' + Fore.RESET}")
            print(f"{Fore.RED + shape + Fore.RESET} if you want to buy a dress enter the word from the table --> {Fore.GREEN + 'Clothe' + Fore.RESET} or {Fore.GREEN + 'Clothe ID' + Fore.RESET}\tSample: {Fore.GREEN + 'Coat' + Fore.RESET}")
            
            choose_clothe = input("Enter Clothe or Clothe ID: ").capitalize()
    
            self.user_order = list(filter(lambda data: data["Clothe"] == choose_clothe or data["Clothe ID"] == choose_clothe, self.women_clothe_info))
            if choose_clothe == "Back":
                break
            
            elif len(self.user_order) < 1:
                print(f"{Fore.RED + 'The clothe is not available...Enter the clothe info correctly.' + Fore.RESET}\n")
                sleep(1)
            
            elif len(self.user_order) > 0:
                self.count = int(input("How many clothes do you want? "))
                if self.count < 0:
                    self.count = 1
                
                self.finished_purchased = False
                self.clothe_size_women_clothe()
                
                # If the purchase is made, thei function will stop
                if self.finished_purchased:
                    break
                else:
                    pass
        
                
    def clothe_size_women_clothe(self):
        """
        Choosing the size of clothe And send the product to pay for it
        """
        
        if "-" in self.user_order[0]["Size"]:
            break_loop = False
            while True:
                clothe_size_list = self.user_order[0]["Size"].split("-")
                shape = "►"
                number_character = False
                
                print("#---------- Sizes list ----------#")
                for size in clothe_size_list:
                    
                    if size.isdigit():
                        print(f"There are sizes from {Fore.GREEN + str(clothe_size_list[0]) + Fore.RESET} to {Fore.GREEN + str(clothe_size_list[1]) + Fore.RESET}")
                        number_character = True
                        break
                        
                    else:
                        print(f"{Fore.RED + shape + Fore.RESET} {size}")
                
                if number_character == True:
                    choose_size = int(input("Sample: 40\nChoice shoes size: "))
                    
                    if choose_size in list(range(int(clothe_size_list[0]), int(clothe_size_list[1]) + 1)):
                        buy_info = [info for info in self.user_order[0].values()]
                        buy_info[1] = choose_size
                        buy_info[3] *= self.count
                        buy_info[4] *= self.count
                        
                        self.paying_for_women_clothes(buy_info)
                        break
                        
                    else:
                        print(f"{Fore.RED + 'Enter a valid size....' + Fore.RESET}")
                     
                else:
                    print(f"{Fore.RED + shape + Fore.RESET} Back")
          
                    while True:
                        # select clothe size:
                        choose_size = input(f"\n{Fore.BLUE + 'Sample' + Fore.RESET}: {Fore.BLUE + 'M' + Fore.RESET}\nEnter clothe size word: ").upper()
                        if choose_size in clothe_size_list:
                            buy_info = [info for info in self.user_order[0].values()]
                            buy_info[1] = choose_size
                            buy_info[3] *= self.count
                            buy_info[4] *= self.count
                            
                            self.paying_for_women_clothes(buy_info)
                            break_loop = True
                            break
                        
                        elif choose_size == "BACK":
                            break_loop = True
                            break
                        
                        else:
                            print(f"{Fore.RED + 'Enter size word !' + Fore.RESET}")
                
                if break_loop == True:
                    break
                
        else:
            # send data for payment
            new_user_order_info = [info for info in self.user_order[0].values()]
            new_user_order_info[3] *= self.count
            new_user_order_info[4] *= self.count
            
            self.paying_for_women_clothes(new_user_order_info)
              
    
    def paying_for_women_clothes(self, buy_info_list):
        """
        Paying for the purchase of clothes if a bank account is available
        And if the account balance is sufficient for the purchase
        Args:
            buy_info_list (list): Final information on buying clothes
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
            if buy_info_list[3] <= self.account_balance["Balance"]:
                print(f"{Fore.GREEN + 'The purchase was made successfully !' + Fore.RESET}")
                self.add_women_clothing_info(tuple(buy_info_list))
                
                # Decuting the purchase amount from ther user's bank account and database
                self.account_balance["Balance"] -= buy_info_list[3]
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
                self.connect.commit()
                
            else:
                print(f"{Fore.RED + 'The purchase was not made...Account balance is not enough for purchase' + Fore.RESET}")
        
        self.finished_purchased = True
     
    
    def purchased_women_clothing(self):
        """
        Get purchase information from the database
        and dispaly it to the user
        """
        self.avilable_order = False
        
        titles_clothe = ["Clothe(women)", "Shorts", "Color", "Price", "NumberOfClothes", "Clothe ID"]
        read_data = f"SELECT * FROM {self.new_email}_women_clothe"
        purchase_information = self.database_info.execute(read_data).fetchall()
        
        self.women_clothing_order = []
        for info in purchase_information:
            self.women_clothing_order.append([data for data in info])
        
        if len(self.women_clothing_order) == 0:
            return f"{Fore.RED + 'There are no purchases available' + Fore.RESET}"
        else:
            # purchase information table
            print(tabulate(self.women_clothing_order, titles_clothe, tablefmt="double_grid"))
            self.avilable_order = True
            print("-" * 90)