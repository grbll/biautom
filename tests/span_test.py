from biautom.misc.span import restricted_span

a = (1,0)
b = (0,2)

print(restricted_span(4,3,{a,b}, {(0,0)}))
