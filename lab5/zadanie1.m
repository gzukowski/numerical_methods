function [V, original_Runge, original_sine, interpolated_Runge, interpolated_sine] = zadanie1()
% Rozmiar tablic komórkowych (cell arrays) V, interpolated_Runge, interpolated_sine: [1,4].
% V{i} zawiera macierz Vandermonde wyznaczoną dla liczby węzłów interpolacji równej N(i)
% original_Runge - wektor wierszowy zawierający wartości funkcji Runge dla wektora x_fine=linspace(-1, 1, 1000)
% original_sine - wektor wierszowy zawierający wartości funkcji sinus dla wektora x_fine
% interpolated_Runge{i} stanowi wierszowy wektor wartości funkcji interpolującej 
%       wyznaczonej dla funkcji Runge (wielomian stopnia N(i)-1) w punktach x_fine
% interpolated_sine{i} stanowi wierszowy wektor wartości funkcji interpolującej
%       wyznaczonej dla funkcji sinus (wielomian stopnia N(i)-1) w punktach x_fine
    N = 4:4:16;
    x_fine = linspace(-1, 1, 1000);
    original_Runge = 1 ./ (1 + 25 * x_fine.^2);

    subplot(2,1,1);
    interpolated_Runge = cell(1, length(N));
    plot(x_fine, original_Runge, 'DisplayName', ["Wartości funkcji Runge"]);
    title('Interpolacja Runge');
    xlabel('x');
    ylabel('f(x) - wartość');
    hold on;
    for i = 1:length(N)
        V{i} = vandermonde_matrix(N(i));% macierz Vandermonde
        x_nodes = linspace(-1, 1, N(i));  % węzły interpolacji
        values = 1 ./ (1 + 25 * x_nodes.^2)  % wartości funkcji interpolowanej w węzłach interpolacji

        c_runge = V{i} \ values'; % współczynniki wielomianu interpolującego
        interpolated_Runge{i} = polyval(flipud(c_runge), x_fine); % interpolacja
        plot(x_fine, interpolated_Runge{i}, 'DisplayName', ['N=' num2str(N(i))]);  % plot interpolated_Runge{i}
    end
    legend show;
    hold off

    original_sine = sin(2 * pi * x_fine);
    subplot(2,1,2);
    plot(x_fine, original_sine, 'DisplayName', ["Wartości funkcji sinus"]);

    title('Interpolacja sinusa');
    xlabel('x');
    ylabel('f(x) - wartość');
    hold on;

    
    interpolated_sine = cell(1, length(N));
    for i = 1:length(N)
        x_nodes = linspace(-1, 1, N(i));
        values = sin(2 * pi * x_nodes); % Wartości funkcji sinus w węzłach
        c_sine = V{i} \ values'; % Rozwiązanie układu liniowego Vc = y
        interpolated_sine{i} = polyval(flipud(c_sine), x_fine); % Obliczenie interpolacji
        plot(x_fine, interpolated_sine{i}, 'DisplayName', ['N=' num2str(N(i))]);
    end
    legend show;
    hold off

    print('zadanie1','-dpng')
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