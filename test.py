user_dict = {
    'tom': {'user_name': 'Tom', 'user_age': 18},
    'jerry': {'user_name': 'Jerry', 'user_age': 10},
    'gani': {'user_name': 'Gani', 'user_age': 25},  
}
   
user = user_dict.get('gani')
if user:
    print(user)