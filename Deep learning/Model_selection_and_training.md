# Model selection (choosing a model)

![alt text]({EF2CA840-2C8D-497C-8A79-7CBEE2D4AA9D}.png)
you can choose a model in d = [1,10], use $J_{\text text}(w^{<d>}, b^{<d>})$
see which one give you the lost values. seen you find that J tests for the fifth-order polynomial for W5, B5
, turns out to be the lowest 

**The Problem**:$J_{\text text}(w^{<d>}, b^{<d>})$ is likely to be an **optimistic estimate** of generalization error. Because an extra parameter **d** (degree of polynomial) was chosen using the test set.

w, b are overly optimistic estimate of generalization erroe on training data
**(如果只看d的话只能说明d在这份数据上泛化能力可以而已)**

to solve this problem, we split this data into **three** different subsets , which we're going to call the **training set**, the **cross-validation(交叉验证集)** set and then also the test.

ps: cross validation = validation(验证集) = development set(开发集) = dev set
![alt text]({A3F040BC-96DB-44C2-A548-203E51841957}.png)

# Diagnosing bias and variance

![alt text]({C1E1BDF4-999D-4D01-8F1E-A29A7AFED94E}.png)
![alt text]({3B410CEB-719D-4EFE-B5EB-3DA3CD34557E}.png)

High bias (underfit)
-> $J_{train}$ will be high ($J_{train} \approx J_{cv}$)

High variance(overfit)
-> $J_{cv} >> J_{train}$($J_{train}$ may be low)

High bias and high variance J_{train} will be high and $J_{cv} >> J_{train}$

# Regularization and bias/variance

Model : $f_{\vec w, b}(x) = w_1x + w_2x^2 + w_3x^3 + w_4x^4 + b$
$J(\vec w, b) = \frac{1}{2m}\sum_{i = 1}^{m}(f_{\vec w,b}(\vec x^{(i)}) - y^{(i)})^2 + \frac{\lambda}{2m}\sum_{j=1}^{n}w_j^2$

let start with the example of setting lambda to be very large value, say lambda is equal to **10,000**
![alt text]({1529ECCC-AAFE-4DE4-BF89-003FC7389E3B}.png)
^ High bias
![alt text]({C7E7136B-5E89-4A6B-BBF4-7B0BA5D2F7DA}.png)
^ High variance

![alt text]({C5869C4D-F15C-40A7-BE46-7912B1ED4E01}.png)

## Bias and variance a function of regularization parameter $\lambda$

![alt text]({C037AFF9-9CB8-4FC2-BE9F-F3360CBB4F29}.png)

#
这块就用中文简单说明一下，简单来说使用一个基准值来评估模型是很重要的，（比如声音数据在人类的表现中也会有很大的噪音数据这就会导致人类也会有比较高的偏差）
![alt text]({50D3F22E-6A4B-4B98-A449-0FF3BDEBD5CA}.png)
![alt text]({0F4FE53A-FD38-4E58-87F8-B692C1DC6205}.png)
上图就能看出来哪些是具有高偏差的数据