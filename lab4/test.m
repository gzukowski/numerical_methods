
%omega = 0
%impedance_delta = impedance_magnitude(omega)

%impedance_delta


a = 1; 
b = 50;
max_iterations = 100;
ytolerance = 1e-12;

[xsolution,ysolution,iterations,xtab,xdif] = bisection_method(a,b,max_iterations,ytolerance,@impedance_magnitude)

disp(size(xdif))