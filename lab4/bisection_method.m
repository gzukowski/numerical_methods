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