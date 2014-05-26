function [ out ] = convert1a( in )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
m = mean(in);
s = std(in);
cols = size(in,2);
out = zeros(size(in));
for i=1:cols
    out(:,i) = (in(:,i) - m(i))/s(i);
end

end

