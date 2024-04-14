from methods import exerciseA, exerciseB, exerciseC, plot_jacobi_gaus, show_results
import numpy as np




def main():
    
    # EXERCISE A
    A, b, x = exerciseA()



    # EXERCISE B
    exB_result = exerciseB(A, b, x)
    
    result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac = exB_result[0]

    result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus = exB_result[1]

    show_results((result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac, "Jacobi"))
    show_results((result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus, "Gaus Seidel"))

    plot_jacobi_gaus((iterations_jac, residual_norm_jac), (iterations_gaus, residual_norm_gaus))

    

    # EXERCISE C
    exC_result = exerciseC()

    result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac = exC_result[0]

    result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus = exC_result[1]


    show_results((result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac, "Jacobi"))
    show_results((result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus, "Gaus Seidel"))


    # if not converged_jac or not converged_gaus:
    #     if not converged_jac:
    #         print("jacobi did not congerge")

    #     if not converged_gaus:
    #         print("gaus did not congerge")


    plot_jacobi_gaus((iterations_jac, residual_norm_jac), (iterations_gaus, residual_norm_gaus))

    


if __name__ == "__main__":
    main()

    