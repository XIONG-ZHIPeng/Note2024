# Fundamental Mathematics

**Content**

> - Differential equations and physics
> - Array and vector
> - Vector analysis
> - Complex function theory
> - Fourier transform
> - Laplace transform


## Differential equation


***Linear differential equation***

: Differential equation defined by **linear polynomial** in the unknown function and its derivatives

- y^\'^ + ay = 0 `{ a is constant , eq.1.1}`
  - If  y~(x)~ satisfy above, y~(x)~ is called as **solution**
  - Solve above equation to obtain y~(x)~
  - Before that, y is called as **unknown function**

- Mission: solve function y^\'^ + ay = 0 `{ a is constant , eq.1.1}`
  - Use nature of exponential function
    - (e^ax^)^\'^ = ae^ax^
  - Multiple e^ax^ to `{eq.1.1: y^\'^ + ay = 0}`
    - e^ax^y^\'^ + ae^ax^y = 0
  - Recall the differential for products
    - (g~(x)~h~(x)~)^'^ = g~(x)~h~(x)~^'^ + g~(x)~^'^h~(x)~
  - `{eq.1.1: y^\'^ + ay = 0}` should be
    - (e^ax^y)^'^ = 0 &rarr; e^ax^y = c `{c is arbitrary constant}`
    - Solution w/o constant: **a general solution**
    - If c has some specific value &rarr; **a particular solution**
- Shape of function depends arbitrary constant `{Initial value problem}`
  - We may don’t know the arbitrary constant itself
  - We may know the value(𝑦~0~) on specific point(𝑥~0~)
    - 𝑦~0~ : Initial value or initial condition
    - y^\'^ + ay = 0, $𝑦_0 = y(x_0) = ce^{-ax_0}$
      - $c = y_0 e^{ax_0}$
  - General form of `{eq.1.1: y^\'^ + ay = 0}` should be
    - $y = y_0 e^{-a(x-x_0)}$

***Homogeneous differential***

