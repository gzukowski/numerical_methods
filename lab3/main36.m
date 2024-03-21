
load('filtr_dielektryczny.mat', 'A', 'b');
N = 20000;

%[M,bm,x,err_norm,time,iterations,index_number] = mikrofala_jacobi(N, A, b);
%[M,bm,x,err_norm,time,iterations,index_number] = mikrofala_gaus(N, A, b);
[x, time, err_norm,index_number] = mikrofala_direct(N, A, b);

disp(time);
disp(err_norm);
disp(iterations);