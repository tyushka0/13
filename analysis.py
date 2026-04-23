"""дорогой дневник, сейчас я сделаю
общую статистику
средние значения по тренировкам
средний сон
средний белой
средний вес
изменение веса
прогресс силы
среднее настроение
максимум колорий
минимум энергии
и проверочку)
"""
import pandas as pd
from src.data_loader import load_data

df = load_data()

# 1. Общая статистика
def basic_stats():
    return df.describe()

# 🏋2. Средние значения по тренировкам
def avg_by_workout():
    return df.groupby("workout_type")[["calories_burned", "duration_min"]].mean()

# 3. Средний сон
def avg_sleep():
    return df["sleep_hours"].mean()

# 4. Средний белок
def avg_protein():
    return df["protein_g"].mean()

# 5. Средний вес
def avg_weight():
    return df["weight_kg"].mean()

# 6. Изменение веса
def weight_change():
    return df["weight_kg"].iloc[-1] - df["weight_kg"].iloc[0]

# 7. Прогресс силы
def strength_progress():
    return {
        "bench_press": df["bench_press_kg"].iloc[-1] - df["bench_press_kg"].iloc[0],
        "squat": df["squat_kg"].iloc[-1] - df["squat_kg"].iloc[0],
        "deadlift": df["deadlift_kg"].iloc[-1] - df["deadlift_kg"].iloc[0],
    }

# 8. Среднее настроение
def avg_mood():
    return df["mood"].mean()

# 9. Максимум калорий
def max_calories_day():
    row = df.loc[df["calories_burned"].idxmax()]
    return {
        "date": row["date"],
        "calories": row["calories_burned"],
        "workout": row["workout_type"]
    }

# 10. Минимум энергии
def min_energy_day():
    row = df.loc[df["energy_level"].idxmin()]
    return {
        "date": row["date"],
        "energy": row["energy_level"],
        "workout": row["workout_type"]
    }

# проверка
if __name__ == "__main__":
    print("📊 Basic stats:\n", basic_stats())
    print("\n😴 Avg sleep:", avg_sleep())
    print("🍗 Avg protein:", avg_protein())
    print("⚖️ Avg weight:", avg_weight())
    print("📈 Weight change:", weight_change())
    print("🏋️ Strength progress:", strength_progress())
    print("😊 Avg mood:", avg_mood())
    print("🔥 Max calories day:", max_calories_day())
    print("😴 Min energy day:", min_energy_day())
    print("\n🏋️ Avg by workout:\n", avg_by_workout())