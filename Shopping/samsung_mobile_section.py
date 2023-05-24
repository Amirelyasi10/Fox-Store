# 9
from iphone_mobile_section import (
    IphoneMobile, women_clothing_info_list, men_clothing_info_list, food_info_list, iphone_mobile_info_list
)
from pyfiglet import figlet_format
from tabulate import tabulate
from colorama import Fore
from time import sleep

phone_id = 50000

samsung_mobile_info_list = [
    {"Brand": "Samusng", "Model": "Galaxy S23 Ultra", "Size(inches)": 6.8, "Color": "Black-Green-Pink-White", "Memory Storage": "1TB", "Price": 1439.99, "Samsung ID": str(phone_id + 1)},
    {"Brand": "Samusng", "Model": "Galaxy S23 Ultra", "Size(inches)": 6.8, "Color": "Black-Green-Pink-White", "Memory Storage": "512GB", "Price": 1379.99, "Samsung ID": str(phone_id + 2)},
    {"Brand": "Samusng", "Model": "Galaxy S23 Ultra", "Size(inches)": 6.8, "Color": "Black-Green-Pink-White", "Memory Storage": "256GB", "Price": 1199.99, "Samsung ID": str(phone_id + 3)},
    {"Brand": "Samusng", "Model": "Galaxy S22", "Size(inches)": 6.6, "Color": "Black-Green-Pink-White", "Memory Storage": "128GB", "Price": 870.00, "Samsung ID": str(phone_id + 4)},
    {"Brand": "Samusng", "Model": "Galaxy M54", "Size(inches)": 6.7, "Color": "Black-Green-Pink-White", "Memory Storage": "128GB", "Price": 210.00, "Samsung ID": str(phone_id + 5)},
    {"Brand": "Samusng", "Model": "Galaxy A73", "Size(inches)": 6.7, "Color": "White-Grey-green-Black", "Memory Storage": "128GB", "Price": 394.90, "Samsung ID": str(phone_id + 6)},
    {"Brand": "Samusng", "Model": "Galaxy A73", "Size(inches)": 6.7, "Color": "White-Grey-green-Black", "Memory Storage": "256GB", "Price": 466.99, "Samsung ID": str(phone_id + 7)},
    {"Brand": "Samusng", "Model": "Galaxy A54", "Size(inches)": 6.4, "Color": "Black-purple-White", "Memory Storage": "128GB", "Price": 449.99, "Samsung ID": str(phone_id + 8)}, 
    {"Brand": "Samusng", "Model": "Galaxy A53", "Size(inches)": 6.5, "Color": "Blue-Black-Peach-white", "Memory Storage": "128GB", "Price": 329.40, "Samsung ID": str(phone_id + 9)},
    {"Brand": "Samusng", "Model": "Galaxy A53", "Size(inches)": 6.5, "Color": "Blue-Black-Peach-white", "Memory Storage": "256GB", "Price": 419, "Samsung ID": str(phone_id + 10)},    
    {"Brand": "Samusng", "Model": "Galaxy A33", "Size(inches)": 6.4, "Color": "Black-Green-Pink-White", "Memory Storage": "128GB", "Price": 276.00, "Samsung ID": str(phone_id + 11)},
    {"Brand": "Samusng", "Model": "Galaxy A23", "Size(inches)": 6.6, "Color": "Black-Green-Pink-White", "Memory Storage": "64GB", "Price": 149.99, "Samsung ID": str(phone_id + 12)},
    {"Brand": "Samusng", "Model": "Galaxy A23", "Size(inches)": 6.6, "Color": "Black-Green-Pink-White", "Memory Storage": "128GB", "Price": 195.00, "Samsung ID": str(phone_id + 13)},
    
]

 
class SamsungMobile(IphoneMobile):
    """
    Display information of samsung brand phones 
    And it is also possible for the user to buy a phone

    Args:
        IphoneMobile (class): There is information about buiyng iphone phone in this class
    """
    
    def samsung_table_info(self, samsung_info):
        self.samsung_info = samsung_info
        
        samsung_title = [title for title in self.samsung_info[0]]
        new_samsung_info = []
        
        for phone in self.samsung_info:
            new_samsung_info.append([info for info in phone.values()])
        
        # Create samsung gable info
        print(figlet_format("Samsung  Mobile"))
        print(tabulate(new_samsung_info, headers=samsung_title, tablefmt="double_grid"))
    
    
    def buy_samsung_mobile(self):
        """
        Display the phone information table
        and choosing a phone and buying it buy the user
        """
        
        while True:
            self.samsung_table_info(self.samsung_info)
            
            shape = "►"
            print(f"{Fore.RED + shape + Fore.RESET} if you want to go back, enter the word --> {Fore.GREEN + 'back' + Fore.RESET}")
            choose_phone = input("Enter samsung model or Samsung ID of the phone from the table: ").lower()
              
            if choose_phone == "back":
                break
            
            elif choose_phone.isdigit():
                check_avilability_samsung_id = list(filter(lambda info: info["Samsung ID"] == choose_phone, self.samsung_info))
                
                if len(check_avilability_samsung_id) == 0:
                    print(f"{Fore.RED + 'The entered Samsung ID is no available.' + Fore.RESET}")
                    sleep(1)
                    continue
                
            else:
                check_avilability_samsung_model = list(filter(lambda info: info["Model"].lower() == choose_phone, self.samsung_info))
                
                if len(check_avilability_samsung_model) == 0:
                    print(f"{Fore.RED + 'The entered Samsung model is not available.' + Fore.RESET}")
                    sleep(1)
                    continue
                
                else:    
                    choose_storage = input(f"Sample: {Fore.RED + '256' + Fore.RESET}\nEnter your desired phone Memory Storage: ").upper()
                
                    if choose_storage.isdigit():     
                        if int(choose_storage) == 1:
                            choose_storage += "TB"
                        else:
                            choose_storage += "GB"
                        
                        check_avilability_memory_storage = list(filter(lambda info:info["Model"].lower() == choose_phone and info["Memory Storage"] == choose_storage, self.samsung_info))
                        
                        if len(check_avilability_memory_storage) == 0:
                            print(f"{Fore.RED + 'The entered memory storage is not available.' + Fore.RESET}")  
                            continue
                    
                    else:
                        choose_storage = choose_storage.replace(" ", "")

                
            self.user_samsung_order = list(filter(lambda data: (data["Model"].lower() == choose_phone and choose_storage == data["Memory Storage"]) or (data["Samsung ID"] == choose_phone), self.samsung_info))   
            self.finished_purchased = False
            self.choose_samsung_phone_color()
      
            # If the purchase is made, thei function will stop
            if self.finished_purchased: # True
                break
            else: # False
                pass
                
     
    def choose_samsung_phone_color(self):
        """
        The user specifies the color of the phone he has chosen
        """
        
        while True:
            colors_list = self.user_samsung_order[0]["Color"].split("-")
            print()
            
            shape = "►"
            for color in colors_list:
                print(f"{Fore.RED + str(shape) + Fore.RESET} {color}")
            print(f"{Fore.RED + str(shape) + Fore.RESET} Back")
            
            choose_color = input(f"\nSample: {Fore.RED + 'Black' + Fore.RESET}\nChoose the color of the phone: ").capitalize()
            if choose_color in ["Back", "back", "BACK"]:
                break
            
            elif choose_color in colors_list:
                new_user_order = [info for info in self.user_samsung_order[0].values()]
                new_user_order[3] = choose_color
                self.paying_for_samsung_phone(new_user_order)
                break
            
            else:
                print(f"{Fore.RED + 'The color is not available --> ' + Fore.RESET}Please choose the available colors carefully.")
                sleep(1)
    
    
    def paying_for_samsung_phone(self, samsung_info_list):
        """
        Paying for the purchase of phone if a bank account is available
        And if the account balance is sufficient for the purchase.
        adding purchase information to the database.
        
        Args:
            samsung_info_list (list): User purchase information
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
            if samsung_info_list[5] <= self.account_balance["Balance"]:
                print(f"{Fore.GREEN + 'The purchase was made successfully !' + Fore.RESET}")
                self.add_samsung_mobile_info(tuple(samsung_info_list))
                
                # Decuting the purchase amount from ther user's bank account and database
                self.account_balance["Balance"] -= samsung_info_list[5]
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
                self.connect.commit()
                
            else:
                print(f"{Fore.RED + 'The purchase was not made...Account balance is not enough for purchase' + Fore.RESET}")
            
        self.finished_purchased = True
    
    
    def purchased_samsung_mobile(self):
        """
        Get information about user purchase from the database
        and display it to the user
        """ 
        self.avilable_order = False
        
        titles_phone = ["Brand", "Model", "Size(inches)", "Color", "Memory Storage", "Price", "Samsung ID"]
        read_data = f"SELECT * FROM {self.new_email}_samsung_mobile"
        purchase_information = self.database_info.execute(read_data).fetchall()
        
        self.samsung_order = []
        for purchase in purchase_information:
            self.samsung_order.append([info for info in purchase])
        
        if len(self.samsung_order) == 0:
            return f"{Fore.RED + 'There are no purchases available' + Fore.RESET}"
        else:
            print(tabulate(self.samsung_order, headers=titles_phone, tablefmt="double_grid")) 
            self.avilable_order = True
            print("-" * 90)