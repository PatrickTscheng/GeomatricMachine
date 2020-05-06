x=table2array(resultsim(:,1));
yy=table2array(resultsim(:,2));

% [population2,gof] = fit(x,y,'poly2');
% plot(population2,x,y);
% legend('Location','NorthWest');

pick = int64([1:5:150]);
tau = x(pick);
y = yy(pick);
% 
% dl = tau(2) - tau(1);
% dr = tau(end) - tau(end-1);
% t = [tau(1)-dl*[2 1] tau tau(end)+dr*[1 2]];  % construct the knot sequence
% plot(tau,y,'ro');
% hold on
% axis(frame+[-2*dl 2*dr 0 0])
% plot(t,repmat(frame(3)+.03,size(t)),'kx')
% hold off
% legend({'Data Values' 'Knots'},'location','NW')
% 
% sp = spapi(t,tau,y);
% 
% plot(tau,y,'ro')
% axis(frame)
% hold on
% fnplt(sp,[tau(1) tau(end)], 'k')
% hold off
% 
% fnplt(sp,'k');
% hold on
% plot(tau,y,'ro', t,repmat(.1,size(t)),'kx');
% hold off
% legend({'Spline Interpolant' 'Data Values' 'Knots'},'location','NW')

plot(tau,y)
