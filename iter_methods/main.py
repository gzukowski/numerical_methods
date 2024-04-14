from methods import exerciseA, exerciseB, exerciseC, exerciseD, exerciseE, plot_jacobi_gaus, show_results
import numpy as np




def main():
    
    # # EXERCISE A
    # A, b, x = exerciseA()



    # # EXERCISE B
    # exB_result = exerciseB(A, b, x)
    
    # result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac = exB_result[0]

    # result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus = exB_result[1]

    # show_results((result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac, "Jacobi"))
    # show_results((result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus, "Gaus Seidel"))

    # plot_jacobi_gaus((iterations_jac, residual_norm_jac), (iterations_gaus, residual_norm_gaus))

    

    # # EXERCISE C
    # exC_result = exerciseC()

    # result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac = exC_result[0]

    # result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus = exC_result[1]


    # show_results((iterations_jac, residual_norm_jac, time_jac, converged_jac, "Jacobi"))
    # show_results((iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus, "Gaus Seidel"))

    # plot_jacobi_gaus((iterations_jac, residual_norm_jac), (iterations_gaus, residual_norm_gaus))


    # # EXERCISE D

    # result_lu, norm_lu, time_taken  = exerciseD()

    # show_results((norm_lu, time_taken, "LU"))

    # EXERCISE E

    #jacobi, gaus, lu  = exerciseE()

    jacobi = [0.050002336502075195, 0.21401548385620117, 23.96886968612671, 101.19808721542358, 226.7834231853485]
    gaus = [0.031004905700683594, 0.12300896644592285, 13.313994884490967, 60.36554169654846, 131.05156469345093]
    lu = [0.025998353958129883, 0.17901349067687988, 202.8671476840973, 1858.7307336330414, 6628.71071434021]

    print(jacobi, gaus, lu)



    


if __name__ == "__main__":
    main()
    

    