clear; close all;

% Make some "data" at random points x,y points
N=200;
x = (rand(N,1)-0.5)*6;
y = (rand(N,1)-0.5)*6;
z = cos((x.^2+y.^2)/2);

% Create an interpolating function named F
F = TriScatteredInterp(x,y,z,'natural');

% Create an evenly spaced grid to interpolate onto
xe = -3:.1:3;
ye = xe;
[XE,YE] = ndgrid(xe,ye);

% Evaluate the interpolation function on the even grid
ZE = F(XE,YE);

% plot the interpolated surface
surf(XE,YE,ZE);

% overlay the "data" as dots
hold on;
plot3(x,y,z,'.');
axis equal
