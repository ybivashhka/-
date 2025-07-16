# Трекер привычек
CLI-утилита на Python для отслеживания привычек и визуализации прогресса. Позволяет добавлять привычки, отмечать их выполнение и строить графики прогресса.

1. Возможности




    - Добавление новых привычек.



    - Отметка выполнения привычек по датам.



    - Построение графика прогресса для выбранной привычки.


    - Вывод статистики по всем привычкам.



    - Сохранение данных в JSON.

2. Установка

    - Склонируйте репозиторий:
     
      git clone https://github.com/yourusername/habit-tracker.git
      
      cd habit-tracker
    - Установите зависимости:

      pip install matplotlib

    - Запустите скрипт:

      python habit_tracker.py --help

3. Использование
   
      - Добавить привычку:

       python habit_tracker.py ---add "Пить воду"



      - Отметить выполнение:

       python habit_tracker.py --mark "Пить воду"



      - Построить график:

       python habit_tracker.py --plot "Пить воду" --output progress.png



      - Показать статистику:

       python habit_tracker.py --stats

 4. Пример вывода

       === Стestatика привычек ===
   
      Пить воду: 10 выполнений

      Читать книгу: 5 выполнений


5. Скриншоты

<img width="912" height="453" alt="image" src="https://github.com/user-attachments/assets/0e46c19c-0e49-45e8-aceb-c954598b4beb" />

6. Требования




      - Python 3+



      - matplotlib для построения графиков



