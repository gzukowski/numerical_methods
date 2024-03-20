function plot_direct(N,vtime_direct)
   % N - wektor zawierający rozmiary macierzy dla których zmierzono czas obliczeń metody bezpośredniej
    % vtime_direct - czas obliczeń metody bezpośredniej dla kolejnych wartości N


    figure;
    plot(N, vtime_direct, 'bo', 'MarkerSize', 2);
    xlabel('Rozmiar'); 
    ylabel('czas w sekundach'); 
    title('czas vs rozmiar');
    grid on;
    legend('bezposrednie');

    print -dpng zadanie2.png 
end
