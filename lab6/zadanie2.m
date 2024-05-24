function [country, source, degrees, y_original, y_movmean, y_approximation, mse] = zadanie2(energy)
    % Głównym celem tej funkcji jest wyznaczenie aproksymacji wygładzonych danych o produkcji energii elektrycznej w wybranym kraju i z wybranego źródła energii.
    % Wygładzenie danych wykonane jest poprzez wywołanie funkcji movmean.
    % Wybór kraju i źródła energii należy określić poprzez nadanie w tej funkcji wartości zmiennym typu string: country, source.
    % Dopuszczalne wartości tych zmiennych można sprawdzić poprzez sprawdzenie zawartości struktury energy zapisanej w pliku energy.mat.
    % 
    % energy - struktura danych wczytana z pliku energy.mat
    % country - [String] nazwa kraju
    % source  - [String] źródło energii
    % degrees - wektor zawierający cztery stopnie wielomianu dla których wyznaczono aproksymację
    % y_original - dane wejściowe, czyli pomiary produkcji energii zawarte w wektorze energy.(country).(source).EnergyProduction
    % y_movmean - średnia 12-miesięczna danych wejściowych, y_movmean = movmean(y_original,[11,0]);
    % y_approximation - tablica komórkowa przechowująca cztery wartości funkcji aproksymującej wygładzone dane wejściowe. y_approximation stanowi aproksymację stopnia degrees(i).
    % mse - wektor o rozmiarze 4x1: mse(i) zawiera wartość błędu średniokwadratowego obliczonego dla aproksymacji stopnia degrees(i).

    country = 'Poland';
    source = 'Hydro';
    degrees = [1, 3, 5, 13];
    y_original = [];
    y_movmean = [];
    y_approximation = cell(1, 4);
    mse = zeros(1, 4);

    % Sprawdzenie dostępności danych
    if isfield(energy, country) && isfield(energy.(country), source)
        % Przygotowanie danych do aproksymacji
        dates = energy.(country).(source).Dates;
        y_original = energy.(country).(source).EnergyProduction;
        y_movmean = movmean(y_original, [11, 0]);

        x = linspace(-1, 1, length(y_original))';

        for i = 1:length(degrees)
            p = polyfit(x, y_movmean, degrees(i));
            y_approximation{i} = polyval(p, x);
            mse(i) = calcMSE(y_movmean, y_approximation{i});
        end

        figure;
        subplot(2, 1, 1);
        plot(dates, y_original, 'k', 'DisplayName', 'Wzorcowa', 'LineWidth', 1.5);
        hold on;
        plot(dates, y_movmean, 'b', 'DisplayName', 'wygładzone', 'LineWidth', 1.5);
        colors = ['r', 'g', 'm', 'c'];
        for i = 1:length(degrees)
            plot(dates, y_approximation{i}, colors(i), 'DisplayName', sprintf('stopień %d', degrees(i)));
        end
        hold off;
        title('Aproksymacja z wygładzeniem ');
        xlabel('data');
        ylabel('Produkcja energii');
        legend('show');
        grid on;

        subplot(2, 1, 2);
        bar(mse);
        set(gca, 'XTickLabel', degrees);
        title('Błąd średniokwadratowy');
        xlabel('Stopień');
        ylabel('Średni błąd');
        grid on;

        print -dpng 'zadanie2.png';

    else
        disp(['Dane dla (country=', country, ') oraz (source=', source, ') nie są dostępne.']);
    end
end

function mse = calcMSE(y_original, y_approx)
    n = length(y_original);
    mse = sum((y_original - y_approx).^2) / n;
end
