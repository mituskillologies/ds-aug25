def largest(a: int, b: int) -> str:
    """
    takes two integers to compare and finds the largest

    Parameters
    __________
                a: int
                    the first integer
                b: int
                    the second integer

    Returns
    ________
                int:
                    largest value between 'a' and 'b'
                    
    """

    
    if a > b:
        print(f"largest is {a}")
    elif a == b:
        print("equal")
    else:
        print(f" largest is {b} ")