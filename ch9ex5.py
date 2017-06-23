clear; close all;

f=@(x) exp(-x).*cos(x)

integral(f,0,2,'AbsTol',1e-8)
