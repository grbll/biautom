def restricted_span(x_restriction: int,  y_restriction: int, generators: set[tuple[int,int]], generated: set[tuple[int, int]]):
    new_generated: set[tuple[int,int]] = set(())
    new_generated.update(generated)
    for vector_1 in generators:
        for vector_2 in generated:
            vector: tuple[int, int] = (vector_1[0] + vector_2[0], vector_1[1] + vector_2[1])
            if vector[0]<=x_restriction and vector[1]<=y_restriction:
                new_generated.add(vector)
    if generated != new_generated:
        return restricted_span(x_restriction, y_restriction, generators, new_generated)
    else:
        return new_generated
