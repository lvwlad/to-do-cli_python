import json


class Task():
    '''Управление задачами пользователей'''
    def __init__(self):
         self.filename = 'files/tasks.json'

    
    def create_task(self, 
                    task_name: str,
                    user_id: str, 
                    description: str = '', 
                    category: str = 'no_category'
                    ):
        cp_task = {
           'task_name': task_name,
           'description': description
            }
        
        with open(self.filename, 'r+') as f:
            all_tasks = json.load(f)
            all_tasks[user_id][category].append(cp_task)
            f.seek(0)
            json.dump(all_tasks, f)
            f.truncate()

    def delete_task(self, task_name, category, user_id):
        '''Удаление задачи'''
        with open(self.filename, 'r+') as f:
            all_tasks = json.load(f)
            for task in all_tasks[user_id][category]:
                if task['task_name'] == task_name:
                    all_tasks[user_id][category].remove(task)
                    break
                else:
                    continue
            f.seek(0)
            json.dump(all_tasks,f)
            f.truncate()
    
    def moving_task(self,
                     user_id: str,
                     task_name: str,
                     category: str,
                     new_category:str = 'completed'
                    ):
        '''Пометка задания как выполненного по двефолут 
        или смена тэга для задачи
        '''
        with open(self.filename, 'r') as f:
            all_tasks = json.load(f)
        for task in all_tasks[user_id][category]:
            if task['task_name'] == task_name:
                all_tasks[user_id][new_category].append(task)
                all_tasks[user_id][category].remove(task)
                break
            else:
                continue
        with open(self.filename, 'w') as f:
            json.dump(all_tasks, f)

    def rename_task(self, 
                    user_id: str,
                    category: str,
                    old_task_name: str
                    ):
        '''rename the task'''
        with open(self.filename) as f:
            all_tasks = json.load(f)
        index = 0
        for task in all_tasks[user_id][category]:
            if task['task_name'] == old_task_name:
                old_desc = task['description']
                all_tasks[user_id][category].remove(task)
                new_task = {'task_name': input('Введите новое название для задачи: '),
                            'description': old_desc}
                all_tasks[user_id][category].insert(index, new_task)
                break
            else:
                index += 1
        with open(self.filename, 'w') as f:
            json.dump(all_tasks,f)

    def set_files(self, user_id: str,
                   category: str,
                   task_name: str
                   ):
        pass

    def set_new_description(self,
                            user_id: str,
                            category: str,
                            task_name: str
                            ):
        pass

    def get_all_tasks(self,
                      user_id: str,
                      category: str
                      ):
        '''Получить все задачи определенной категории'''
        with open(self.filename) as f:
            all_tasks = json.load(f)
        user_tasks = all_tasks[user_id][category]
        return user_tasks
        
