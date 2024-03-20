function [A,b,M,bm,x,err_norm,time,iterations,index_number] = solve_Jacobi(N)


% A - macierz z równania macierzowego A * x = b
% b - wektor prawej strony równania macierzowego A * x = b
% M - macierz pomocnicza opisana w instrukcji do Laboratorium 3 – sprawdź wzór (5) w instrukcji, który definiuje M jako M_J.
% bm - wektor pomocniczy opisany w instrukcji do Laboratorium 3 – sprawdź wzór (5) w instrukcji, który definiuje bm jako b_{mJ}.
% x - rozwiązanie równania macierzowego
% err_norm - norma błędu rezydualnego rozwiązania x; err_norm = norm(A*x-b)
% time - czas wyznaczenia rozwiązania x
% iterations - liczba iteracji wykonana w procesie iteracyjnym metody Jacobiego
% index_number - Twój numer indeksu
index_number = 193184;
L1 = mod(index_number, 10);

[A,b] = generate_matrix(N, L1);

x =  ones(N,1);

D = diag(diag(A));
L = tril(A,-1);
U = triu(A,1);


MAX_ITERATIONS = 1000;
DESIRED_ERROR = 1e-12;






M = -inv(D) * (L + U);
bm = inv(D) * b;


tic();

iterations = 0;
for iteration = 1:MAX_ITERATIONS


x = M*x + bm;

err_norm = norm(A*x-b);

iterations = iterations +1;
if err_norm < DESIRED_ERROR
        %disp(err_norm);
        break; 
end

disp(err_norm);

end


time = toc();




end