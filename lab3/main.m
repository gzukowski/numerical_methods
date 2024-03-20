
N = 1000:1000:8000;
n = length(N);

index_number = 193184;
L1 = mod(index_number, 10);

vtime_direct = ones(1,n); 

%{
for size = 1:n
    size

    [A,b,x,time_direct,err_norm,index_number] = solve_direct(N(size));

    vtime_direct(size) = time_direct;



end

plot_direct(N, vtime_direct);

%}



%[A,b,M,bm,x,err_norm,time,iterations,index_number] = solve_Jacobi(100);


%disp(iterations);

[A,b,M,bm,x,err_norm,time,iterations,index_number] = solve_Gauss_Seidel(100);


disp(iterations);