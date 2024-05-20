function [country, source, degrees, x_coarse, x_fine, y_original, y_yearly, y_approximation, mse] = zadanie3(energy)
    % Głównym celem tej funkcji jest wyznaczenie aproksymacji rocznych danych o produkcji energii elektrycznej w wybranym kraju i z wybranego źródła energii.
    % Wybór kraju i źródła energii należy określić poprzez nadanie w tej funkcji wartości zmiennym typu string: country, source.
    % Dopuszczalne wartości tych zmiennych można sprawdzić poprzez sprawdzenie zawartości struktury energy zapisanej w pliku energy.mat.
    % 
    % energy - struktura danych wczytana z pliku energy.mat
    % country - [String] nazwa kraju
    % source  - [String] źródło energii
    % degrees - wektor zawierający cztery stopnie wielomianu dla których wyznaczono aproksymację
    % x_coarse - wartości x danych aproksymowanych; wektor o rozmiarze [N,1].
    % x_fine - wartości, w których wyznaczone zostaną wartości funkcji aproksymującej; wektor o rozmiarze [P,1].
    % y_original - dane wejściowe, czyli pomiary produkcji energii zawarte w wektorze energy.(country).(source).EnergyProduction
    % y_yearly - wektor danych rocznych (wektor kolumnowy).
    % y_approximation - tablica komórkowa przechowująca cztery wartości funkcji aproksymującej dane roczne.
    %   - y_approximation{i} stanowi aproksymację stopnia degrees(i)
    %   - y_approximation{i} stanowi wartości funkcji aproksymującej w punktach x_fine.
    % mse - wektor o rozmiarze [4,1]: mse(i) zawiera wartość błędu średniokwadratowego obliczonego dla aproksymacji stopnia degrees(i).

    country = 'Italy';%'Poland';
    source = 'Coal';%'Hydro';
    degrees = [1, 2, 3, 4];
    x_coarse = [];
    x_fine = [];
    y_original = [];
    y_yearly = [];
    y_approximation = cell(1, 4);
    mse = zeros(1, 4);

    % Sprawdzenie dostępności danych
    if isfield(energy, country) && isfield(energy.(country), source)
        % Przygotowanie danych do aproksymacji
        dates = energy.(country).(source).Dates;
        y_original = energy.(country).(source).EnergyProduction;

        n_years = floor(length(y_original) / 12);
        y_cut = y_original(end-12*n_years+1:end);
        y4sum = reshape(y_cut, [12 n_years]);
        y_yearly = sum(y4sum, 1)';

        N = length(y_yearly);
        P = 10 * N;
        x_coarse = linspace(-1, 1, N)';
        x_fine = linspace(-1, 1, P)';

        for i = 1:length(degrees)
            p = my_polyfit(x_coarse, y_yearly, degrees(i));
            y_approximation{i} = polyval(p, x_fine);
            mse(i) = calcMSE(y_yearly, polyval(p, x_coarse));
        end

        figure;

        subplot(2, 1, 1);
        plot(x_coarse, y_yearly, 'k', 'DisplayName', 'Yearly Data', 'LineWidth', 1.5); % Zmieniono z 'ko' na 'k'
        hold on;
        colors = ['r', 'g', 'b', 'm'];
        for i = 1:length(degrees)
            plot(x_fine, y_approximation{i}, colors(i), 'DisplayName', sprintf('Degree %d', degrees(i)));
        end
        hold off;
        title('Yearly Energy Production Approximation');
        xlabel('Normalized Time');
        ylabel('Yearly Energy Production');
        legend('show');
        grid on;

        subplot(2, 1, 2);
        bar(mse);
        set(gca, 'XTickLabel', degrees);
        title('Mean Squared Error for Different Polynomial Degrees');
        xlabel('Polynomial Degree');
        ylabel('Mean Squared Error');
        grid on;


        print -dpng 'zadanie3.png';

    else
        disp(['Dane dla (country=', country, ') oraz (source=', source, ') nie są dostępne.']);
    end
end

function p = my_polyfit(x, y, deg)
    V = zeros(length(x), deg + 1);
    for i = 0:deg
        V(:, i + 1) = x.^i;
    end
    
    p = (V' * V) \ (V' * y);
    p = flip(p');
    %disp(p);
    %disp(polyfit(x, y, deg));
    
end

function mse = calcMSE(y_original, y_approx)
    n = length(y_original);
    mse = sum((y_original - y_approx).^2) / n;
end
