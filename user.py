import json, hashlib



import category, task

userfile = 'files/users.json'


class User():
    '''Класс приложения'''
    def __init__(self):
         '''инициализация экземпляра'''
         self.categories = category.Category()
         self.tasks = task.Task()
   

    def register(self, user_id: str, username: str, password: str):
        '''Регистрация пользователя в системе'''
        #pass
        try:
            with open(userfile) as f:
                users = json.load(f)
        except json.decoder.JSONDecodeError:
            hash_passsword = hashlib.sha256()
            hash_passsword.update(password.encode('utf-8'))
            hash_passsword = hash_passsword.hexdigest()
            users = { 
                user_id: {'name': username, 'password': hash_passsword}
            }
            with open(userfile, 'w') as f:
                json.dump(users,f)
            self.categories.set_default_category(user_id)
            print('You have been registred')
        else:
            hash_passsword = hashlib.sha256()
            hash_passsword.update(password.encode('utf-8'))
            hash_passsword = hash_passsword.hexdigest()
            users[user_id] = {'name': username, 'password': hash_passsword}
            with open(userfile, 'w') as f:
                json.dump(users,f)
            self.categories.set_default_category(user_id)
            print('You have been registred')

    def login(self, user_id: str, password: str):
        '''Login user in system'''
        try:
            with open(userfile) as f:
                users = json.load(f)
        except FileNotFoundError:
            print('Error: NoDataFound')
        else:
           if user_id in users:
               hash_passsword = hashlib.sha256()
               hash_passsword.update(password.encode('utf-8'))
               hash_passsword = hash_passsword.hexdigest()
               if users[user_id]['password'] == hash_passsword:
                   return True
               else:
                   print('Пароль неверный') 
                   return False
           else:
               print('Такого пользователя не существует')
               return False


                   
            
               
                

# my_do = User()
# my_do.register('vldslv','vlad', 'qwerty')
# my_do.register('baldi_1920','aldi', 'qwerty')
# #my_do.login('vldslv', 'qwerty')
# my_do.categories.set_new_category('apple', 'baldi_1920')
# my_do.categories.delete_category('apple', 'baldi_1920')
#my_do.categories.rename_category('study', 'baldi_1920')
#my_do.categories.delete_category('work', 'baldi_1920')
# print(my_do.categories.get_all_user_categories('baldi_1920'))




