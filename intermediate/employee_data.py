from functools import reduce

# employee data
employees = [
    ("Alice", 150, 4.7, 10),
    ("Bob", 180, 4.1, 8),
    ("Charlie", 120, 4.9, 9),
    ("David", 170, 4.4, 7),
    ("Charles", 250, 2.1, 5),
    ("John", 175, 4.8, 9)
]


def calculate_score(sales, rating, tasks):
    """Calculates score based on weighted sales, rating and tasks score.

    Args:
        sales (float): sales score
        rating (float): ratings
        tasks (float): tasks score

    Returns:
        float: Returns weighted sum of sales, rating and tasks.
    """
    return sales * 0.5 + rating * 30 + tasks * 10


# calculate scores from a list of tuples
employee_scores = list(
    map(lambda emp: (emp[0], calculate_score(emp[1], emp[2], emp[3])), employees))

# filter employees based on score
thresh = 200
filtered_employees = list(filter(lambda x: x[1] > thresh, employee_scores))

# sort employees based on score
sorted_employees = sorted(filtered_employees, key=lambda x: x[1], reverse=True)

# rank and create final report
ranks = range(1, len(sorted_employees)+1)
final_report = list(zip(ranks, sorted_employees))

# calculate total score
total_score = reduce((lambda acc, x: acc+x[1]), sorted_employees, 0)

if __name__ == '__main__':
    # print findings
    print("Employee Rankings:")
    for rank, emp in final_report:
        print(f"Rank {rank}: {emp[0]} with a score of {emp[1]}")

    print(f"\nTotal score of top employees: {total_score}")
