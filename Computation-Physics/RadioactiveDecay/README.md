# Problem Setup
## Understanding the difference between analytical and numerical modeling using eulers method.
First we solve for  Δ𝑁𝐴 . Given the expression

𝑑𝑁𝐴𝑑𝑡=−𝑁𝐴(𝑡)𝜏𝐴 

⇒Δ𝑁𝐴=−𝑁𝐴(𝑡)𝜏𝐴Δ𝑡 

We also know that

Δ𝑁𝐴=𝑁𝐴(𝑡+Δ𝑡)−𝑁𝐴(𝑡) 

⇒𝑁𝐴(𝑡+Δ𝑡)=𝑁𝐴(𝑡)+Δ𝑁𝐴 

Pluggin in  Δ𝑁𝐴  gives:

𝑁𝐴(𝑡+Δ𝑡)=𝑁𝐴(𝑡)−𝑁𝐴(𝑡)𝜏𝐴Δ𝑡 

This is enough to solve the expression.


First lets set some constants:

We are using Euler's method so at every given  𝑁𝐴(𝑡)  we will have a corresponding slope. The shorter the time intervals are when propogating forward with these slopes the more accurate the estimation. That being said, we have to choose how long these intervals are and how many times we want to step forward using this chosen value. We can do something a bit simpler by just stating some overall time and dividing that by the time intervals to get a number of iterations. To our benefit,  𝜏𝐴  is known and we simply pick a value to call it.

Working in units of  𝜏𝐴 .



First we solve for  Δ𝑁𝐵 . Given the expression

𝑑𝑁𝐵𝑑𝑡=𝑁𝐴𝜏𝐴−𝑁𝐵(𝑡)𝜏𝐵 

⇒Δ𝑁𝐵=𝑁𝐴(𝑡)𝜏𝐴Δ𝑡−𝑁𝐵(𝑡)𝜏𝐵Δ𝑡 

We also know that

Δ𝑁𝐵=𝑁𝐵(𝑡+Δ𝑡)−𝑁𝐵(𝑡) 

⇒𝑁𝐵(𝑡+Δ𝑡)=𝑁𝐵(𝑡)+Δ𝑁𝐵 

Pluggin in  Δ𝑁𝐴  gives:

𝑁𝐵(𝑡+Δ𝑡)=𝑁𝐵(𝑡)(1−Δ𝑡𝜏𝐵)+𝑁𝐴(𝑡)𝜏𝐴Δ𝑡 

This is enough to solve the expression.


---
## In collaboration with my dear colleague Josh Spradlin
