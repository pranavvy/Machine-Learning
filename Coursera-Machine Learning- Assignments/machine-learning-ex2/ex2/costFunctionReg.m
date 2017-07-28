function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

n = size(X,2);

h = sigmoid(X*theta);
J = ((-y)' * log(h) - (1-y)' * log(1-h))/m;

theta1 = [0 ; theta(2:size(theta), :)];

%regularization
soma = 0
for j=1:n,
   soma = soma + (theta1(j) * theta1(j));
end;

%penalty
p = (lambda*soma) / (2*m);

%J plus penalty
J = J + p;

%regularized gradientDescent
grad = (X' * (h-y) + lambda*theta1) / m;

% =============================================================

end
