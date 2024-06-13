function [integration_error, Nt, ft_5, integral_1000] = zadanie1()
    % Numeryczne całkowanie metodą prostokątów.
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
    integration_error = [0];
    integral_1000 = [0];
    ft_5 = f(5);
    step = 5 / 1000;
    i = 0;

    integral_1000 = rectangle_integ(@f, 1000);

    for i = 1:length(Nt)
        N = Nt(i);
        integration_result = rectangle_integ(@f, N);
        integration_error(i) = abs(integration_result - reference_value);
    end

    loglog(Nt, integration_error);
    xlabel('Przedziały (N)');
    ylabel('Blad calkowania');
    title('Blad calkowania vs. Liczba przedzialow');
    grid on;
    print -dpng 'zadanie1.png';

end

function [value] = f(t)
sigma = 3;
mi = 10;
value = 1 / (sigma * sqrt(2*pi)) * exp( (-(t-mi)^2)/ (2*sigma^2) );

end

function integral = rectangle_integ(f, N)
    a = 0;
    b = 5;
    
    h = (b - a) / N;
    
    integral = 0;
    
    for i = 1:N
        x = a + (i - 0.5) * h;
        integral = integral + f(x);
    end
    
    integral = integral * h;
end