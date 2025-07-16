import argparse
import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

def load_habits(file_path="habits.json"):
    """Загружает привычки из JSON-файла."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {"habits": {}}

def save_habits(habits, file_path="habits.json"):
    """Сохраняет привычки в JSON-файл."""
    with open(file_path, 'w') as f:
        json.dump(habits, f, indent=4)

def add_habit(habits, habit_name):
    """Добавляет новую привычку."""
    if habit_name not in habits["habits"]:
        habits["habits"][habit_name] = []
        print(f"Привычка '{habit_name}' добавлена.")
    else:
        print(f"Привычка '{habit_name}' уже существует.")
    return habits

def mark_habit(habits, habit_name):
    """Отмечает выполнение привычки на текущую дату."""
    if habit_name in habits["habits"]:
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in habits["habits"][habit_name]:
            habits["habits"][habit_name].append(today)
            print(f"Привычка '{habit_name}' отмечена за {today}.")
        else:
            print(f"Привычка '{habit_name}' уже отмечена за сегодня.")
    else:
        print(f"Привычка '{habit_name}' не найдена.")
    return habits

def plot_progress(habits, habit_name, output_image=None):
    """Строит график прогресса для привычки."""
    if habit_name not in habits["habits"]:
        print(f"Привычка '{habit_name}' не найдена.")
        return

    dates = habits["habits"][habit_name]
    date_counts = defaultdict(int)
    for date in dates:
        date_counts[date] += 1

    sorted_dates = sorted(date_counts.keys())
    counts = [date_counts[date] for date in sorted_dates]

    plt.figure(figsize=(10, 5))
    plt.plot(sorted_dates, counts, marker='o', color='teal')
    plt.title(f"Прогресс привычки: {habit_name}")
    plt.xlabel("Дата")
    plt.ylabel("Выполнения")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    if output_image:
        plt.savefig(output_image)
        print(f"График сохранен в {output_image}")
    else:
        plt.show()
    plt.close()

def show_stats(habits):
    """Выводит статистику по всем привычкам."""
    print("\n=== Статистика привычек ===")
    for habit, dates in habits["habits"].items():
        count = len(dates)
        print(f"{habit}: {count} выполнений")

def main():
    parser = argparse.ArgumentParser(description="Трекер привычек: отслеживайте свои привычки")
    parser.add_argument('--add', help="Добавить новую привычку")
    parser.add_argument('--mark', help="Отметить выполнение привычки")
    parser.add_argument('--plot', help="Построить график прогресса для привычки")
    parser.add_argument('--output', help="Путь для сохранения графика", default=None)
    parser.add_argument('--stats', action='store_true', help="Показать статистику")

    args = parser.parse_args()

    habits = load_habits()

    if args.add:
        habits = add_habit(habits, args.add)
        save_habits(habits)
    elif args.mark:
        habits = mark_habit(habits, args.mark)
        save_habits(habits)
    elif args.plot:
        plot_progress(habits, args.plot, args.output)
    elif args.stats:
        show_stats(habits)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()