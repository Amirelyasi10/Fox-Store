# 12
from movie_section import (
    Movie, women_clothing_info_list, men_clothing_info_list, food_info_list, 
    iphone_mobile_info_list, samsung_mobile_info_list, books_info_list, movies_info_list
)
from colorama import Fore


class RemoveData(Movie):
    """
    Delete purchase order
    And the purchase Price will be returned to the user's account
    Args:
        Movie (class): _description_
    """
    
    def delete_women_clothing_order(self, order_id):
        self.delete_order = False
        
        finally_order = []
        for data in self.women_clothing_order:
            if order_id in data:
                finally_order = data

        if len(finally_order) == 0:
            pass
        else:
            delete_order = f"DELETE FROM {self.new_email}_women_clothe WHERE ClotheID = {order_id}"
            self.database_info.execute(delete_order)
            self.connect.commit()
            
            print(f"{Fore.GREEN + 'Your order has been successfully deleted...and the cost was returned to your bank account' + Fore.RESET}")
            self.account_balance["Balance"] += finally_order[3]
            self.delete_order = True
            
            #  Update account balance in database
            self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
            self.connect.commit()

    
    def delete_men_clothing_order(self, order_id):
        self.delete_order = False
        
        finally_order = []
        for data in self.men_clothing_order:
            if order_id in data:
                finally_order.append(data)

        if len(finally_order) == 0:
            pass
        else:
            delete_order = f"DELETE FROM {self.new_email}_men_clothe WHERE ClotheID = {order_id}"
            self.database_info.execute(delete_order)
            self.connect.commit()
            
            print(f"{Fore.GREEN + 'Your order has been successfully deleted...and the cost was returned to your bank account' + Fore.RESET}")
            self.account_balance["Balance"] += finally_order[3]
            self.delete_order = True
            
            #  Update account balance in database
            self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
            self.connect.commit()
            
    
    def delete_food_order(self, order_id):
        self.delete_order = False
        
        finally_order = []
        for data in self.food_order:
            if order_id in data:
                finally_order = data
        
        if len(finally_order) == 0:
            pass
        else:
            delete_order = f"DELETE FROM {self.new_email}_food WHERE FoodID = {order_id}" 
            self.database_info.execute(delete_order)
            self.connect.commit()
            
            print(f"{Fore.GREEN + 'Your order has been successfully deleted...and the cost was returned to your bank account' + Fore.RESET}")
            self.account_balance["Balance"] += finally_order[1]
            self.delete_order = True
            
            #  Update account balance in database
            self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
            self.connect.commit()
            
    
    def delete_iphone_mobile_order(self, order_id):
        self.delete_order = False
        
        finally_order = []
        for data in self.iphone_order:
            if order_id in data:
                finally_order = data
        
        if len(finally_order) == 0:
            pass
        else:
            delete_order = f"DELETE FROM {self.new_email}_iphone_mobile WHERE iPhoneID = {order_id}" 
            self.database_info.execute(delete_order)
            self.connect.commit()
            
            print(f"{Fore.GREEN + 'Your order has been successfully deleted...and the cost was returned to your bank account' + Fore.RESET}")
            self.account_balance["Balance"] += finally_order[6]
            self.delete_order = True
            
            #  Update account balance in database
            self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
            self.connect.commit()
            
    
    def delete_samsung_phone_order(self, order_id):
        self.delete_order = False
        
        finally_order = []
        for data in self.samsung_order:
            if order_id in data:
                finally_order = data
        
        if len(finally_order) == 0:
            pass
        else:
            delete_order = f"DELETE FROM {self.new_email}_samsung_mobile WHERE SamsungID = {order_id}" 
            self.database_info.execute(delete_order)
            self.connect.commit()
            
            print(f"{Fore.GREEN + 'Your order has been successfully deleted...and the cost was returned to your bank account' + Fore.RESET}")
            self.account_balance["Balance"] += finally_order[6]
            self.delete_order = True
            
            #  Update account balance in database
            self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
            self.connect.commit()
    
    
    def delete_book_order(self, order_id):
        self.delete_order = False
        
        finally_order = []
        for data in self.books_order:
            if order_id in data:
                finally_order = data
        
        if len(finally_order) == 0:
            pass
        else:
            delete_order = f"DELETE FROM {self.new_email}_book WHERE BookID = {order_id}" 
            self.database_info.execute(delete_order)
            self.connect.commit()
            
            print(f"{Fore.GREEN + 'Your order has been successfully deleted...and the cost was returned to your bank account' + Fore.RESET}")          
            self.account_balance["Balance"] += finally_order[2]
            self.delete_order = True
            
            #  Update account balance in database
            self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
            self.connect.commit()
    
    
    def delete_movie_order(self, order_id):
        self.delete_order = False
        
        finally_order = []
        for data in self.movie_order:
            if order_id in data:
                finally_order = data
        
        if len(finally_order) == 0:
            pass
        else:
            delete_order = f"DELETE FROM {self.new_email}_movie WHERE MovieID = {order_id}" 
            self.database_info.execute(delete_order)
            self.connect.commit()
            
            print(f"{Fore.GREEN + 'Your order has been successfully deleted...and the cost was returned to your bank account' + Fore.RESET}")
            self.account_balance["Balance"] += finally_order[4]
            self.delete_order = True
            
            #  Update account balance in database
            self.database_info.execute(f"UPDATE {self.new_email}_bank_account SET Balance = {self.account_balance['Balance']}")
            self.connect.commit()
    