# Требования к приложению
Необходимо разработать небольшую систему для планирования мероприятия. Планирование
мероприятия осуществляется голосованием в две фазы: в первой фазе голосования собираются
предпочтения пользователей по мероприятию, во второй фазе голосования система принуждает
пользователей к единогласному решению.
1. При запуске страницы пользователю необходимо ввести имя и пароль, либо
зарегистрироваться.
2. Пользователь создаёт голосование, указывая продолжительность первой и второй фазы
голосования в минутах.
3. Первая фаза голосования. Отображается список предложенных мероприятий, обратный отчёт
времени до завершения первой фазы голосования и суммарный счётчик проголосовавших
пользователей.
4. У любого пользователя есть возможность предложить произвольное мероприятие.
5. Когда время первой фазы голосования истекает, всем пользователям отображается
следующая информация.
a. Мероприятие, набравшее максимальное количество голосов.
b. Cписок пользователей, которые проголосовали за это мероприятие.
6. Вторая фаза голосования начинается сразу, как только завершается первая фаза.
7. Пользователям предлагается согласиться с выбранным мероприятием, либо отказаться.
8. Если пользователь соглашается, он включается в список участников мероприятия. В случае
отказа, участник не включается в список.
9. После окончания второй фазы голосования пользователям отображается список участников
мероприятия.
10. Вся информация на странице обновляется у всех пользователей без перезагрузки страницы.
## Требования к реализации, технологиям и инструментам
1. Выбор серверного языка программирования и фреймворка - на ваше усмотрение.
2. Обязательно использование COMET-технологии (WebSockets, Long Polling, PUSH).
## Релиз
1. Ссылка на репозиторий исходного кода. Репозиторий должен быть публично доступным.
2. Ссылка на развернутое приложение, доступное через Интернет.
_______________________________________________________________________________
### Python
Установите Python версии 3.6 и выше.
### Зависмости
Установите все зависмости из файла requirements.txt
### Запуск программы
Для запуска программы используйте команду 'python ./manage.py runserver'
### Демка
https://mahamerz.herokuapp.com/