- Think about following equation
  - $ y^{'} + ay = r_{(x)} $ `{eq.1.7}`
  - A differential equation is **homogeneous** when
    - $f_{(x,y)}dy = -g{(x,y)}dx$ &rarr; $f_{(x,y)} + g_{(x,y)}\frac{dx}{dy} = 0 $
    - If r~(x)~ = 0, `{eq.1.7 }` is homogeneous
  - If not, a differential equation is **inhomogeneous**
    - If $r_{(x)} \neq 0$ , `{eq.1.7}` is inhomogeneous
  - A general solution of inhomogeneous function `{eq.1.7}` is
    - $y = (\int r_{(x)}e^{ax}dx + c)e^{-ax}$
    - Multiple e^ax^ to `{eq.1.7}`
      - $(y^{'} + ay) e^{ax} = r_{(x)}e^{ax}$ &rarr; $(ye^{ax})^{'} = r_{x}e^{ax}$
    - Take integral
      - $ ye^{ax} = \int r_{(x)}e^{(ax)}dx +c$ `{c is constant}`
      - $y = (\int r_{(x)}e^{(ax)}dx +c)e^{-ax}$
    - ![](example1.png)

***Quiz***

- Solve a general form of following equations
  - $y^{'} - y = 0$
        $a = -1, y = ce^x $ `{c is arbitrary constatn}`
  - $y^{'} + y = 0$
        $a = 1, y = ce^{-x} $ `{c is arbitrary constatn}`

- Solve a initial value problem of following equations 
    $c = y_0 e^{ax_0}, y = y_0 e^{-a(x-x_0)}$

  - $y^{'} + y = 0, y_{(0)} = 2$
        $a = 1, y = ce^{-x} $ 
        $c = 2, y = 2e^{-x}$
  - $y^{'} - 2y = 0, y_{(1)} = 2$
        $a = -2, y = ce^{2x} $ 
        $c = \frac{2}{e^2}, y = 2e^{2(x-1)}$

- Generalize
    - ![](general1.png)
    - ![](general2.png)

**Solution of differential equation**

- Constant coefficient 1st order differential equation
  - Homogeneous: $y^{'} + ay = 0 \leftrightarrow y = ce^{-ax}$ `{c is constant}`
  - Inhomogeneous:
    - $ y^{'} + ay =r_{(x)} \leftrightarrow y = (\int r_{(x)}e^{ax}dx +c)e^{-ax}$
  - Variable coefficient 1st order differential equation
    - Homogeneous: $y^{'} + f_{(x)}y = 0 \leftrightarrow y = ce^{-F_{(x)}}$
    - Inhomogeneous: $y^{'} + f_{(x)}y = r_{(x)} \leftrightarrow y = (\int r_{(x)}e^{F_{(x)}}dx +c)e^{-F_{(x)}}$

> - Variation of constants
> - Method of indeterminate coefficient

***Variation of constants***

: Can solve linear (inhomogeneous) differential equation
  - Difficulty to solve high order equation
  - Equation becomes complex for high order equation

- Strategy
  1. Change given inhomogeneous equation to homogeneous
  2. Solve general solution for the homogeneous equation
  3. Replace constant 𝑐 to function 𝑢(𝑥)
  4. Substitute 𝑢(𝑥) to given inhomogeneous equation
        - Calculate general solution of 𝑢(𝑥)
  5. Substitute 𝑢(𝑥) to solution of homogeneous equation

- Example: get general solution of :  $ y^{'} + f_{(x)}y = r_{(x)}$ `{eq.1.7}`
    1. Change given inhomogeneous equation to homogeneous
        - $ y^{'} + f_{(x)}y = 0 $
    2. Solve general solution for the homogeneous equation
        - Use this relationship: $(e^{F(x)})^{'} = e^{F_{(x)}}F^{'}_{(x)} = e^{F_{(x)}}f_{(x)}$
        - $e^{F_{(x)}}y^{'} + e^{F_{(x)}} f_{(x)}y = e^{F(x)}y^{'} + e^{F_{(x)}}(e^{F(x)})^{'}y=0$
        - thus, $(e^{F(x)}y)^{'} = 0 \rightarrow e^{F(x)}y = c$ `{c is constant}`
    3. Replace constant 𝑐 to function 𝑢(𝑥)
        - $y = ce^{-F(x)} \rightarrow y = u_{(x)}e^{-F(x)} \rightarrow u_{(x)} = ye^{+F(x)}$
    4. Substitute 𝑢(𝑥) to given inhomogeneous equation
        - $(u_{(x)}e^{-F(x)})^{'} + f_{(x)}u_{(x)}e^{-F(x)} = r_{(x)}$
        - $ u^{'}_{(x)}e^{-F(x)} - f_{(x)}u_{(x)}e^{-F(x)} + f_{(x)}u_{(x)}e^{-F(x)} = r_{(x)}$
        - $ u^{'}_{(x)} = r_{(x)}e^{F(x)} \rightarrow u_{(x)} = \int r_{(x)}e^{F_{(x)}}dx + C$`{c is constant}`
    5. Substitute 𝑢(𝑥) to solution of homogeneous equation
        - $y = u_{(x)}e^{-F(x)}= (\int r_{(x)}e^{F_{(x)}}dx + C)e^{-F(x)}$

***Method of indeterminate coefficient***

: With some assumptions, we can easily solve differential equation
: Guess the candidate of particular solution
: If the right side of an equation is
    - n-order polynormal: candidate should be n-polynormal
    - sine function: candidate should be in sine
    - exponential: candidate should be in exponential

- Example1: get general solution of: $y^{'}+3y = x^{2} -1$ `{eq.1.23}`
  - Assume particular solution is $ y_p = \alpha x^2 + \beta x + \gamma $
    - $\alpha, \beta, \gamma $ are constant. Substitute $y_p$ to `{eq.1.23}`
    - $y^{'}_p + 3y_p = (2 \alpha x + \beta) + 3(\alpha x^2 + \beta x + \gamma) = x^2 -1$
    - This equation should satisfy following conditions
      - $x^2 : 2\alpha = 1, x : 2\alpha + 3 \beta = 0, x^0: \beta + 3 \gamma = -1 $, thus
    - $y_p = \frac{1}{3} x^2 - \frac{2}{9} x - \frac{7}{27}$


  - If one particular solution is clear, general solution can be easily solved.
  - Example: get general solution of : $y^{'} + f_{(x)}y = r_{(x)}$
    - Assume particular solution 𝑦~𝑝~, general solution 𝑦, and its difference $y_h = y - y_p$ is
    -  $y^{'}_h + f_{(x)}y_h = (y-y_p)^{'} + f_{(x)}(y-y_p) = y^{'} + f_{(x)}y-(y^{'}_{p}+f_{(x)}y_p) = r_{(x)} - r_{(x)} = 0$ 
    -  This is homogeneous:$y_h = ce^{-F_{(x)}}$
    -  $\mathbf{y = y_p + y_h = y_p + ce^{-F_{(x)}}}$ `{c is constant}`
       -  we can use this as theorem
    -  general solution of `{eq.1.23}`:$y = \frac{1}{3} x^2 - \frac{2}{9} x - \frac{7}{27} + ce^{-3x}$

- Example2: get general solution of :$ y^{'} + 2y = \cos(x)$`{eq.1.25}`
  - Assume particular solution is $y_p = \alpha \cos x + \beta \sin x$
    - $\alpha , \beta$ are constant. Substitute y~p~ to `{eq.1.25}`
    - $y^{'}_p + 2y_p = - \alpha \sin x + \beta \cos x + 2(\alpha \cos c + \beta \sin x) = \cos x$
    - This equation should satisfy following conditions
    - $\cos x : 2\alpha + \beta = 1, \sin x : - \alpha + 2 \beta = 0$, thus
  - $y_p = \frac{2}{5} \cos x + \frac{1}{5} \sin x$
  - $y = \frac{2}{5} \cos x + \frac{1}{5} \sin x + ce^{-2x}$

- Example3: get general solution of : $y^{'} - y = 2e^{2x}$ `{eq.1.28}`
  - Assume particular solution is $y_p = \alpha e^{2x}$
    - &alpha; is constant. Substitute y~p~ to `{eq.1.28}`
    - $y^{'}_p - y_p = 2 \alpha e^{2x} - \alpha e^{2x} = \alpha e^{2x} = 2 e^{2x}$, thus
    -  $y_p = 2e^{2x}$
    -  $y = 2e^{2x} + ce^{x}$
    -  However, this is not true for all of solution
 -  Example: get general solution of : $y^{'} - 2y = 2e^{2x}$ `{eq.1.29}`
    -  Assume particular solution is $y_p = \alpha e^{2x}$
       -  &alpha; is constant. Substitute y~p~ to `{eq.1.29}`
       -  $y^{'}_p - y_p = 2\alpha e^{2x} - 2\alpha e^{2x} = 0 \rightarrow $ wrong  assumption
    -  Assume particular solution is $y_p = \alpha xe^{2x}$
       -  &alpha; is constant. Substitute y~p~ to `{eq.1.29}`
       -  $y^{'}_p - y_p = (\alpha e^{2x} + 2\alpha x e^{2x}) - 2\alpha x e^{2x} = 2e^{2x}$
       -  $y_p = 2xe^{2x}$
       -  $ y = (2x + c) e^{2x}$
    -  If general solution is $\mathbf{y^{'} + ay = ke^{-ax}}$, particular solution should be $y_p = kxe^{-ax}$
 -  **Exerceis(1)**
    -  Solve general solutions for following equations
       -  by Variation of constants method
          -  $y^{'} - xy = x$
                1. $f_{(x)} = -x, F_{(x)} = -\frac{1}{2}x^2, r_{(x)} = x $
                2. $u_{(x)} = \int r_{(x)}e^{F_{(x)}}dx + c, \\ y = u_{(x)} e^{-F_{(x)}} = (\int x e^{-\frac{1}{2}x^2}dx + c_1)e^{\frac{1}{2}x^2} = -1 + c_2 e^{\frac{x}{2}}$ 
                - `{c1, c2 is constant}`
          -  $y^{'} + \frac{y}{x} = x^2 +2x$

                1. $f_{(x)} = \frac{1}{x}, F_{(x)} = \ln x , \\ r_{(x)} = x^2 +2x$
                2. $y = \frac{\int (x^2 + 2x)xdx +c_1}{x} = \frac{x^3}{4} + \frac{2x^2}{3} + \frac{c_2}{x}$
       -  by Method of indeterminate coefficient
          -  $2y^{'} + 3y = 3x^2 + x$
               - Assuming the particular solution: $y_p = \alpha x^2 + \beta x + \gamma$
               - Substitute: $2(2\alpha x + \beta ) + 3(\alpha x^2 + \beta x + \gamma) = 3x^2 + x \\ 3\alpha =3, 4\alpha + 3\beta = 1, 2\beta + 3\gamma = 0 \\ \alpha =1, \beta = -1, \gamma = \frac{2}{3}$
               - $f_{(x)} = \frac{3}{2}, F_{(x)} = \frac{3}{2}x$
               - particular solution: $ y_p = x^2 -x + \frac{2}{3}$
               - general solution: $y_p = x^2 -x + \frac{2}{3} + ce^{-\frac{3}{2}x}$ `{c: const}`
          -  $y^{'} + 4y = 3e^{-x}$
             -  $y_p = \alpha e^{-x}$
             -  $ - \alpha e^{-x} + 4\alpha e^{-x} = 3 e^{-x}, \alpha = 1$
             -  $f_{(x)} = 4 , F_{(x)} = 4x$
             -  $y_p = e^{-x}, y = e^{-x} + ce^{-4x}$

***Euler's formula***
- The trigonometric functions (sin cos) and complex exponential function satisfy following relationship
  - $e^{ix} = \cos x + i\sin x$
  - 𝑒: base of natural logarithm, 𝑖(or 𝑗): imaginary unit
- Euler’s formula is useful for circuit analysis, cause
  - Easy to take integral, differential
    - $\frac{d}{dx}e^{\lambda x} = \lambda e^{\lambda x}, \int e^{\lambda x}dx = \frac{1}{\lambda}e^{\lambda x } + c$ `{c: constant}`
    - Phasor: expression of sine func. in complex exponent
      - $A\cos wx = \Re{A \cos wx + i A\sin wx}$
      - Calculate circuit in complex exponent, then convert to original sine functions

***2nd order differential equation***
- Introduce 2nd order differential equation
  - $y^{''} + a y^{'} + by = r_{(x)}$`{a, b are constants, eq.3.1}`
    - If $r_{(x)} = 0$, `{eq.3.1}` is homogeneous
    - If $r_{(x)} \neq 0$, `{eq.3.1}` is inhomogeneous
- Inhomogeneous form is very tough for hand calculation
  - If 𝑟(𝑥) is constant, sine, or exponential we can use method of indeterminate coefficient
    -  In physics, circuits, we can use this assumption

***Characteristic equation***
- If $r_{(x)} = 0 \text{ and } y_{(x)} = ce^{\lambda x}$ (c, &lambda; : constant), `eq.3.1` is
  - $y^{''} + ay^{'} + by = (\lambda ^2 + a\lambda + b)ce^{\lambda x} = 0 , ce^{\lambda x} \neq 0$ thus
    - $\lambda ^2 + a\lambda + b = 0 : \text{ characteristic equation}$
  - Solution and $ \lambda = \frac{-a \pm \sqrt{a^2 -4b}}{2}$ changes depend on discriminant function $(a^2 -4b)$
    - $a^2 -4b > 0: \lambda _1, \lambda _2 $ in real. Solutions: $c_1e^{\lambda x}, c_2e^{\lambda x}$
    - $a^2 -4b = 0: \lambda = -\frac{a}{2}$. Solutions: $c_1e^{\lambda x}, c_2xe^{\lambda x}$ 
    - $a^2 -4b < 0: \lambda _1, \lambda _2$ in imaginary value.
      - $\lambda _1 = \alpha + i\beta, \lambda _2 = \alpha - i\beta$
      - Solutions: $c_1e^{\lambda x}, c_2e^{\lambda x}$

***Linearity of solution***
- Use linearity  of solution
- Theorem: if y~(x)~ and w~(x)~ are the solution of linear equation `{eq.3.1}`, sum $c_1y_{(x)} + c_2w_{(x)}$ is also the solution
- Proof: since y~(x)~ and w~(x)~ are the solution, it should satisfy
  - $y^{''} + ay^{'} + by = 0, w^{''} + aw^{'} + bw = 0,$
  - Multiply const c~1~ and c~2~ and get its sum
    - $c_1y^{''} + c_1ay^{'} + c_1by + c_2w^{''} + c_2aw^{'} + c_2bw = 0 $
  - $(c_1y+c_2w)^{''} + a(c_1y+c_2w)^{'}+b(c_1y+c_2w) = 0$
  - So, $c_1y_{(x)} + c_2w_{(x)}$ is also the solution
- Solution is the sum of exponents, comes from
characteristic equation

***General solution***
- Theorem: General solution of 2nd order homogeneous differential equation is
  - $a^2 - 4b = 0: y_{(x)} = c_1e^{\lambda _1 x} + c_2xe^{\lambda _1 x}, \lambda_1 \text{: multiple root of char. eq}$ 
  - $a^2 - 4b \neq 0: y_{(x)} = c_1e^{\lambda _1 x} + c_2e^{\lambda _2 x}, \lambda_1, \lambda_2 \text{: roots of char. eq}$
- Proof: if 𝑦(𝑥) is the solution of `{eq.3.1}`, multiply 𝑒^−𝜆𝑥^
  - $e^{-\lambda x}y^{''} + e^{-\lambda x}ay^{'} + e^{-\lambda x}by = 0$
  - $(e^{-\lambda x}y)^{''} + (a + 2\lambda)(e^{-\lambda x}y)^{'} + (\lambda ^2 + a\lambda +b)e^{-\lambda x}y = 0$
    - If we assume 𝜆1 is root of char. eq., $\lambda_1 ^2 + a\lambda_1 +b = 0$, thus
    - $(e^{-\lambda x}y)^{''} + (a + 2\lambda)(e^{-\lambda x}y)^{'} = 0$
  - $u^{''} + (a+2\lambda_1)u^{'} = 0$, when $e^{-\lambda x}y_{(x)} = u_{(x)}$
    - Case $a^2 - 4b =0 : \lambda = -\frac{a}{2}, \text{thus} u^{''} = 0$
      - $u(x) = c_1 + c_2 x, \text{ thus } y_{(x)} = c_1e_{\lambda_1 x} + c_2xe^{\lambda_1 x}$
      - Case $a^2 - 4b \neq 0:$
        - $v^{'} + (a + 2\lambda_1)v = 0, \text{when} v = u^{'}, $ solve this then
        - $v = Ce^{-(a+2\lambda_1)x}$, C is constant. Then integrate this 
          - $u_{(x)} = c_1 - \frac{C}{a+2\lambda_1}e^{-(a+2\lambda_1)x}$, thus
          - $y = c_1e^{\lambda_1 x} - c_2e^{\lambda_2x}$, since (a + &lambda;~1~) si the solution &lambda;~2~. $(c_2 = \frac{C}{a+2\lambda_1}, \lambda_2 = a + \lambda_1)$
  - Transform from/to sine to/from exponent
    - Case $(a^2 - 4b < 0):$
    - $y_{(x)} = c_1e^{(A+iB)x} + c_2e^{(A-iB)x}$
    - $y_{(x)} = c_1e^{Ax}(\cos Bx + i\sin Bx) + c_2e^{Ax}(\cos Bx - i\sin Bx)$
      - $= (c_1 + c_2) e^{Ax}\cos Bx + i(c_1 - c_2)e^{Ax}\sin Bx$
      - $= d_1e^{Ax}\cos Bx + d_2 e^{Ax}\sin Bx$

***Exercise(2)***

- Solve characteristic equation and general solutions for following equations
  - by Method of indeterminate coefficient
    - $y^{''} + 2y^{'} + y = 0$
      - since r~(x)~ = 0, assume $y = ce^{\lambda x}. c, \lambda :$ unknown 
      - $(\lambda ^2 + 2\lambda +1)ce^{\lambda x} = 0$
      - characteristic. eq $\lambda ^2 + 2\lambda + 1 = 0 \rightarrow \lambda = -1$
      - general solution: $y = c_1e^{-x} + c_2 xe^{-x}$
    - $y^{''} + 2y^{'} + 3y = 0$
      - since r~(x)~ = 0, assume $y = ce^{\lambda x}. c, \lambda :$ unknown 
      - $(\lambda ^2 + 2\lambda +3)ce^{\lambda x} = 0$
      - characteristic. eq $\lambda ^2 + 2\lambda + 3 = 0 \rightarrow \lambda = -1 \pm \sqrt{2}i$
      - general solution: $y = c_1e^{-(1+\sqrt{2}i)x} + c_2e^{-(1-\sqrt{2}i)x}$
    - $y^{''} - 4y^{'} - 5y = 0$
      - characteristic. eq $\lambda ^2 - 4\lambda - 5 = 0 \rightarrow \lambda = -1, 5$
      - general solution: $y = c_1e^{5x} +c_2e^{-x}$`{c1, c2: constant}` 

***2nd order differential equation***
- Introduce 2nd order differential equation
  - $y^{''} + ay^{'} + by = r_{(x)}$ (a, b are constants)`{eq.2.12}`
    - If r(x) = 0, `{eq.2.12}` is homogeneous `{eq.2.2}`
    - If r(x) &ne; 0, `{eq.2.12}` is inhomogeneous `
- Inhomogeneous form is very tough for hand calculation
  - If 𝑟(𝑥) is constant, sine, or exponential we can use **method of indeterminate coefficient**
  - Variation of constants
  - Method of indeterminate coefficient

***Structure of solution for inhomogeneous equation***

