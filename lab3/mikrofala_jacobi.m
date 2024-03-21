function [M,bm,x,err_norm,time,iterations,index_number] = mikrofala_jacobi(N, A, b)


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

x =  ones(N,1);

D = diag(diag(A));
L = tril(A,-1);
U = triu(A,1);


MAX_ITERATIONS = 1000;
DESIRED_ERROR = 1e-12;






M = -inv(D) * (L + U);
bm = inv(D) * b;


tic();
last_error = 0;
iterations = 0;
for iteration = 1:MAX_ITERATIONS


x = M*x + bm;

err_norm = norm(A*x-b);

iterations = iterations +1;

if isnan(err_norm) || isinf(err_norm)
        err_norm = last_error;
        break;
end        

if err_norm < DESIRED_ERROR
        %disp(err_norm);
        break; 
end
last_error = err_norm;
disp(err_norm);

end


time = toc();




end