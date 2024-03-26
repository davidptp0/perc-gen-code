import random
import math

# Функция для оценки решения
def fitness(x, y):
    return 1 / (1 + x**2 + y**2)

# Генетический алгоритм с методом элит
def ga_elitist(population_size, max_generations, mutation_rate):
    # Инициализация популяции
    population = [(random.random(), random.random()) for _ in range(population_size)]

    # Цикл генетического алгоритма
    for generation in range(max_generations):
        # Оценка каждого решения
        fitness_values = [fitness(x, y) for x, y in population]

        # Отбор лучших решений
        elite = sorted(zip(fitness_values, population), reverse=True)[:population_size//2]
        population = [pair[1] for pair in elite]

        # Мутация и скрещивание
        for _ in range(population_size - len(elite)):
            parent1, parent2 = random.choice(population), random.choice(population)
            child = (parent1[0] + parent2[0], parent1[1] + parent2[1])
            if random.random() < mutation_rate:
                child = (random.random(), random.random())
            population.append(child)

    return population

# Генетический алгоритм с методом рулетки
def ga_roulette(population_size, max_generations, mutation_rate):
    # Инициализация популяции
    population = [(random.random(), random.random()) for _ in range(population_size)]

    # Цикл генетического алгоритма
    for generation in range(max_generations):
        # Оценка каждого решения
        fitness_values = [fitness(x, y) for x, y in population]

        # Отбор лучших решений
        probabilities = [fitness_value / sum(fitness_values) for fitness_value in fitness_values]
        selected = [random.random() < probability for probability in probabilities]
        elite = [pair for pair, selected in zip(population, selected) if selected]

        # Мутация и скрещивание
        for _ in range(population_size - len(elite)):
            parent1, parent2 = random.choice(elite), random.choice(elite)
            child = (parent1[0] + parent2[0], parent1[1] + parent2[1])
            if random.random() < mutation_rate:
                child = (random.random(), random.random())
            elite.append(child)

    return elite

# Запуск генетического алгоритма
best_solution_elitist = ga_elitist(100, 1000, 0.1)
best_solution_roulette = ga_roulette(100, 1000, 0.1)

print(f"Лучшее решение с методом элит: {best_solution_elitist}")
print(f"Лучшее решение с методом элит: {best_solution_roulette}")