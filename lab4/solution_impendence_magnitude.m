
a = 1;
b = 50;
ytolerance = 1e-12;
max_iterations = 100;
%R = 75;

[omega_bisection, ysolution_bi, iterations_bi, xtab_bi, xdif_bi] = bisection_method(a, b, max_iterations, ytolerance, @impedance_magnitude);


[omega_secant, ysolution_sec, iterations_sec, xtab_sec, xdif_sec] = secant_method(a, b, max_iterations, ytolerance, @impedance_magnitude);




subplot(2,1,1);
plot(1:length(xtab_bi), xtab_bi, 'b-', 'LineWidth', 2);
hold on;
plot(1:length(xtab_sec), xtab_sec, 'r-', 'LineWidth', 2);
title('iteracje vs. zmiana przybliżenia');
xlabel('iteracje');
ylabel('czestosc');
legend('Bisection Method', 'Secant Method');



subplot(2,1,2);
semilogy(1:length(xdif_bi), xdif_bi, 'b-', 'LineWidth', 2);
hold on;
semilogy(1:length(xdif_sec), xdif_sec, 'r-', 'LineWidth', 2);
title('Iteracje vs różnice');
xlabel('iteracje');
ylabel('różnice');
legend('Bisection Method', 'Secant Method');






