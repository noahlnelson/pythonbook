clear; close all;

f = @(x,y) cos(x.*y);

integral2(f,0,2,0,2,'AbsTol',1e-10)
