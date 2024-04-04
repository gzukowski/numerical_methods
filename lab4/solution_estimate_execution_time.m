
a = 1;
b = 60000;
max_iterations = 100;
ytolerance = 1e-12;


[n_bisection, ysolution_bi, iterations_bi, xtab_bi, xdif_bi] = bisection_method(a, b, max_iterations, ytolerance, @estimate_execution_time);


[n_secant, ysolution_sec, iterations_sec, xtab_sec, xdif_sec] = secant_method(a, b, max_iterations, ytolerance, @estimate_execution_time);


subplot(2,1,1);
plot(1:length(xtab_bi), xtab_bi, 'b-', 'LineWidth', 2);
hold on;
plot(1:length(xtab_sec), xtab_sec, 'r-', 'LineWidth', 2);
title('Iteracje vs. Przybliżenie');
xlabel('Iteracje');
ylabel('Przybliżenie');
legend('Metoda bisekcji', 'Metoda siecznych');

subplot(2,1,2);
semilogy(1:length(xdif_bi), xdif_bi, 'b-', 'LineWidth', 2);
hold on;
semilogy(1:length(xdif_sec), xdif_sec, 'r-', 'LineWidth', 2);
title('Iteracje vs. Różnica');
xlabel('Iteracje');
ylabel('Różnica');
legend('Metoda bisekcji', 'Metoda siecznych');


function time_delta = estimate_execution_time(N)
% time_delta - różnica pomiędzy estymowanym czasem wykonania algorytmu dla zadanej wartości N a zadanym czasem M
% N - liczba parametrów wejściowych
M = 5000 ; % [s]


if N <=0
    error("error")
end

time = ( N^(16/11) + N^( (pi^2)/8 ) ) / 1000;
time_delta = time - M; 

end
function [xsolution,ysolution,iterations,xtab,xdif] = bisection_method(a,b,max_iterations,ytolerance,fun)
% a - lewa granica przedziału poszukiwań miejsca zerowego
% b - prawa granica przedziału poszukiwań miejsca zerowego
% max_iterations - maksymalna liczba iteracji działania metody bisekcji
% ytolerance - wartość abs(fun(xsolution)) powinna być mniejsza niż ytolerance
% fun - nazwa funkcji, której miejsce zerowe będzie wyznaczane
%
% xsolution - obliczone miejsce zerowe
% ysolution - wartość fun(xsolution)
% iterations - liczba iteracji wykonana w celu wyznaczenia xsolution
% xtab - wektor z kolejnymi kandydatami na miejsce zerowe, począwszy od xtab(1)= (a+b)/2
% xdiff - wektor wartości bezwzględnych z różnic pomiędzy i-tym oraz (i+1)-ym elementem wektora xtab; xdiff(1) = abs(xtab(2)-xtab(1));

xsolution = [];
ysolution = [];


xtab = [];
xdif = [];


    for iterations = 1:max_iterations
            xsolution = (a + b) / 2;
            
            
            ysolution = fun(xsolution);

             xtab(iterations) = xsolution;
    
              if iterations > 1
                xdif(iterations-1) = abs(xtab(iterations) - xtab(iterations - 1));
            end
            % sprawdzdenie znaku


            znak = ysolution * fun(a);
            if abs(ysolution) < ytolerance || abs(a - b) < ytolerance
                break;

            elseif znak < 0
                b = xsolution;
            else
                a = xsolution;
            end

           

    end



xtab = xtab';
xdif= xdif';



end

function [xsolution,ysolution,iterations,xtab,xdif] = secant_method(a,b,max_iterations,ytolerance,fun)
% a - lewa granica przedziału poszukiwań miejsca zerowego (x0=a)
% b - prawa granica przedziału poszukiwań miejsca zerowego (x1=b)
% max_iterations - maksymalna liczba iteracji działania metody siecznych
% ytolerance - wartość abs(fun(xsolution)) powinna być mniejsza niż ytolerance
% fun - nazwa funkcji, której miejsce zerowe będzie wyznaczane
%
% xsolution - obliczone miejsce zerowe
% ysolution - wartość fun(xsolution)
% iterations - liczba iteracji wykonana w celu wyznaczenia xsolution
% xtab - wektor z kolejnymi kandydatami na miejsce zerowe, począwszy od x2
% xdiff - wektor wartości bezwzględnych z różnic pomiędzy i-tym oraz (i+1)-ym elementem wektora xtab; xdiff(1) = abs(xtab(2)-xtab(1));

xsolution = [];
ysolution = [];
xdif = [];

xtab = [a, b];




    for iterations = 1:max_iterations
        
        fxk = fun(xtab(end));
        fxk_1 = fun(xtab(end-1));
        xsolution =  xtab(end) - fxk * ( xtab(end) - xtab(end-1) ) / (fxk - fxk_1);

        
        xtab = [xtab, xsolution];
        xdif = [xdif, abs(xtab(end) - xtab(end-1))];
        
        if abs(fun(xsolution)) < ytolerance
            xsolution = xsolution;
            ysolution = fun(xsolution);
            break;
        end

        

        %xtab
        
    
    
    end
xtab = xtab(3:end);
xdif = xdif(2:end);
xtab = xtab';
xdif = xdif';


end