# Regularized linear Regression
$\min J(\vec w,b) = \min [\frac{1}{2m}\sum_{i=1}^{m}(f_{\vec w,b}(\vec {x}^{(i)})-y^{(i)})^2 + \frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2]$

$\begin{cases}
w=w-\alpha\frac{d}{dw}J(\vec{w},b) \\
b=b-\alpha\frac{d}{db}J(\vec{w},b)
\end{cases}$

$\begin{cases}
w = \frac{1}{m}\sum_{i=1}^{m}(f_{\vec w,b}(\vec x^{(i)})-y^{(i)})x_j^{(i)} +\frac {\lambda}{m}w_j \\
b = \frac{1}{m}\sum_{i=1}^{m}(f_{\vec w,b}(\vec x^{(i)})-y^{(i)})
\end{cases}$