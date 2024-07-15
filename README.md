# Newton-Raphson Method for Finding Roots

This Python script implements the Newton-Raphson Method for finding the roots of a given function. The Newton-Raphson Method is an iterative numerical technique used to find the root of a function, i.e., the point where the function evaluates to zero.

## Description

The Newton-Raphson Method requires an initial approximation for the root, and it iteratively refines this approximation using the formula:

\[ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \]

The iterations continue until the difference between successive approximations is less than a specified tolerance (`tol`) or a maximum number of iterations (`max_iter`) is reached.

## Parameters

- `f`: The function whose root we want to find.
- `df`: The derivative of the function `f`.
- `x0`: The initial approximation.
- `tol`: The acceptable error tolerance (default is `1e-5`).
- `max_iter`: The maximum number of iterations (default is `100`).

## Returns

- The approximate root of the function if found within the specified tolerance and iteration limit.
- `None` if the root is not found or if the derivative is zero during the iterations.

## Usage

To use the `newton_method` function, define the function `f` and its derivative `df` whose root you want to find and call `newton_method` with an appropriate initial approximation:

```python
def newton_method(f, df, x0, tol=1e-5, max_iter=100):
    """
    Implementation of the Newton-Raphson Method for finding roots of a function.

    :param f: The function whose root we want to find.
    :param df: The derivative of the function f.
    :param x0: The initial approximation.
    :param tol: The acceptable error tolerance.
    :param max_iter: The maximum number of iterations.
    :return: The approximate root.
    """
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        
        if dfx == 0:
            print("Derivative is zero, stopping execution.")
            return None

        x1 = x0 - fx / dfx
        
        if abs(x1 - x0) < tol:
            print(f"Root found after {i+1} iterations: x = {x1}")
            return x1
        
        x0 = x1

    print(f"Root not found after {max_iter} iterations.")
    return None

# Example usage
def f(x):
    return x**2 - 4

def df(x):
    return 2 * x

root = newton_method(f, df, x0=2)
print("Approximate root:", root)
