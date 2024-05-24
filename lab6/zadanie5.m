function [country, source, degrees, x_coarse, x_fine, y_original, y_yearly, y_approximation, mse, msek] = zadanie5(energy)

    country = 'Poland';
    source = 'Hydro';
    degrees = [1, 3, 5, 8];

    x_coarse = [];
    x_fine = [];
    y_original = [];
    y_yearly = [];
    y_approximation = [];
    mse = [];
    msek = [];

    if isfield(energy, country) && isfield(energy.(country), source)
        y_original = energy.(country).(source).EnergyProduction;
        n_years = floor(length(y_original) / 12);
        y_cut = y_original(end-12*n_years+1:end);
        y4sum = reshape(y_cut, [12 n_years]);
        y_yearly = sum(y4sum, 1)';

        N = length(y_yearly);
        P = (N-1)*8 + 1;
        x_coarse = linspace(0, 1, N)';
        x_fine = linspace(0, 1, P)';

        kmax = N;
        disp(N);

        mse = zeros(N, 1);
        msek = zeros(N-1, 1);
       
        y_approximation = cell(1, N);

        disp(mat2str(size(y_approximation)));

        for i = 1:N
            X = dct2_custom(y_yearly, N);
            y_approximation{i} = idct2_custom(X, i, N, P);
            y_approx_coarse = idct2_custom(X, i, N, N);
            mse(i) = calcMSE(y_yearly, y_approx_coarse);
        end

        for i = 1:N-1
            msek(i) = calcMSE(y_approximation{i}, y_approximation{i+1});
        end

        disp(mat2str(size(y_approximation)));
       figure;

        % roczne i aproksymacja
        subplot(3, 1, 1);
        plot(x_coarse, y_yearly, 'k', 'DisplayName', 'Roczne dane', 'LineWidth', 1.5);
        hold on;
        colors = ['r', 'g', 'b', 'm'];
        for i = 1:length(degrees)
            if degrees(i) <= length(y_approximation)
                plot(x_fine, y_approximation{degrees(i)}, colors(i), 'DisplayName', sprintf('Degree %d', degrees(i)));
            end
        end
        hold off;
        title('Aproksymacja rocznej produkcji');
        xlabel('Czas');
        ylabel('Roczna produkcja energii');
        legend('show');
        grid on;


        subplot(3, 1, 2);
        semilogy(1:N, mse, '-');
        title('Błąd średniokwadratgowy dla różnych stopni aproksymacji cosinusa');
        xlabel('Stopień');
        ylabel('Błąd średniokwadratowy');
        grid on;


        subplot(3, 1, 3);
        semilogy(1:N-1, msek, '-');
        title('Zbieżność dla stopni aproksymacji');
        xlabel('stopień');
        ylabel('różnica błędu');
        grid on;

        print -dpng 'zadanie5.png';

    else
        disp(['Dane dla (country=', country, ') oraz (source=', source, ') nie są dostępne.']);
    end

    disp(mat2str(size(y_approximation)));
end

function X = dct2_custom(x, kmax)
    % Wyznacza kmax pierwszych współczynników DCT-2 dla wektora wejściowego x.
    N = length(x);
    X = zeros(kmax, 1);
    c2 = sqrt(2/N);
    c3 = pi/2/N;
    nn = (1:N)';

    X(1) = sqrt(1/N) * sum(x(nn));
    for k = 2:kmax
        X(k) = c2 * sum(x(nn) .* cos(c3 * (2*(nn-1)+1) * (k-1)));
    end
end

function x = idct2_custom(X, kmax, N, P)
    % Wyznacza wartości aproksymacji cosinusowej x.
    % X - współczynniki DCT
    % kmax - liczba współczynników DCT zastosowanych do wyznaczenia wektora x
    % N - liczba danych dla których została wyznaczona macierz X
    % P - długość zwracanego wektora x (liczba wartości funkcji aproksymującej w przedziale [0,1])
    x = zeros(P, 1);
    kk = (2:kmax)';
    c1 = sqrt(1/N);
    c2 = sqrt(2/N);
    c3 = pi * (N - 1) / (2 * N * (P - 1));
    c4 = -(pi * (N - P)) / (2 * N * (P - 1));

    for n = 1:P
        x(n) = c1 * X(1) + c2 * sum(X(kk) .* cos((c3 * (2 * (n-1) + 1) + c4) * (kk - 1)));
    end
end

function mse = calcMSE(y_original, y_approx)
    n = length(y_original);
    mse = sum((y_original - y_approx).^2) / n;
end
