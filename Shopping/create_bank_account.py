# 4
from login_or_signup import Login
from colorama import Fore
from tabulate import tabulate

class BankAccount(Login):
    """
    A bank account is created
    And there is the ability to deposit moneyhas been created
    and withdraw money and see the balance.
    Args:
        Login (class): Checking Login or sign up user
    """
    
    def user_private_account(self, name, last_name, balance = 0):
        """
        Save the user's banking information
        and applying new information
        """
        self.name = name
        self.last_name = last_name
        self.balance = balance
        
        self.account_balance = {"First name":"", "Last name":"", "Balance":0}
        self.account_balance["First name"] = self.name
        self.account_balance["Last name"] = self.last_name
        self.account_balance["Balance"] = self.balance
        self.create_bank_account = True
        
        self.create_user_bank_account()
        self.add_user_bank_account_info(tuple(info for info in self.account_balance.values()))
        return f"{Fore.GREEN + 'Your bank account has been successfully created' + Fore.RESET}"
    
    # Use of account services
    def account_services(self):
        """
        Services provided to the user
        1: Deposit money
        2: withdraw money
        3: Account balance
        """
    
        def deposit_money():
            """
            Deposit money to account
            user cannot deposit money to account more than 3000$ money
            """
            deposit = float(input("how much do you want to deposit: "))
            
            if deposit < 0:
                print(f"{Fore.RED + 'The amount of money should not be negative.' + Fore.RESET}")
            elif deposit > 3000:
                print(f"{Fore.RED + 'more than 3000 cannot be deposit.' + Fore.RESET}")
            else:
                print(f"{Fore.GREEN + 'done successfully...' + Fore.RESET}")
                self.account_balance["Balance"] += deposit
                
                #  Update account balance in database
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
                self.connect.commit()
        
        
        def withdraw_money():
            """              
            Receive money from the account
            cannot withdraw more than balance 
            and it is not possible to withdraw all the inventory
            """
            withdraw = float(input("how much money do you want to withdraw: "))
            
            if withdraw < 0:
                print(f"{Fore.RED + 'The amount of money should not be negative.' + Fore.RESET}")
            elif withdraw > self.account_balance["Balance"]:
                print(f"{Fore.RED + 'insufficient inventory.' + Fore.RESET}")
            elif withdraw == self.account_balance["Balance"]:
                print(f"{Fore.RED + 'it is not possible to withdraw the enter account Balance.' + Fore.RESET}")    
            elif withdraw > 3000:
                print(f"{Fore.RED + 'more than 3000 cannot be withdraw.' + Fore.RESET}")      
            else:
                print(f"{Fore.GREEN + 'done successfully...' + Fore.RESET}")    
                self.account_balance["Balance"] -= withdraw
                
                #  Update account balance in database
                self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balanace = {self.account_balance['Balance']}")
                self.connect.commit()
        
        
        def account_balance():
            """
            Show account balance 
            and display account information
            """
            account_title = [title for title in self.account_balance]
            account_info = [[info for info in self.account_balance.values()]]
            
            account_table = tabulate(account_info, headers = account_title, tablefmt = "double_grid")
            print(f"\n{Fore.RED + 'Note' + Fore.RESET}: Your account information\n{account_table}")
        
        
        while True:
            options = ["deposit money", "withdraw money", "account Balance", "Back"]
            
            number = 1
            for service in options:
                print(f"[{Fore.RED + str(number) + Fore.RESET}] {service}")
                number += 1
                
            choose_option = input("Enter an option: ").lower()
            
            if choose_option in ["1", "deposit money"]:
                deposit_money()
            elif choose_option in ["2", "withdraw money"]:
                withdraw_money()
            elif choose_option in ["3", "account Balance"]:
                account_balance()
            elif choose_option in["4", "back"]:
                break
            else:
                print(f"{Fore.RED + 'Enter a valid option !' + Fore.RESET}")
            print()