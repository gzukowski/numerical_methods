from methods import exerciseA, exerciseB, exerciseC, exerciseD, exerciseE, plot_jacobi_gaus, plot_times, show_results




def main():
    
    # EXERCISE A
    A, b, x = exerciseA()


    # EXERCISE B
    exB_result = exerciseB(A, b, x)
    
    result_jac, iterations_jac, residual_norm_jac, time_jac, converged_jac = exB_result[0]

    result_gaus, iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus = exB_result[1]

    show_results((iterations_jac, residual_norm_jac, time_jac, converged_jac, "Jacobi"))
    show_results((iterations_gaus, residual_norm_gaus, time_gaus, converged_gaus, "Gaus Seidel"))

    plot_jacobi_gaus((iterations_jac, residual_norm_jac), (iterations_gaus, residual_norm_gaus))

    
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


    # # EXERCISE E
    # jacobi, gaus, lu  = exerciseE()

    # plot_times(jacobi, gaus, lu)



    


if __name__ == "__main__":
    main()
    

    