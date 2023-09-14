import math

# Функция для получения количества критериев от пользователя
def get_criteria_count():
    while True:
        try:
            n = abs(int(input('\nВведите количество критериев (целое, положительное число): ')))
            if n == 0:
                print('Введен ноль.\nПопробуйте снова.\n')
                continue
            elif n == 1:
                print('Сравнение одного критерия невозможно(но коэффициент у него будет равен 1)')
            return n
        except ValueError:
            print('Введено некорректное значение количества критериев.\nПопробуйте снова\n')

# Функция создания таблицы сравнения на основе данных, введенных пользователем
def create_comparison_table(n):
    table = [[1.0] * n for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            while True:
                try:
                    table[i][j] = float(input(f'Насколько параметр {i+1} важнее параметра {j+1}: '))
                    table[j][i] = 1 / table[i][j]
                    table[i][j] = round_down(table[i][j])
                    table[j][i] = round_down(table[j][i])
                    break
                except ValueError:
                    print('Введено некорректное значение.\nПопробуйте снова.\n')
                except ZeroDivisionError:
                    print('Введен ноль.\nПопробуйте снова.\n')
    return table

# Функция для округления числа до двух знаков после запятой, если оно меньше 1, иначе округление до ближайшего целого числа
def round_down(num):
    return float(math.floor(num)) if num > 1 else float(math.floor(num * 100)/100)

# Функция расчета весов на основе сравнительной таблицы
def calculate_weights(n, table):
    list_of_sum = [sum(row) for row in table]
    list_of_alpha = [math.floor((s/sum(list_of_sum)) * 100) / 100 for s in list_of_sum]
    sum_of_alphas = round(sum(list_of_alpha), 2)
    while sum_of_alphas != 1:
        adjustment = -0.01 if sum_of_alphas > 1 else 0.01
        target_index = list_of_alpha.index(min(list_of_alpha) if sum_of_alphas > 1 else max(list_of_alpha))
        list_of_alpha[target_index] += adjustment
        sum_of_alphas = round(sum(list_of_alpha), 2)
    return list_of_alpha

# Функция вывода сравнительной таблицы и весов
def print_results(n, table, list_of_alpha):
    print('\nТаблица попарного сравнения')
    for i in range(n):
        print('\t'.join(str(x) for x in table[i]))
    print('\nКоэффициенты')
    for i in range(n):
        print(f'Коэффициент критерия {i+1}: {round(list_of_alpha[i], 2)}')

# Главная функция, вызывающая все остальные функции
def main():
    n = get_criteria_count()
    if n > 1:
        table = create_comparison_table(n)
        list_of_alpha = calculate_weights(n, table)
        print_results(n, table, list_of_alpha)

if __name__ == "__main__":
    main()
