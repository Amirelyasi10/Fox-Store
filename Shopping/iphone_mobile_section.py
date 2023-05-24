# 8
from food_section import (
    Food, women_clothing_info_list, men_clothing_info_list, food_info_list
)
from pyfiglet import figlet_format
from tabulate import tabulate
from colorama import Fore
from time import sleep

phone_id = 40000
        
iphone_mobile_info_list = [
    {"Brand": "Apple", "Model": "iPhone 14 Pro", "Size(inches)": 6.1, "Color": "Black-Silver-Gold-Purple-Red", "Memory Storage": "1TB", "Price": 2502.15, "iPhone ID": str(phone_id + 1)},
    {"Brand": "Apple", "Model": "iPhone 14 Pro", "Size(inches)": 6.1, "Color": "Black-Silver-Gold-Purple-Red", "Memory Storage": "512GB", "Price": 2169.05, "iPhone ID": str(phone_id + 2)},
    {"Brand": "Apple", "Model": "iPhone 14 Pro", "Size(inches)": 6.1, "Color": "Black-Silver-Gold-Purple-Red", "Memory Storage": "256GB", "Price": 1836, "iPhone ID": str(phone_id + 3)},
    {"Brand": "Apple", "Model": "iPhone 14 Pro", "Size(inches)": 6.1, "Color": "Black-Silver-Gold-Purple-Red", "Memory Storage": "128GB", "Price": 1664.40, "iPhone ID": str(phone_id + 4)},
    {"Brand": "Apple", "Model": "iPhone 14", "Size(inches)": 6.1, "Color": "Blue-Purple-Yellow-Midnight-Starlight-Red", "Memory Storage": "512GB", "Price": 1815.80, "iPhone ID": str(phone_id + 5)},
    {"Brand": "Apple", "Model": "iPhone 14", "Size(inches)": 6.1, "Color": "Blue-Purple-Yellow-Midnight-Starlight-Red", "Memory Storage": "256GB", "Price": 1482.70, "iPhone ID": str(phone_id + 6)},
    {"Brand": "Apple", "Model": "iPhone 14", "Size(inches)": 6.1, "Color": "Blue-Purple-Yellow-Midnight-Starlight-Red", "Memory Storage": "128GB", "Price": 1311.10, "iPhone ID": str(phone_id + 7)},
    {"Brand": "Apple", "Model": "iPhone 13", "Size(inches)": 6.1, "Color": "Blue-Pink-Midnight-Starlight-Green-Red", "Memory Storage": "512GB", "Price": 1513.00, "iPhone ID": str(phone_id + 8)},
    {"Brand": "Apple", "Model": "iPhone 13", "Size(inches)": 6.1, "Color": "Blue-Pink-Midnight-Starlight-Green-Red", "Memory Storage": "256GB", "Price": 1179.90, "iPhone ID": str(phone_id + 9)},
    {"Brand": "Apple", "Model": "iPhone 13", "Size(inches)": 6.1, "Color": "Blue-Pink-Midnight-Starlight-Green-Red", "Memory Storage": "128GB", "Price": 1008.30, "iPhone ID": str(phone_id + 10)},
    {"Brand": "Apple", "Model": "iPhone SE", "Size(inches)": 4.71, "Color": "Midnight-Starlight-Red", "Memory Storage": "256GB", "Price": 947.75, "iPhone ID": str(phone_id + 11)},
    {"Brand": "Apple", "Model": "iPhone SE", "Size(inches)": 4.71, "Color": "Midnight-Starlight-Red", "Memory Storage": "128GB", "Price": 776.15, "iPhone ID": str(phone_id + 12)},
    {"Brand": "Apple", "Model": "iPhone SE", "Size(inches)": 4.71, "Color": "Midnight-Starlight-Red", "Memory Storage": "64GB", "Price": 705.50, "iPhone ID": str(phone_id + 13)},
    {"Brand": "Apple", "Model": "iPhone 12", "Size(inches)": 6.1, "Color": "Blue-Purple-Green-White-Black-Red", "Memory Storage": "256GB", "Price": 1250.55, "iPhone ID": str(phone_id + 14)},
    {"Brand": "Apple", "Model": "iPhone 12", "Size(inches)": 6.1, "Color": "Blue-Purple-Green-White-Black-Red", "Memory Storage": "128GB", "Price": 1070.05, "iPhone ID": str(phone_id + 15)},
    {"Brand": "Apple", "Model": "iPhone 12", "Size(inches)": 6.1, "Color": "Blue-Purple-Green-White-Black-Red", "Memory Storage": "64GB", "Price": 1008.30, "iPhone ID": str(phone_id + 16)}
]

