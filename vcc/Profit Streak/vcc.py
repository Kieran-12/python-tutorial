from data import *


def find_best_profit_streak(profits):
    current_max = profits[0]
    global_max = profits[0]

    start = 0
    end = 0
    a = 0

    for i in range(1, len(profits)):
        if profits[i] > current_max + profits[i]:
            current_max = profits[i]
            a = i
        else:
            current_max += profits[i]

        if current_max > global_max:
            global_max = current_max
            start = a
            end = i

    return global_max, start, end


best_profit, streak_start, streak_end = find_best_profit_streak(daily_profit)

print(
    f"The best profit streak is from day {dates[streak_start]} to day {dates[streak_end]} with a total profit of ${best_profit:.2f}."
)
