# Gradient descent

$J(\vec w,b)=-\frac{1}{m}\sum_{i=1}^{m}[y^{(i)}\log(f_{\overline{w},b}(\vec{x}^{(i)}))+(1-y^{(i)})\log(1-f_{\overline{w},b}(\vec{x}^{(i)}))]$

repeat { 
    $\begin{cases}
w_j=w_j-\alpha\frac{d}{dw_j}J(\vec w,b) \\
b=b-\alpha\frac{d}{db}J(\vec w,b)
\end{cases}$
} simultaneous updates

Same concepts:
- Monitor gradient descent(learning curve)
- Vectorized implementation
- Feature scaling