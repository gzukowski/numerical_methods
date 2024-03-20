N = 1000:1000:8000;
n = length(N);

index_number = 193184;
L1 = mod(index_number, 10);

time_Jacobi = ones(1,n);
time_Gauss_Seidel = ones(1,n);



for size = 1:n

    [A,b,M,bm,x,err_norm,time,iterations,index_number] = solve_Jacobi(N(size));

    time_Jacobi(size) = time;
    iterations_Jacobi(size) = iterations;


    [A,b,M,bm,x,err_norm,time,iterations,index_number] = solve_Gauss_Seidel(N(size));

    time_Gauss_Seidel(size) = time;
    iterations_Gauss_Seidel(size) = iterations;



end

%disp(time_Jacobi);


%disp(time_Gauss_Seidel);

plot_problem_5(N,time_Jacobi,time_Gauss_Seidel,iterations_Jacobi,iterations_Gauss_Seidel);