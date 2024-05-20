function [country, source, degrees, x_coarse, x_fine, y_original, y_yearly, y_approximation, mse, msek] = zadanie4(energy)
% Głównym celem tej funkcji jest wyznaczenie danych na potrzeby analizy dokładności aproksymacji wielomianowej.
% 
% energy - struktura danych wczytana z pliku energy.mat
% country - [String] nazwa kraju
% source  - [String] źródło energii
% x_coarse - wartości x danych aproksymowanych
% x_fine - wartości, w których wyznaczone zostaną wartości funkcji aproksymującej
% y_original - dane wejściowe, czyli pomiary produkcji energii zawarte w wektorze energy.(country).(source).EnergyProduction
% y_yearly - wektor danych rocznych
% y_approximation - tablica komórkowa przechowująca wartości nmax funkcji aproksymujących dane roczne.
%   - nmax = length(y_yearly)-1
%   - y_approximation{1,i} stanowi aproksymację stopnia i
%   - y_approximation{1,i} stanowi wartości funkcji aproksymującej w punktach x_fine
% mse - wektor mający nmax wierszy: mse(i) zawiera wartość błędu średniokwadratowego obliczonego dla aproksymacji stopnia i.
%   - mse liczony jest dla aproksymacji wyznaczonej dla wektora x_coarse
% msek - wektor mający (nmax-1) wierszy: msek zawiera wartości błędów różnicowych zdefiniowanych w treści zadania 4
%   - msek(i) porównuj aproksymacje wyznaczone dla i-tego oraz (i+1) stopnia wielomianu
%   - msek liczony jest dla aproksymacji wyznaczonych dla wektora x_fine

country = 'Poland';
source = 'Hydro';
degrees = [1, 3, 5, 8];
x_coarse = [];
x_fine = [];
y_original = [];
y_yearly = [];
y_approximation = []
mse = [];
msek = [];

% Sprawdzenie dostępności danych
if isfield(energy, country) && isfield(energy.(country), source)
        % Przygotowanie danych do aproksymacji
        dates = energy.(country).(source).Dates;
        y_original = energy.(country).(source).EnergyProduction;
    
        % Obliczenie danych rocznych
        n_years = floor(length(y_original) / 12);
        y_cut = y_original(end-12*n_years+1:end);
        y4sum = reshape(y_cut, [12 n_years]);
        y_yearly = sum(y4sum,1)';
    
        N = length(y_yearly);
        P = (N-1)*10+1;
        x_coarse = linspace(-1, 1, N)';
        x_fine = linspace(-1, 1, P)';
        
    
        mse = zeros(N-1, 1);
        msek = zeros(N-2, 1);
        % Pętla po wielomianach różnych stopni
        y_approximation = cell(1, N-1);
    
        for i = 1:N-1
            p = my_polyfit(x_coarse, y_yearly, i);
            y_approximation{i} = polyval(p, x_fine);
            y_approx_coarse = polyval(p, x_coarse);
            mse(i) = calcMSE(y_yearly, y_approx_coarse);
        end

        for i = 1:N-2
            msek(i) = calcMSE(y_approximation{i}, y_approximation{i+1});
        end

        figure;

        subplot(3, 1, 1);
        plot(x_coarse, y_yearly, 'k', 'DisplayName', 'Yearly Data', 'LineWidth', 1.5);
        hold on;
        colors = ['r', 'g', 'b', 'm'];
        for i = 1:length(degrees)
            plot(x_fine, y_approximation{degrees(i)}, colors(i), 'DisplayName', sprintf('Degree %d', degrees(i)));
        end
        hold off;
        title('Yearly Energy Production Approximation');
        xlabel('Normalized Time');
        ylabel('Yearly Energy Production');
        legend('show');
        grid on;

        subplot(3, 1, 2);
        semilogy(1:N-1, mse, '-');
        title('Mean Squared Error for Different Polynomial Degrees');
        xlabel('Polynomial Degree');
        ylabel('Mean Squared Error');
        grid on;

        subplot(3, 1, 3);
        semilogy(1:N-2, msek, '-');
        title('Convergence of Polynomial Approximations');
        xlabel('Polynomial Degree');
        ylabel('Difference Error');
        grid on;

        print -dpng 'zadanie4.png';

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
