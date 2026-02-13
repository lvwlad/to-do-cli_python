import json

class Category():
    '''Создание и управление категориями'''
    def __init__(self):
        self.filename = 'files/tasks.json'

    # def open_file(self):
    #     try:
    #         with open('files/tasks.json')
    #             data = json.load(f)

    def set_default_category(self, user_id):
        '''Установка стандартных категорий'''
        categories = ['work', 'study', 'completed', 'no_category']
        # filename = 'files/tasks.json'
        try:
            with open(self.filename) as f:
                users_task = json.load(f)
        except json.decoder.JSONDecodeError:
            users_task = {}
            users_task[user_id] = {}
            for category in categories:
                users_task[user_id][category] = [] 

            with open(self.filename, 'w') as f:
                json.dump(users_task, f)
        else:
            users_task[user_id] = {}
            for category in categories:
                users_task[user_id][category] = [] 
            with open(self.filename, 'w') as f:
                json.dump(users_task, f)
            
        
    def set_new_category(self, categoty_name: str, user_id: str):
        '''Добавление новой категории для задач'''
        # filename = 'files/tasks.json'
        with open(self.filename,'r+') as f:
            users_task = json.load(f)
            categories = users_task.get(user_id, 'No user')
            categories[categoty_name.lower()] = []
            users_task[user_id] = categories
            f.seek(0)                 # Прыгаем в начало для перезаписи
            json.dump(users_task, f) # Пишем поверх
            f.truncate()

    def delete_category(self, categoty_name: str, user_id: str):
        '''Удаление категории для задач'''
        # filename = 'files/tasks.json'
        with open(self.filename,'r+') as f:
            users_task = json.load(f)
            categories = users_task.get(user_id, 'No user')
            # categories[categoty_name] = []
            for task in categories[categoty_name]:
                categories['no_category'].append(task)
            del categories[categoty_name]
            users_task[user_id] = categories
            f.seek(0)                 # Прыгаем в начало для перезаписи
            json.dump(users_task, f) # Пишем поверх
            f.truncate()
    
    def rename_category(self, old_categoty: str, user_id: str):
        '''Переименование существующей категории'''
        with open(self.filename, 'r+') as f:
            all_tasks = json.load(f)
            new_category_name = input('Введите новое название категории (тэга): ')
            all_tasks[user_id][new_category_name] = all_tasks[user_id].pop(old_categoty)
            f.seek(0)
            json.dump(all_tasks,f)
            f.truncate()

    def get_all_user_categories(self,
                                user_id: str
                                ):
        '''
        Получить списко всех категорий пользователя\n
        Возвращает список категорйи пользователя
        '''
        user_categories = []
        with open(self.filename) as f:
            all_categories = json.load(f)
        for category in all_categories[user_id].keys():
            if category not in ['completed', 'no_category']:
                user_categories.append(category)
        return user_categories




