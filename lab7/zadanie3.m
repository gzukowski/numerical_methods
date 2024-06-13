function [integration_error, Nt, ft_5, integral_1000] = zadanie3()
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
    integral_1000 = simpsone(@f, 1000);
    %integral_1000 = [];

    for i = 1:length(Nt)
        N = Nt(i);
        integration_result = simpsone(@f, N);
        integration_error(i) = abs(integration_result - reference_value);
    end

    loglog(Nt, integration_error);
    xlabel('Przedziały (N)');
    ylabel('Blad calkowania');
    title('Blad calkowania vs. Liczba przedzialow');
    grid on;
    print -dpng 'zadanie3.png';

end

function [value] = f(t)
sigma = 3;
mi = 10;
value = 1 / (sigma * sqrt(2*pi)) * exp( (-(t-mi)^2)/ (2*sigma^2) );

end

function integral = simpsone(f, N)
    a = 0;
    b = 5;


    h = (b - a) / N;
   
    integral = 0;
    for i = 1:N
        x_i = a + (i-1) * h;
        x_i1 = a + i * h;
        integral = integral + (f(x_i) + 4 * f((x_i + x_i1) / 2) + f(x_i1));
    end
    
    integral = integral * h / 6;
end