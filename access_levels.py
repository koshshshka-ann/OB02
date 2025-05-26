# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

# Требования:

# 1. Класс User: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).

# 2. Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

# 3. Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access = 'user'

    def get_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access(self):
        return self._access

    def set_name(self, new_name):
        old_name = self._name
        self._name = new_name
        print(f"\nИмя сотрудника '{old_name}' успешно заменено на '{new_name}'")

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Пользователь '{user.get_name()}' добавлен в список сотрудников!")

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"Пользователь '{user.get_name()}' удален из списка сотрудников!")

    def info(self, user_list):
        print("\n=== СПИСОК СОТРУДНИКОВ ===")
        for user in user_list:
            print(f"""\nСотрудник {user.get_id()}:
Имя: {user.get_name()}
Доступ: {user.get_access()}""")

users = []

user1 = User("u-01", "Николай Петров")
user2 = User("u-02", "Екатерина Максимова")
admin = Admin("a-01", "Иван Иванов")

admin.add_user(users, user1)
admin.add_user(users, user2)
admin.add_user(users, admin)
admin.info(users)

user2.set_name("Екатерина Иванова")
admin.info(users)