class IphoneMobile(Food):
    """
    Display information of iPhone brand phones 
    And it is also possible for the user to buy a phone
    
    Args:
        Food (class): There is information about buiyng food in this class
    """
 

    def iphone_table_info(self, iphone_info):
        """
        Phone information is received 
        it is displayed ti the user as a table
        Args:
            iphone_info (list): A list of information about iPhone phones
        """
        
        self.iphone_info = iphone_info
        
        iphone_title = [title for title in self.iphone_info[0]]
        new_iphone_info = []
        
        for phone in self.iphone_info:
            new_iphone_info.append([info for info in phone.values()])
        
        # Create iphone gable info
        print(figlet_format("iPhone  Mobile"))
        print(tabulate(new_iphone_info, headers=iphone_title, tablefmt="double_grid"))
    
    
    def buy_iphone_mobile(self):
        """
        Display the phone information table
        and choosing a phone and buying it buy the user
        """
        
        while True:
            self.iphone_table_info(self.iphone_info)
            
            shape = "►"
            print(f"{Fore.RED + shape + Fore.RESET} if you want to go back, enter the word --> {Fore.GREEN + 'back' + Fore.RESET}")
            
            choose_phone = input("Enter iPhone model or iPhone ID of the phone from the table: ").replace("p", "P")
              
            if choose_phone in ["back", "Back", "BACK"]:
                break
            
            elif choose_phone.isdigit():
                check_avilability_iphone_id = list(filter(lambda info: info["iPhone ID"] == choose_phone, self.iphone_info))
                
                if len(check_avilability_iphone_id) == 0:
                    print(f"{Fore.RED + 'The entered iPhone ID is no available.' + Fore.RESET}")
                    sleep(1)
                    continue
                
            else:
                check_avilability_iphone_model = list(filter(lambda info: info["Model"] == choose_phone, self.iphone_info))
                
                if len(check_avilability_iphone_model) == 0:
                    print(f"{Fore.RED + 'The entered iPhone model is not available.' + Fore.RESET}")
                    sleep(1)
                    continue
                
                else:    
                    choose_storage = input(f"Sample: {Fore.RED + '256' + Fore.RESET}\nEnter your desired phone Memory Storage: ").upper()
                
                    if choose_storage.isdigit():     
                        if int(choose_storage) == 1:
                            choose_storage += "TB"
                        else:
                            choose_storage += "GB"
                        
                        check_avilability_memory_storage = list(filter(lambda info:info["Model"] == choose_phone and info["Memory Storage"] == choose_storage, self.iphone_info))
                        
                        if len(check_avilability_memory_storage) == 0:
                            print(f"{Fore.RED + 'The entered memory storage is not available.' + Fore.RESET}")  
                            continue
                    
                    else:
                        choose_storage = choose_storage.replace(" ", "")
                    
            self.user_iphone_order = list(filter(lambda data: (data["Model"] == choose_phone and choose_storage == data["Memory Storage"]) or (data["iPhone ID"] == choose_phone), self.iphone_info))    
            self.finished_purchased = False
            self.choose_iPhone_phone_color()
                
            # If the purchase is made, thei function will stop
            if self.finished_purchased:
                break
            else:
                pass
        
    
    def choose_iPhone_phone_color(self):
        """
        The user specifies the color of the phone he has chosen
        """
        
        while True:
            colors_list = self.user_iphone_order[0]["Color"].split("-")
            print()
            
            shape = "►"
            for color in colors_list:
                print(f"{Fore.RED + str(shape) + Fore.RESET} {color}")
            print(f"{Fore.RED + str(shape) + Fore.RESET} Back")
            
            choose_color = input(f"\nSample: {Fore.RED + 'Red' + Fore.RESET}\nChoose the color of the phone: ").capitalize()
            if choose_color in ["Back", "back", "BACK"]:
                break
            
            elif choose_color in colors_list:
                new_user_order = [info for info in self.user_iphone_order[0].values()]
                new_user_order[3] = choose_color
                self.paying_for_iphone_phone(new_user_order)
                break
            
            else:
                print(f"{Fore.RED + 'The color is not available --> ' + Fore.RESET}Please choose the available colors carefully.")
                sleep(1)
            
    
    def paying_for_iphone_phone(self, phone_info_list):
        """
        Paying for the purchase of phone if a bank account is available
        And if the account balance is sufficient for the purchase.
        adding purchase information to the database.
        
        Args:
            phone_info_list (list): User purchase information
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
            if phone_info_list[5] <= self.account_balance["Balance"]:
                print(f"{Fore.GREEN + 'The purchase was made successfully !' + Fore.RESET}")
                self.add_iphone_mobile_info(tuple(phone_info_list))
                
                # Decuting the purchase amount from ther user's bank account and database
                self.account_balance["Balance"] -= phone_info_list[5]
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
                self.connect.commit()
                
            else:
                print(f"{Fore.RED + 'The purchase was not made...Account balance is not enough for purchase' + Fore.RESET}")
        self.finished_purchased = True
    
    
    def purchased_iphone_mobile(self):
        """
        Get information about user purchase from the database
        and display it to the user
        """
        self.avilable_order = False
        
        titles_phone = ["Brand", "Model", "Size(inches)", "Color", "Memory Storage", "Price", "iPhone ID"]
        read_data = f"SELECT * FROM {self.new_email}_iphone_mobile"
        purchase_information = self.database_info.execute(read_data).fetchall()
        
        self.iphone_order = []
        for purchase in purchase_information:
            self.iphone_order.append([info for info in purchase])
        
        if len(self.iphone_order) == 0:
            return f"{Fore.RED + 'There are no purchases available' + Fore.RESET}"
        else:
            print(tabulate(self.iphone_order, titles_phone, tablefmt="double_grid")) 
            self.avilable_order = True
            print("-" * 10)