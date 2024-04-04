function velocity_delta = rocket_velocity(t)
% velocity_delta - różnica pomiędzy prędkością rakiety w czasie t oraz zadaną prędkością M
% t - czas od rozpoczęcia lotu rakiety dla którego ma być wyznaczona prędkość rakiety
M = 750; % [m/s]
mO = 150000;
u = 2000;


g = 1.622;
q = 2700;

if t <=0 
    erorr("Error")
end




velocity_delta = u * log( mO / ( mO - q*t ) ) - g*t;


velocity_delta = velocity_delta - M;
end
