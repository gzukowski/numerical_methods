function [lake_volume, x, y, z, zmin] = zadanie5()
    % Funkcja zadanie5 wyznacza objętość jeziora metodą Monte Carlo.
    %
    %   lake_volume - objętość jeziora wyznaczona metodą Monte Carlo
    %
    %   x - wektor wierszowy, który zawiera współrzędne x wszystkich punktów
    %       wylosowanych w tej funkcji w celu wyznaczenia obliczanej całki.
    %
    %   y - wektor wierszowy, który zawiera współrzędne y wszystkich punktów
    %       wylosowanych w tej funkcji w celu wyznaczenia obliczanej całki.
    %
    %   z - wektor wierszowy, który zawiera współrzędne z wszystkich punktów
    %       wylosowanych w tej funkcji w celu wyznaczenia obliczanej całki.
    %
    %   zmin - minimalna dopuszczalna wartość współrzędnej z losowanych punktów
    N = 1e6;
    zmin = -100 + (rand * 55);
    x = 100*rand(1,N); % [m]
    y = 100*rand(1,N); % [m]
    z = zmin * rand(1,N); % [m]

    xmax = 100;
    ymax = 100;
    lake_volume = [];
    accepted_points = 0;

    for i = 1:N
        if z(i) >= get_lake_depth(x(i), y(i))
            accepted_points = accepted_points + 1;
        end
    end
    V = xmax * ymax * abs(zmin);
    lake_volume = V * accepted_points / N;
    disp(lake_volume);
end