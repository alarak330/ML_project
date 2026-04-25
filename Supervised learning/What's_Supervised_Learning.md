# What's Supervised Learning?

***X***(input) -> ***Y***(output label)

The key characteristic of supervised learning is that you give you give your learning algorithm **examples to learn from that include the right answer**, where by right answer I mean the correct label ***Y*** for a given input ***X***.

And it's by seeing correct pairs of input ***X*** and desired output label ***Y*** that the learning algorithm eventually **learns to take just the input alone without the output label**

Input (X) | Output (Y) | Application|
|---|---|---|
email|spam?(0/1)|spam filter
audio|text transcripts|speech recognition|
English|Spanish|machine translation
ad, user info|click?(0/1)|online advertising

Learns from being given **right_answer**
***Regression***| ***Classification***
|---|---|
|predict a **number**|predict **categories**|
|**infinitely** many possible outputs|**small number** of possible outputs|