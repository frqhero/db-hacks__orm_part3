# Взламываем дневник

Репозиторий содержит [модуль](scripts.py) предназначенный для обеления репутации ученика имеющего проблемы с успеваемостью.
Предназначен для работы с проектом ["Электронный дневник"](https://github.com/devmanorg/e-diary).  
### Позволяет:
1. Все оценки ученика 2 и 3 исправить на 5
2. Удалить все замечания
3. Создать похвалу

### Использование:
Файл scipts.py перенести в корень проекта "Электронный дневник". Импортировать класс в целевой код. Например [management command](management).
* Создаем объект класса, передаем туда данные: фио, название предмета, причина похвалы. 
```python
hack_1 = Hack()
```
Все аргументы необязательные, 
указываются в случае необходимости изменения стандартного поведения (по умолчанию ученик `Фролов Иван`, предмет `Математика`, 
причина похвалы `Отлично!`). 
* Вызываем отдельные методы
  * `fix_marks()`
  * `remove_chastisements()`
  * `create_commendation`  
  * либо все разом 
  путем запуска метода `carry_out_all_features()`.

### Состав репозитория:
1. management - содержит пример менеджмент команды в которой демонстрируются [сценарии](https://gist.github.com/dvmn-tasks/4b354a1f1d7da0267a5922b195dc2d80) работы с классом взлома.
2. scripts.py - код для выполнения взлома. 