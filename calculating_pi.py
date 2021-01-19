def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operator: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += numerator / denominator * operator
        operator *= -1.0
        denominator += 2.0
    return pi


if __name__ == '__main__':
    print(calculate_pi(1000))