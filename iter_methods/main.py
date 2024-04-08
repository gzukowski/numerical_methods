from methods import exerciseA, exerciseB


if __name__ == "__main__":

    A, b, x = exerciseA()
    result, iterations, residual_norm, time = exerciseB(A, b, x)

    print(iterations, residual_norm[-1], time)