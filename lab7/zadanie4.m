function [integration_error, Nt, ft_5, integral_1000] = zadanie4()
    % Numeryczne całkowanie metodą trapezów.
    % Nt - wektor zawierający liczby podprzedziałów całkowania
    % integration_error - integration_error(1,i) zawiera błąd całkowania wyznaczony
    %   dla liczby podprzedziałów równej Nt(i). Zakładając, że obliczona wartość całki
    %   dla Nt(i) liczby podprzedziałów całkowania wyniosła integration_result,
    %   to integration_error(1,i) = abs(integration_result - reference_value),
    %   gdzie reference_value jest wartością referencyjną całki.
    % ft_5 - gęstość funkcji prawdopodobieństwa dla n=5
    % integral_1000 - całka od 0 do 5 funkcji gęstości prawdopodobieństwa
    %   dla 1000 podprzedziałów całkowania

    reference_value = 0.0473612919396179; % wartość referencyjna całki

    Nt = 5:50:10^4;
    integration_error = [];

    ft_5 = f(5);
    yrmax = ft_5 * 1.05;
    xr = cell(1, length(Nt));
    yr = cell(1, length(Nt));
    integral_1000 = monte_carlo(@f, 1000, yrmax);
    %integral_1000 = [];

    for i = 1:length(Nt)
        N = Nt(i);
        [integration_result,  xr{i}, yr{i}] = monte_carlo(@f, N, yrmax);
        integration_error(i) = abs(integration_result - reference_value);
    end

    loglog(Nt, integration_error);
    xlabel('Próbki (N)');
    ylabel('Blad calkowania');
    title('Blad calkowania vs. Liczba próbek');
    grid on;
    print -dpng 'zadanie4.png';

end

function [value] = f(t)
sigma = 3;
mi = 10;
value = 1 / (sigma * sqrt(2*pi)) * exp( (-(t-mi)^2)/ (2*sigma^2) );

end

function [integral, x_rand, y_rand] = monte_carlo(f, N, yrmax)
    a = 0;
    b = 5;

    x_rand = a + (b-a) * rand(1, N);
    y_rand = yrmax * rand(1, N);
    

    values = arrayfun(f, x_rand);

    accepted_points = sum(y_rand <= values);

    %{
    values = zeros(1, N);
    for j = 1:N
        values(j) = f(x_rand(j));
    end

    accepted_points = 0;
    for j = 1:N
        if y_rand(j) <= values(j)
            accepted_points = accepted_points + 1;
        end
    end
    %}
    integral = b * yrmax * sum(accepted_points) / N;
    
end