
options = optimset('Display','iter');


[x1,~,~,output1] = fzero(@tan, 6.0, options);


[x2,~,~,output2] = fzero(@tan, 4.5, options);

% Zapisanie wyników do pliku zadanie9.txt
fid = fopen('zadanie9.txt', 'w');
fprintf(fid, '6.0:\n');
fprintf(fid, 'x1 = %.15f\n', x1);
fprintf(fid, 'Szczegóły działania funkcji fzero:\n');
fprintf(fid, '%s\n\n', output1.message);

fprintf(fid, '4.5:\n');
fprintf(fid, 'x2 = %.15f\n', x2);
fprintf(fid, 'Szczegóły działania funkcji fzero:\n');
fprintf(fid, '%s\n\n', output2.message);

fclose(fid);
