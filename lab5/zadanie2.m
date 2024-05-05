function [nodes_Chebyshev, V, V2, original_Runge, interpolated_Runge, interpolated_Runge_Chebyshev] = zadanie2()
% nodes_Chebyshev - wektor wierszowy zawierający N=16 węzłów Czebyszewa drugiego rodzaju
% V - macierz Vandermonde obliczona dla 16 węzłów interpolacji rozmieszczonych równomiernie w przedziale [-1,1]
% V2 - macierz Vandermonde obliczona dla węzłów interpolacji zdefiniowanych w wektorze nodes_Chebyshev
% original_Runge - wektor wierszowy zawierający wartości funkcji Runge dla wektora x_fine=linspace(-1, 1, 1000)
% interpolated_Runge - wektor wierszowy wartości funkcji interpolującej określonej dla równomiernie rozmieszczonych węzłów interpolacji
% interpolated_Runge_Chebyshev - wektor wierszowy wartości funkcji interpolującej wyznaczonej
%       przy zastosowaniu 16 węzłów Czebyszewa zawartych w nodes_Chebyshev 
    N = 16;
    x_fine = linspace(-1, 1, 1000);
    

    V = vandermonde_matrix(N);
    


    original_Runge = 1 ./ (1 + 25 * x_fine.^2);
    interpolated_Runge = [] %cell(1, length(N));

    subplot(2,1,1);
    plot(x_fine, original_Runge, 'DisplayName', ["Wartości funkcji Rungego"]);
    title('Interpolacja Rungego');
    xlabel('x');
    ylabel('f(x) - wartość');
    hold on;
   
    x_nodes = linspace(-1, 1, N);  % węzły interpolacji
    values = 1 ./ (1 + 25 * x_nodes.^2)  % wartości funkcji interpolowanej w węzłach interpolacji
    plot(x_nodes, values, 'o', 'DisplayName', ["Wartości funkcji Rungego w węzłach"])

    c_runge = V \ values'; % współczynniki wielomianu interpolującego
    interpolated_Runge = polyval(flipud(c_runge), x_fine); % interpolacja
    plot(x_fine, interpolated_Runge, 'DisplayName', ["Wartosc interpolacji"]);  % plot interpolated_Runge{i}
    legend show;
    hold off

    subplot(2,1,2);
    plot(x_fine, original_Runge, 'DisplayName', ["Wartości funkcji Rungego"]);

    title('Interpolacja z węzłami Chebysheva');
    xlabel('x');
    ylabel('f(x) - wartość');
    hold on;


    nodes_Chebyshev = get_Chebyshev_nodes(N);
    V2 = vandermonde_matrix_chebyshev(N, nodes_Chebyshev);
    values = 1 ./ (1 + 25 * nodes_Chebyshev.^2)  % wartości funkcji interpolowanej w węzłach interpolacji

    plot(nodes_Chebyshev, values, 'o', 'DisplayName', ["Wartości funkcji Rungego w węzłach"])

    c_runge = V2 \ values'; % współczynniki wielomianu interpolującego
    interpolated_Runge_Chebyshev = polyval(flipud(c_runge), x_fine); % interpolacja


    plot(x_fine, interpolated_Runge_Chebyshev, 'DisplayName', ["Wartości interpolacji z węzłami Chebysheva"]);  % plot interpolated_Runge{i}
    legend show;
    hold off

end

function V = vandermonde_matrix_chebyshev(N, x_coarse)
    for i = 1:N
        V(:, i) = x_coarse.^(i-1);
    end
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

end

function nodes = get_Chebyshev_nodes(N)
    % oblicza N węzłów Czebyszewa drugiego rodzaju
    nodes = size(N);

    for i = 1:N
        nodes(i) = cos( ( (i-1)*pi) / (N-1));
    end
end