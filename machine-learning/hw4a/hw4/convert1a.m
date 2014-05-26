function out = convert1a(in)


me = mean(in);
st = std(in);
cols = size(in,2);
out = zeros(size(in));
for i=1:cols
    out(:,i) = (in(:,i) - me(i))/st(i);
end

end

