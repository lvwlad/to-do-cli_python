import user

class App():
    '''To-Do CLI'''
    def __init__(self):
        self.manage = user.User()

    def action_tasks(self, user_id, category):
        print('<-------------------------------------------------->')
        print('Выберите действие:')
        print('1. Добавить задачу\n' \
                    '2. Выполнить задачу\n' \
                    '3. Переместить в другую категорию\n' \
                    '4. Переименовать задачу\n' \
                    '5. Удалить задачу\n' \
                    '6. Посмотреть список всех задач в данной категории'
                    )
        print('<-------------------------------------------------->')
        user_answer = input('Ваш ответ: ')
        match user_answer:
            case "1":
                self.manage.tasks.create_task(input('Введите название задачи: '),
                                              user_id,
                                              input('Введите описание для задачи: '),
                                              category)
                self.action_tasks(user_id, category)
            case "2":
                self.manage.tasks.moving_task(user_id, 
                                              input('Введите название задачи, которое вы хотите выполнить: '),
                                              category)
                self.action_tasks(user_id, category)
            case "3":
                 self.manage.tasks.moving_task(user_id, 
                                              input('Введите название задачи, которое вы хотите выполнить: '),
                                              category,
                                              input('Введите новую категорию для задачи: '))
                 self.action_tasks(user_id, category)
            case "4":
                self.manage.tasks.rename_task(user_id, category,
                                              input('Введите название задачи, название которой вы хотите поменять: '))
                self.action_tasks(user_id, category)
            case "5":
                self.manage.tasks.delete_task(input('Введите название задачи, которую Вы хотите удалить: '),
                                              category,
                                              user_id)
                self.action_tasks(user_id, category)
            case "6":
                user_tasks = self.manage.tasks.get_all_tasks(user_id, category) 
                for task in user_tasks:
                    print(f'Название задачи: {task['task_name']}')
                    print(f'Описание задачи: {task['description']}')
                    print("----")
                self.action_tasks(user_id, category)
            case "q":
                return 
            case _:
                print('Введите корреткное действие (1-6)')
                self.action_tasks(user_id, category)
                

    
    def manage_tasks(self, user_id):
        print('Выберите категорию: ')
        user_ctgr = self.manage.categories.get_all_user_categories(user_id)
        for ctgr in user_ctgr:
            print(f'\t--> {ctgr}')
        user_answer = input('Введите категорию: ')
        if user_answer.lower() not in self.manage.categories.get_all_user_categories(user_id):
            print('Введите существующую категорию')
            self.manage_tasks(user_id)
        else:
            self.action_tasks(user_id, user_answer)

    def manage_ctgr(self, user_id):
        print('<-------------------------------------------------->')
        print('Выберите действие:')
        print('1. Добавить категорию (тэг)\n' \
                    '2. Переименовать категорию\n' \
                    '3. Удалить категорию'
                    )
        print('<-------------------------------------------------->')
        user_answer = input('Ваш ответ: ')
        match user_answer:
            case '1':
                self.manage.categories.set_new_category(input('Введите новый тэг: '),
                                                        user_id)
                self.manage_ctgr(user_id)
            case '2':
                self.manage.categories.rename_category(input('Введите какой тэг хотите переименовать: '),
                                                       user_id)
                self.manage_ctgr(user_id)
            case '3':
                self.manage.categories.delete_category(input('Введите какой тэг хотите удалить: '),
                                                       user_id)
                self.manage_ctgr(user_id)
            case 'q':
                return 
            case _:
                self.manage_ctgr(user_id)
      

    def choice_action(self, user_id):
        print('<-------------------------------------------------->')
        print('Выберите действие:')
        print('1. Посмоотреть список тэгов (категорий)\n' \
                    '2. Посмотреть задачи'
                    )
        print('<-------------------------------------------------->')
        user_action = input('Ваш ответ: ')
        match user_action:
            case "1":
                user_ctgr = self.manage.categories.get_all_user_categories(user_id)
                print('Ваши категории:')
                for ctgr in user_ctgr:
                    print(f'\t--> {ctgr}')
                self.manage_ctgr(user_id)
                self.choice_action(user_id)
            case "2":
                self.manage_tasks(user_id)
                self.choice_action(user_id)
            case 'q':
                return False
            case _:
                print('Некорректный ввод')
                self.choice_action(user_id)        

    def main(self):
        print('<-------------------------------------------------->')
        print('Здраствуйте! Выбирите действие\n\t', end = '')
        print('Нажмите "1" для регистрации')
        print('\tНажмите "2" для вход с существующий аккаунт')
        print('<-------------------------------------------------->')
        user_answer = input('Ваш ответ: ')
        match user_answer:
            case "1":
                user_id = input('Введите Ваш логин: ')
                self.manage.register(user_id,
                                     input('Введите Ваше имя: '),
                                     input('Введите Ваш пароль: '))
                self.main()
            case "2":
                user_id = input('Введите Ваш логин: ')
                if self.manage.login(user_id,
                                  input('Введите Ваш пароль: ')
                                  ):
                
                    self.choice_action(user_id)  

                    
            case "q":
                return         
            case _:
                print('Укажите 1 или 2\n')
                self.main()
        


if __name__ == "__main__":
    my_app = App()
    my_app.main()