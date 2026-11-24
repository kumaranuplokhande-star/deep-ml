def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    import numpy as np
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    if len(a)==len(b):
        s=np.array(a)+np.array(b)
        s_l=s.tolist()
        return s_l
    else:
        return -1

    