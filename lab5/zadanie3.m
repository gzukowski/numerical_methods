function [matrix_condition_numbers, max_coefficients_difference_1, max_coefficients_difference_2] = zadanie3()
% Zwracane są trzy wektory wierszowe:
% matrix_condition_numbers - współczynniki uwarunkowania badanych macierzy Vandermonde
% max_coefficients_difference_1 - maksymalna różnica między referencyjnymi a obliczonymi współczynnikami wielomianu,
%       gdy b zawiera wartości funkcji liniowej
% max_coefficients_difference_2 - maksymalna różnica między referencyjnymi a obliczonymi współczynnikami wielomianu,
%       gdy b zawiera zaburzone wartości funkcji liniowej

N = 5:40;
N
%% chart 1
matrix_condition_numbers = zeros(1, length(N));
subplot(3,1,1);

title('Wzrost współczynnika uwarunkowania macierzy Vandermonde');
xlabel('wspolczynnik');
ylabel('rozmiar');
hold on;
for i = 1:length(N)
    N(i)
    V = vandermonde_matrix(N(i));
    matrix_condition_numbers(i) = cond(V);
end
semilogy(N, matrix_condition_numbers, '-');
hold off;



%% chart 2
subplot(3,1,2);
title('Błąd interpolacji dla funkcji liniowej');
xlabel('Rozmiar N');
ylabel('Maksymalna różnica współczynników');
hold on;
a1 = randi([20,30]);
for i = 1:length(N)
    ni = N(i);
    V = vandermonde_matrix(ni);
    
    % Niech wektor b zawiera wartości funkcji liniowej
    b = linspace(0,a1,ni)';
    reference_coefficients = [ 0; a1; zeros(ni-2,1) ]; % tylko a1 jest niezerowy
    
    % Wyznacznie współczynników wielomianu interpolującego
    calculated_coefficients = V \ b;

    max_coefficients_difference_1(i) = max(abs(calculated_coefficients-reference_coefficients));
end
plot(N, max_coefficients_difference_1, '-');
hold off;

%% chart 3
subplot(3,1,3);
title('Błąd interpolacji dla zaburzonej funkcji liniowej');
xlabel('Rozmiar N');
ylabel('Maksymalna różnica współczynników');
hold on;

for i = 1:length(N)
    ni = N(i);
    V = vandermonde_matrix(ni);
    
    % Niech wektor b zawiera wartości funkcji liniowej nieznacznie zaburzone
    b = linspace(0,a1,ni)' + rand(ni,1)*1e-10;
    reference_coefficients = [ 0; a1; zeros(ni-2,1) ]; % tylko a1 jest niezerowy
    
    % Wyznacznie współczynników wielomianu interpolującego
    calculated_coefficients = V \ b;
    
    max_coefficients_difference_2(i) = max(abs(calculated_coefficients-reference_coefficients));
end
plot(N, max_coefficients_difference_2, '-');
hold off;

end


function V = vandermonde_matrix(N)
     % Generuje macierz Vandermonde dla N równomiernie rozmieszczonych w przedziale [-1, 1] węzłów interpolacji
    x_coarse = linspace(-1,1,N);

    V = zeros(N, N);
    

    for i = 1:N
        V(:, i) = x_coarse.^(i-1);
    end
    %for j = 1:N
    %   for i = 1:N
    %        V(i, j) = x_coarse(i)^(N-j);
    %    end
    %end

    V
end