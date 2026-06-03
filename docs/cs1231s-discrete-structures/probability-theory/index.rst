Probability Theory
==================

.. note::
    So, I was initially thinking that it wouldn't be too big of a leap to extend the CS1231S probability theory syllabus to also cover concentration bounds, turns out I was quite wrong and the page has become quite long. I have marked with asterisks (*) the sections/subsections that are out of the scope of CS1231S as of AY25/26 S1.

Probability theory is intuitively the theory of uncertainty, though interpretation of probability is in fact `subject to philosphical debates <https://en.wikipedia.org/wiki/Probability_interpretations>`_. With a number of exceptions, applications of probability theory in computer science are predominantly under the discrete context. As such, throughout our discussion we shall focus on discrete probability theory.

Sample Space and Probability
____________________________

Based on a specific random process, such as rolling a six-sided fair die, we can define a set $\Omega$, known as the sample space, consisting of every possible outcome of the random process. In our example, it is natural to define the sample space as $\{1, 2, 3, 4, 5, 6\}$, where each outcome indicates the number of dots on the upward-facing side of the (supposedly cube-shaped) die. It is imperative that there is one and only one outcome in $\Omega$ in every trial of the random process. We will henceforth assume for simplicity that the sample space is always finite.

Once a sample space $\Omega$ has been established, we can define a function $\Pr : \Omega\rightarrow [0, 1]$ which intuitively associates every outcome $s$ with a real number between $0$ and $1$, known as the probability of $s$, and denoted $\Pr[s]$. We furthermore enforce that $\Pr$ must satisfy $\sum_{s\in\Omega}\Pr[s] = 1$. Roughly speaking, the value $\Pr[s]$ indicates a quantitative chance for $s$ to be the outcome of one trial of the random process in question. A probability of $0$ indicates that the outcome is impossible, whereas a probability of $1$ indicates that the outcome is certain. In general, higher probability indicates higher chance. Continuing our example, it is natural to assign a probability of exactly $\frac{1}{6}$ to each of the $6$ outcomes.

.. note::
    It is important to note that the choice of sample space and probability assignment are essentially arbitrary, largely depending on what we are interested in studying regarding the random process. The sample space for our example could have also been $\{\text{even}, \text{odd}\}$ where each outcome indicates the parity of the number of dots on the upward-facing side of the die. It then follows that $\Pr[\text{even}] = \Pr[\text{odd}] = \frac{1}{2}$.

Event
_____

An event is a subset of the sample space. In our fair die-rolling example with $\Omega = \{1, 2, 3, 4, 5, 6\}$, we can define the event $\text{Small}\subseteq\Omega$ as the set $\{1, 2, 3\}$, to be interpreted as the event in which the outcome of a roll is small. In general, an event is a collection of outcomes with a common property.

It is common to abuse notation and denote for an event $E$ its probability $\Pr[E] := \sum_{s\in E} \Pr[s]$. We can then say that the probability that the outcome of a roll is small is $\Pr[\text{Small}] = \frac{1}{2}$. The complement of the event, i.e. the event $\overline{\text{Small}} := \Omega\setminus\text{Small}$, is the event that the outcome of a roll is large, and has probability $1 - \frac{1}{2} = \frac{1}{2}$.

In general, when probabilities are uniform, i.e. for every outcome $s$ we have $\Pr[s] = \frac{1}{| \Omega | }$, then it follows that $\Pr[E] = \frac{| E | }{| \Omega | }$, so computing $\Pr[E]$ essentially reduces to two counting problems. Otherwise, we remark that it is possible to re-define the sample space to make them uniform. For example, on an unfair die in which $\Pr[1] = \frac{1}{2}$ whereas every other outcome has equal probabilities, i.e. we have probability assignemnts $\Pr[2] = \Pr[3] = \Pr[4] = \Pr[5] = \Pr[6] = \frac{1}{10}$, we can re-define the sample space to instead be $\{1_1, 1_2, 1_3, 1_4, 1_5, 2, 3, 4, 5, 6\}$ (so there are $5$ duplicates of $1$) and assign every outcome a probability of $\frac{1}{10}$.

(*) Law of Total Probability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For any events $A$ and $B$, we have

.. math::
    \Pr[A] = \Pr[A\cap B] + \Pr[A\cap\overline{B}]

just by writing the sum $\sum_{s\in A} \Pr[s] = \sum_{s\in A\cap B}\Pr[s] + \sum_{s\in A\setminus B}\Pr[s]$. In our die-rolling example, we can say that

.. math::
    \Pr[\text{Small}] &= \Pr[\text{Small}\cap\{1, 4\}] + \Pr[\text{Small}\cap\{2, 3, 5, 6\}] \\
    &= \frac{1}{6} + \frac{2}{6} = \frac{1}{2}

More generally, for any partition $\{S_1, S_2, \cdots, S_k\}$ of the sample space, we have

.. math::
    \Pr[A] = \sum_{i = 1}^k \Pr[A\cap S_i]

This is known as the law of total probability.

(*) Union Bound
^^^^^^^^^^^^^^^

Similar to the inclusion-exclusion principle, for any events $A$ and $B$ we have

.. math::
    \Pr[A\cup B] = \Pr[A] + \Pr[B] - \Pr[A\cap B]

In our die-rolling example, note that $\Pr[\{1, 2, 3, 4\}] = \frac{2}{3}$, and indeed

.. math::
    \Pr[\{1, 2, 3, 4\}] &= \Pr[\text{Small}\cup\{1, 4\}] = \Pr[\text{Small}] + \Pr[\{1, 4\}] - \Pr[\text{Small}\cap\{1, 4\}] \\
    &= \frac{1}{2} + \frac{1}{3} - \frac{1}{6} = \frac{2}{3}

When $\Pr[A\cap B] = 0$, the events $A$ and $B$ are said to be mutually exclusive. Intuitively, this means that the two events cannot both occur, as no probable outcome lies within their intersection. In our example, the events $\text{Small}$ and $\overline{\text{Small}}$ are mutually exclusive, i.e. no outcome of a roll is small and large at the same time.

Since $\Pr[A\cap B]\geq 0$, we have $\Pr[A\cup B]\leq\Pr[A] + \Pr[B]$. Similarly, note that for any events $A, B$ and $C$, we have

.. math::
    \Pr[A\cup B\cup C] = \Pr[(A\cup B)\cup C]\leq\Pr[A\cup B] + \Pr[C]\leq\Pr[A] + \Pr[B] + \Pr[C]

In fact, we can show by induction that for any events $A_1, A_2, \cdots, A_n$, we have

.. math::
    \Pr\left[\bigcup_{i = 1}^n A_i\right]\leq\sum_{i = 1}^n \Pr[A_i]

This is what we call the union bound. In its applications in theoretical computer science, the events $A_i$ are usually bad events which we intuitively think are extremely unlikely, yet we are successful if and only if we avoid all these bad events, i.e. the success probability is $\Pr\left[\bigcap_{i = 1}^n \overline{A_i}\right]$. It follows by the De Morgan's law that the error probability is precisely $\Pr\left[\bigcup_{i = 1}^n A_i\right]$. Now, if every bad event is extremely unlikely, we can proceed to apply the union bound to bound this error probability by $\sum_{i = 1}^n \Pr[A_i]$, and hence argue intuitively that the error probability is small.

Note that since we already know that probabilities are at most $1$, for this technique to be of any use, the sum $\sum_{i = 1}^n \Pr[A_i]$ has to be strictly less than $1$, and the union bound is really only relevant when the probabilities of the bad events are extremely small.

Conditional Probability
_______________________

For any events $A$ and $B$ where $\Pr[B] > 0$, the conditional probability of $A$ given $B$, which we will denote as $\Pr[A\mid B]$, is defined as follows.

.. math::
    \Pr[A\mid B] := \frac{\Pr[A\cap B]}{\Pr[B]}

In other words, this is the value of $\Pr[A]$ when the sample space is re-defined to be $B$ instead of the original $\Omega$. Intuitively, we are conditioning on the fact that $B$ occurs, and we want to find out what is the "new" probability of $A$ based on this condition. When $\Pr[B] = 0$, it makes sense that $\Pr[A\mid B]$ is undefined, since $B$ cannot occur in the first place.

In our die-rolling example, we have $\Pr[\{1, 2\}] = \frac{1}{3}$, but $\Pr[\{1, 2\}\mid\text{Small}] = \frac{2}{3}$. Indeed, if we already know that the outcome of a roll is small, there is a higher chance that the outcome is either $1$ or $2$ relative to if we didn't have that information. Moreover, we have $\Pr[\{1, 2\}\mid\overline{\text{Small}}] = 0$ since knowing that the outcome is large, it cannot possibly be $1$ nor $2$.

Assuming $\Pr[B] > 0$, it follows that $\Pr[A\cap B] = \Pr[B]\Pr[A\mid B]$. Intuitively, for $A\cap B$ to occur, we need $B$ to occur, and we also need $A$ to occur conditioned on the fact that $B$ occurs.

Using the notion of conditional probability, the law of total probability can be rewritten as

.. math::
    \Pr[A] = \sum_{i = 1}^k\Pr[A\cap S_i] = \sum_{i = 1}^k \Pr[S_i]\Pr[A\mid S_i]

where $A$ is any event and $\{S_1, S_2, \cdots, S_k\}$ is any partition of the sample space such that all components are probable events, i.e. $\prod_{i = 1}^k\Pr[S_i] > 0$.

Bayes' Theorem
^^^^^^^^^^^^^^

If we also assume that $\Pr[A] > 0$, then we can similarly say that $\Pr[A\cap B] = \Pr[A]\Pr[B\mid A]$. Substituting this back to the definition of $\Pr[A\mid B]$ gives

.. math::
    \Pr[A\mid B] = \frac{\Pr[A]\Pr[B\mid A]}{\Pr[B]}

This result is known as Bayes' theorem, true for any events $A$ and $B$ with $\Pr[A]\Pr[B] > 0$, and a useful theorem overall by relating $\Pr[A\mid B]$ with $\Pr[B\mid A]$.

Recall in our example that $\Pr[\{1, 2\}\mid\text{Small}] = \frac{2}{3}$. It is intuitive that $\Pr[\text{Small}\mid\{1, 2\}] = 1$, since knowing that the outcome of a roll is $\{1, 2\}$, it cannot possibly be large. Indeed, by Bayes' theorem,

.. math::
    \Pr[\text{Small}\mid\{1, 2\}] = \frac{\Pr[\text{Small}]\Pr[\{1, 2\}\mid\text{Small}]}{\Pr[\{1, 2\}]} = \frac{\frac{1}{2}\cdot\frac{2}{3}}{\frac{1}{3}} = 1

Independence
____________

Two events $A, B$ with $\Pr[A]\Pr[B] > 0$ are independent if and only if $\Pr[A\mid B] = \Pr[A]$. Note that by Bayes' theorem, this also implies $\Pr[B\mid A] = \Pr[B]$. Intuitively, this means that the occurrence of $B$ does not affect the probability of $A$ occurring, and vice versa. As a result, we have

.. math::
    \Pr[A\cap B] = \Pr[A]\Pr[B\mid A] = \Pr[A]\Pr[B]

For example, consider the random process of rolling two dice. It is then natural to define the sample space as $\Omega := \{1, 2, 3, 4, 5, 6\}^2$ with every outcome having probability $\frac{1}{36}$. Let $A$ be the event that the first roll yields $3$, i.e.

.. math::
    A := \{(s_1, s_2)\in\Omega : a = 3\}

Similarly, let $B$ be the event that the second roll yields $1$. It is then intuitive that $A$ and $B$ are independent since the outcome of one roll should not affect the other. Indeed, among all the $36$ outcomes in $\Omega$, exactly $6$ of them has the first roll yielding $3$, so $\Pr[A] = \frac{1}{6}$. Similarly, we can also say that $\Pr[B] = \frac{1}{6}$. Moreover, the event $A\cap B$ is precisely the singleton $\{(3, 1)\}$. This tells us that

.. math::
    \Pr[A\mid B] = \frac{\Pr[A\cap B]}{\Pr[B]} = \frac{\frac{1}{36}}{\frac{1}{6}} = \frac{1}{6} = \Pr[A]

Now, let $C = \{(1, 1), (1, 2), (1, 3), (3, 4), (3, 5), (3, 6)\}$. Note that $A$ and $C$ are not independent. Intuitively, the event $C$ communicates that the first roll is either $1$ or $3$, and so it increases the chances of the occurrence of $A$, i.e. $\Pr[A\mid C] = \frac{3}{6}\neq\frac{1}{6} = \Pr[A]$.

.. note::
    We have $\Pr[B\mid C] = \frac{1}{6} = \Pr[B]$, so $B$ and $C$ are independent. The example above also provides a counterexample showing that independence is not transitive in general.

.. note::
    Moreover, the same example above also illustrates that the independence between two events can be broken by conditioning on a third event, i.e. it is possible that
     
    .. math::
        \Pr[A\mid B] &= \Pr[A] \\
        \Pr[A\mid B\cap C] &\neq\Pr[A\mid C]

    Indeed, knowing that the second roll yields $1$, and also $C$ has occurred, it is no longer possible for $A$ to occur, as the outcome is already deterministically $(1, 1)$. In other words, we have $\Pr[A\mid B\cap C] = 0\neq\frac{3}{6} = \Pr[A\mid C]$.

    On the other hand, two events can become independent upon conditioning on a third event, i.e. it is also possible that

    .. math::
        \Pr[A\mid B] &\neq\Pr[A] \\
        \Pr[A\mid B\cap C] &= \Pr[A\mid C]

    The simplest example would arise when $C = B$, or more generally when $C\subseteq B$. Intuitively, the occurrence of $C$ already implies the occurrence of $B$, so upon conditioning on $C$, the occurrence of $B$ no longer contributes new information that can possibly change $\Pr[A\mid C]$.

    In general, for any events $A, B, C$ with $\Pr[A]\Pr[B\cap C] > 0$, if $\Pr[A\mid B\cap C] = \Pr[A\mid C]$, we say that $A$ and $B$ are conditionally independent given $C$. In other words, conditioned on $C$, the occurrence of $B$ does not affect $\Pr[A\mid C]$.

(*) Mutual Independence
^^^^^^^^^^^^^^^^^^^^^^^

The definition of independence can be generalized to more than two events. A finite set of events, which we will denote as $\mathcal{E} = \{A_1, A_2, \cdots, A_n\}$, is mutually independent if and only if for every $i$ and every $A_i\notin S\subseteq\mathcal{E}$ we have $\Pr\left[\bigcap_{A\in S} A\right] > 0$, and moreover

.. math::
    \Pr\left[A_i\mid\bigcap_{A\in S} A\right] = \Pr[A_i]

Intuitively, for every $i$, knowing the occurrence of any collection of events other than $A_i$ does not affect the probability of $A_i$. As a corollary, we have

.. math::
    \Pr\left[\bigcap_{i = 1}^n A_i\right] = \prod_{i = 1}^n\Pr[A_i]

To prove the above rigorously, one uses induction, which we will illustrate using a three-set example. Let the events $A, B, C$ be mutually independent, then

.. math::
    \Pr[A\cap B\cap C] &= \Pr[B\cap C]\Pr[A\mid B\cap C] = \Pr[B\cap C]\Pr[A] \\
    &= \Pr[C]\Pr[B\mid C]\Pr[A] = \Pr[C]\Pr[B]\Pr[A]

Note that when $n = 2$, we recover the definition of independence between two events.

It is important to realize that mutual independence implies, but is not equivalent to, pairwise independece, i.e. for every $i\neq j$ we have $A_i$ and $A_j$ are independent. The implication is rather clear: For every $i\neq j$, we set $S := \{A_j\}$ in the definition of mutual independence to get $\Pr[A_i\mid A_j] = \Pr[A_i]$.

To see why mutual independence and pairwise independence are not equivalent, consider again our example of rolling two dice, i.e. $\Omega := \{1, 2, 3, 4, 5, 6\}^2$ with every outcome having probability $\frac{1}{36}$, and the events $A, B$ are defined as follows.

.. math::
    A &:= \{(s_1, s_2)\in\Omega : s_1 = 3\} \\
    B &:= \{(s_1, s_2)\in\Omega : s_2 = 1\} \\

Recall that $\Pr[A] = \Pr[B] = \frac{1}{6}$ and the two events are independent. Now, define

.. math::
    C := \{(s_1, s_2)\in\Omega : s_1 = s_2\}
    
to be the event that the two rolls yield the same outcome. The events $A$ and $C$ are independent because only one out of the $6$ outcomes in $C$ has the first roll yielding $3$, i.e. $\Pr[A\mid C] = \frac{1}{6} = \Pr[A]$. For similar reasons, the events $B$ and $C$ are independent.

However, the events $A, B, C$ are not mutually independent, since the occurrence of $C$ is deterministic given the occurrence of $A$ and $B$. In particular, we have

.. math::
    \Pr[C\mid A\cap B] = 0\neq\frac{1}{6} = \Pr[C]

Random Variable
_______________

A random variable is a function $X : \Omega\rightarrow\mathbb{R}$ that intuitively associates every outcome (which, mind you, is not necessarily a number) with a real number. For example, consider flipping a fair coin and receiving a payoff based on the flip outcome, e.g. we get $\$ 3$ for a head and $-\$ 1$ for a tail. It is natural to define the sample space as $\Omega := \{\text{H}, \text{T}\}$, where $\text{H}$ denotes a head and $\text{T}$ denotes a tail, with probability assignment $\Pr[\text{H}] = \Pr[\text{T}] = \frac{1}{2}$. We can then formulate this payoff mathematically as a random variable $X$ with $X(\text{H}) = 3$ and $X(\text{T}) = -1$.

We will often abuse notation and denote the event $\{s\in\Omega : X(s) = x\}$ as just $X = x$. This is the event that the random variable has observed value $x$. Similar notation applies to when we have inequalities rather than an equality. Continuing our example, we have $\Pr[X = 3] = \Pr[\text{H}] = \frac{1}{2}$.

We can combine random variables to form further random variables. For example, for any random variables $X$ and $Y$, the random variable $Z := X + Y$ is defined such that $Z(s) = X(s) + Y(s)$. Similarly, the random variable $Z := XY$ is defined such that $Z(s) = X(s)Y(s)$, and for any real number $a$ the random variable $Z := aX$ is defined such that $Z(s) = aX(s)$.

We will henceforth denote $R_X := \{x\in\mathbb{R} : X(s) = x\text{ for some }s\in\Omega\}$ as the range of the random variable $X : \Omega\rightarrow\mathbb{R}$. In our example, we have $R_X = \{3, -1\}$.

The distribution of a random variable is a function $\mu : \mathbb{R}\rightarrow [0, 1]$ that assigns for every real number $x$ the probability $\Pr[X = x]$. We write $X\sim\mu$ and say that $X$ follows the distribution $\mu$. In our example, the distribution of $X$ maps $3$ as well as $-1$ to $\frac{1}{2}$, and everything else to $0$.

(*) Indicator Random Variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Random variables are, in some sense, a generalization of events, via the notion of indicator random variables. These are specific types of random variables that is ubiquitous in the context of theoretical computer science. For any event $A$, the indicator random variable of $A$ is defined as follows.

.. math::
    \mathbf 1_A(s) = \begin{cases}
        1 & s\in A \\
        0 & \text{otherwise}
    \end{cases}

In many use cases, a complicated random variable is written as a sum of indicator random variables that are way simpler in nature. For example, consider a random distribution of $n$ distinct balls into $n$ distinct bins. Let $X$ be the number of balls in bin $1$. We can then express $X = \sum_{i = 1}^n X_i$ where $X_i$ indicates whether ball $i$ enters bin $1$, that is to say that $X_i = \mathbf 1_{A_i}$ where $A_i$ is the event that ball $i$ enters bin $1$.

One trivial observation is that for any events $A$ and $B$, we have $\mathbf 1_A\mathbf 1_B = \mathbf 1_{A\cap B}$.

(*) Independence
^^^^^^^^^^^^^^^^

The notion of independence between events extends naturally for random variables as generalizations.

Two random variables $X$ and $Y$ are said to be independent if and only if for every $x\in R_X$ and $y\in R_Y$ with $\Pr[X = x]\Pr[Y = y] > 0$, the events $X = x$ and $Y = y$ are independent, i.e.

.. math::
    \Pr[X = x\mid Y = y] = \Pr[X = x]

Intuitively, observing $Y$ does not affect the distribution of $X$. Similar to independence between events, by Bayes' theorem, this also implies $\Pr[Y = y\mid X = x] = \Pr[Y = y]$. As a result, we have

.. math::
    \Pr[X = x\cap Y = y] = \Pr[X = x]\Pr[Y = y\mid X = x] = \Pr[X = x]\Pr[Y = y]

Note that for any events $A$ and $B$, setting $X = \mathbf 1_A$ and $Y = \mathbf 1_B$ recovers the definition of independence between events.

Recall that in our coin-flipping example, we let $X$ be the payoff for the flip and we had $X(\text{H}) = 3$ as well as $X(\text{T}) = -1$. The function $X$ has domain $\Omega$. Suppose now that there are two flips, so that the sample space becomes $\Omega' := \Omega\times\Omega = \{(\text{H}, \text{H}), (\text{H}, \text{T}), (\text{T}, \text{H}), (\text{T}, \text{T})\}$ where every outcome has probability $\frac{1}{4}$. Now, let $X_1, X_2 : \Omega'\rightarrow\mathbb{R}$ be random variables such that

.. math::
    X_1(s_1, s_2) = X(s_1) \\
    X_2(s_1, s_2) = X(s_2)

For example, if the observed flip outcome is $(\text{T}, \text{H})$, then $X_1$ takes the value $X_1(\text{T}, \text{H}) = X(\text{T}) = -1$, whereas $X_2$ takes the value $3$. In other words, the random variable $X_1$ denotes the payoff for the first flip, whereas $X_2$ denotes the payoff for the second flip. The random variables $X_1$ and $X_2$ are intuitively independent, since the outcome of one flip should not affect the other.

.. note::
    Similarly, for any random variables $X, Y, Z$, we say that $X$ and $Y$ are conditionally independent given $Z$ if and only if for every $x\in R_X, y\in R_Y$ and $z\in R_Z$ with $\Pr[X = x]\Pr[Y = y\cap Z = z] > 0$, the events $X = x$ and $Y = y$ are conditionally independent given $Z = z$, i.e.

    .. math::
        \Pr[X = x\mid Y = y\cap Z = z] = \Pr[X = x\mid Z = z]
    
    In other words, given $Z$, observing $Y$ does not affect the distribution of $X$.

Readers are now encouraged to write down the definition for random variables $X_1, X_2, \cdots, X_n$ being mutually independent.

Expectation
___________

The expectation $\mathbb{E}[X]$ of a random variable $X$ is defined as follows.

.. math::
    \mathbb{E}[X] := \sum_{x\in R_X} x\cdot\Pr[X = x]

In other words, this is the mean of every possible value $X$ can take, weighted according to the probability of $X$ actually taking the value.

In our coin-flipping example with $X(\text{H}) = 3$ and $X(\text{T}) = -1$, it follows that the expectation of $X$, i.e. the expected payoff of the flip, is $\mathbb{E}[X] = \frac{1}{2}\cdot 3 + \frac{1}{2}\cdot (-1) = 1$.

The following definition of expectation is equivalent and sometimes useful. Instead of summing across every possible value $X$ can take, we sum across every outcome in the sample space.

.. math::
    \mathbb{E}[X] := \sum_{s\in\Omega} X(s)\cdot\Pr[s]

If indicator random variables correspond to events, then expectations correspond to probabilities, as for any indicator random variable $\mathbf 1_A$ we have

.. math::
    \mathbb{E}[\mathbf 1_A] = 1\cdot\Pr[\mathbf 1_A = 1] + 0\cdot\Pr[\mathbf 1_A = 0] = \Pr[A]

Linearity of Expectation
^^^^^^^^^^^^^^^^^^^^^^^^

For any random variables $X$ and $Y$, we can plug $X + Y$ into the alternative definition of expectation and get

.. math::
    \mathbb{E}[X + Y] &= \sum_{s\in\Omega} (X + Y)(s)\cdot\Pr[s] \\
    &= \sum_{s\in\Omega} (X(s) + Y(s))\cdot\Pr[s] \\
    &= \sum_{s\in\Omega} X(s)\cdot\Pr[s] + \sum_{s\in\Omega} Y(s)\cdot\Pr[s] \\
    &= \mathbb{E}[X] + \mathbb{E}[Y]

More generally, for any real numbers $a$ and $b$, plugging $aX + bY$ into the definition gives

.. math::
    \mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]
    
a result known as the linearity of expectation.

Recall that in our example of flipping two coins, we had $X(\text{H}) = 3$ as well as $X(\text{T}) = -1$, and furthermore there are two random variables $X_1$ and $X_2$ denoting the payoff for the first and second flip respectively. Note that $X$ has exactly the same distribution as $X_1$ and $X_2$ (i.e. they are all observed as $3$ with probability $\frac{1}{2}$ and $-1$ otherwise), so we can say that $\mathbb{E}[X] = \mathbb{E}[X_1] = \mathbb{E}[X_2] = 1$. It therefore follows that the expected total payoff for both flips is

.. math::
    \mathbb{E}[X_1 + X_2] = \mathbb{E}[X_1] + \mathbb{E}[X_2] = 1 + 1 = 2

(*) Conditional Expectation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to conditional probabilities, we can define a notion of conditional expectation. Let $X$ be a random variable and $A$ be an event with $\Pr[A] > 0$. The conditional expectation of $X$ given $A$, which we will denote as $\mathbb{E}[X\mid A]$, is defined as follows.

.. math::
    \mathbb{E}[X\mid A] := \sum_{x\in R_X} x\cdot\Pr[X = x\mid A]

In other words, this is the value of $\mathbb{E}[X]$ when the sample space is re-defined to be $A$ instead of the original $\Omega$. Intuitively, we are conditioning on the fact that $A$ occurs, and we want to find out what is the "new" expectation of $X$ based on this condition. When $\Pr[A] = 0$, it makes sense that $\mathbb{E}[X\mid A]$ is undefined, since $A$ cannot occur in the first place.

In our example, despite knowing that $\mathbb{E}[X_1 + X_2] = 2$, if it turns out that the first flip is a tail, i.e. we have observed that $X_1 = -1$, the expected total payoff should intuitively be reduced. Indeed, conditioned on $X_1 = -1$, since $X_2$ is either $3$ or $-1$, the sum $X_1 + X_2$ is either $-1 + 3$ or $-1 - 1$. Therefore, we have

.. math::
    &\mathbb{E}[X_1 + X_2\mid X_1 = -1] \\
    &= (-1 + 3)\cdot\Pr[X_1 + X_2 = -1 + 3\mid X_1 = -1] + (-1 - 1)\cdot\Pr[X_1 + X_2 = -1 - 1\mid X_1 = -1] \\
    &= 2\cdot\Pr[X_2 = 3] - 2\cdot\Pr[X_2 = -1] \\
    &= 2\cdot\frac{1}{2} - 2\cdot\frac{1}{2} = 0

Observe that when $X$ and $Y$ are independent random variables, for every $y\in Y$, we have

.. math::
    \mathbb{E}[X\mid Y = y] = \sum_{x\in R_X} x\cdot\Pr[X = x\mid Y = y] = \sum_{x\in R_X} x\cdot\Pr[X = x] = \mathbb{E}[X]
    
This is intuitive because observing $Y$ does not affect the distribution of $X$, and hence in particular the expectation of $X$ should remain unchanged.

With the notion of conditional expectation at hand, the law of total probability now implies

.. math::
    \mathbb{E}[X] = \sum_{x\in R_X}x\cdot\Pr[X = x] &= \sum_{x\in R_X}x\cdot\sum_{i = 1}^k\Pr[S_i]\Pr[X = x\mid S_i] \\
    &= \sum_{i = 1}^k\Pr[S_i]\sum_{x\in R_X} x\cdot\Pr[X = x\mid S_i] \\
    &= \sum_{i = 1}^k\Pr[S_i]\cdot\mathbb{E}[X\mid S_i]

where $X$ is any random variable, and $\{S_1, S_2, \cdots, S_k\}$ is any partition of the sample space such that all components are probable events.

.. note::
    Let $Y$ be a random variable and partition the sample space $\Omega$ based on the value of $Y$. This gives us

    .. math::
        \mathbb{E}[X] = \sum_{y\in R_Y}\Pr[Y = y]\cdot\mathbb{E}[X\mid Y = y] = \sum_{s\in\Omega}\Pr[s]\cdot\mathbb{E}[X\mid Y = Y(s)]

    Now, denote $\mathbb{E}[X\mid Y]$ as the random variable mapping each outcome $s$ to $\mathbb{E}[X\mid Y = Y(s)]$. It follows that

    .. math::
        \mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X\mid Y]]

    This is known as the law of total expectation and I agree that it is notationally very confusing.

(*) Variance
____________

Intuitively, the expectation of a random variable $X$ is the mean of $X$, i.e. the value that it takes on average. On the other hand, the variance of $X$ measures the dispersion, i.e. how spread out are the values of $X$ in its distribution. More precisely, the variance of a random variable $X$ is defined as follows.

.. math::
    \mathrm{Var}(X) := \mathbb{E}[(X - \mathbb{E}[X])^2]

In other words, the variance of $X$ is the expected squared distance from $X$ to its expectation. Therefore, the higher the variance of a random variable, the higher the dispersion of $X$ around its mean.

The motivation to consider the squared distance $(X - \mathbb{E}[X])^2$ instead of $| X - \mathbb{E}[X] | $ is essentially for the sake of mathematical tractability. We have a lot of algebraic tools that deals with squares of binomials, whereas it is less convenient to deal with absolute values. Indeed, denoting $\mu := \mathbb{E}[X]$, using the binomial theorem and the linearity of expectation, we have

.. math::
    \mathrm{Var}(X) &= \mathbb{E}[X^2 - 2X\mu + \mu^2] \\
    &= \mathbb{E}[X^2] - \mathbb{E}[2X\mu] + \mathbb{E}[\mu^2] \\
    &= \mathbb{E}[X^2] - 2\mu\mathbb{E}[X] + \mu^2 \\
    &= \mathbb{E}[X^2] - 2\mathbb{E}[X]^2 + \mathbb{E}[X]^2 \\
    &= \mathbb{E}[X^2] - \mathbb{E}[X]^2

giving us an alternative definition for $\mathrm{Var}(X)$. Some people memorize this formula as "the mean of squares minus the square of the mean".

For example, consider a random distribution of one ball into $n$ distinct bins with uniform probability, i.e. for every $i$ we have $\Pr[\text{the ball enters bin }i] = \frac{1}{n}$. Let $X$ be indicating whether the ball enters bin $1$. It follows that $\mathbb{E}[X] = \Pr[\text{the ball enters bin }1] = \frac{1}{n}$ and in fact $\mathbb{E}[X^2] = \mathbb{E}[X] = \frac{1}{n}$, so

.. math::
    \mathrm{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \frac{1}{n} - \frac{1}{n^2}

Recall that the linearity of expectation asserts that $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$ for any $X$ and $Y$. Unfortunately, we note that it is very much possible that $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$. This is already evident from the alternative definition of $\mathrm{Var}(X)$. Indeed, if $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ in general, then just by setting $X = Y$ we have $\mathrm{Var}(X) = 0$ for any $X$, a statement more than easy to disprove.

Covariance
^^^^^^^^^^

The covariance between $X$ and $Y$ is defined as follows.

.. math::
    \mathrm{Cov}(X, Y) := \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]

where the second equality follows from a similar and slightly generalized calculation as the one used to derive $\mathrm{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2$. It follows that for every random variables $X$ and $Y$ we have the equalities $\mathrm{Cov}(X, X) = \mathrm{Var}(X)$ and $\mathrm{Cov}(X, Y) = \mathrm{Cov}(Y, X)$.

For specific $x\in R_X$ and $y\in R_Y$, if $(x - \mathbb{E}[X])(y - \mathbb{E}[Y]) > 0$, then $x$ and $y$ lie on the same side of the mean. Similarly, if $(x - \mathbb{E}[X])(y - \mathbb{E}[Y]) < 0$, then $x$ and $y$ lie on opposite sides of the mean. By taking the expectation over all $x$ and $y$, the covariance can intuitively reveal the direction and degree of dependency between $X$ and $Y$. When $X$ and $Y$ are strongly dependent, the magnitude of $\mathrm{Cov}(X, Y)$ should be large, and vice versa.

For example, consider distributing $n$ distinct balls into $n$ distinct bins independently and uniformly at random, i.e. for every $i, j$ we have $\Pr[\text{ball }i\text{ enters bin }j] = \frac{1}{n}$. Moreover, for every $i'\neq i$ and every $j'$ the events $\text{ball }i'\text{ enters bin }j'$ and $\text{ball }i\text{ enters bin }j$ are independent. Let $X_i$ be indicating whether bin $i$ is empty, then observe that

.. math::
    \mathbb{E}[X_i] = \Pr[\text{bin }i\text{ is empty}] = \left(1 - \frac{1}{n}\right)^n

since every ball has to avoid entering bin $i$. Similarly, the random variable $X_iX_j$ indicates the event that bin $i$ and $j$ are both empty, so when $i\neq j$, we have $\mathbb{E}[X_iX_j] = \left(1 - \frac{2}{n}\right)^n$. It follows that

.. math::
    \mathrm{Cov}(X_i, X_j) = \mathbb{E}[X_iX_j] - \mathbb{E}[X_i]\mathbb{E}[X_j] = \left(1 - \frac{2}{n}\right)^n - \left(1 - \frac{1}{n}\right)^{2n}

Intuitively, knowing that bin $j$ is empty reduces the chances for bin $i$ to be empty, since the balls have to avoid bin $j$ and thus have less bins to go to. Indeed, we see that

.. math::
    1 - \frac{2}{n}\leq 1 - \frac{2}{n} + \frac{1}{n^2} = \left(1 - \frac{1}{n}\right)^2 &\implies\left(1 - \frac{2}{n}\right)^n\leq\left(1 - \frac{1}{n}\right)^{2n} \\
    &\implies\mathrm{Cov}(X_i, X_j)\leq 0

This agrees with the fact that the values of $X_i$ and $X_j$ tend to move in opposite directions.

It is therefore reasonable for us to conjecture that if $X$ and $Y$ are independent, then $\mathrm{Cov}(X, Y) = 0$, i.e. $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$. This can be proven via a manipulation of sums.

.. math::
    \mathbb{E}[XY] &= \sum_{z\in R_{XY}} z\cdot\Pr[XY = z] \\
    &= \sum_{x\in R_X}\sum_{y\in R_Y} xy\cdot\Pr[X = x\cap Y = y] \\
    &= \sum_{x\in R_X}\sum_{y\in R_Y} xy\cdot\Pr[X = x]\Pr[Y = y] \\
    &= \left(\sum_{x\in R_X} x\cdot\Pr[X = x]\right)\left(\sum_{y\in R_Y} y\cdot\Pr[Y = y]\right) \\
    &= \mathbb{E}[X]\mathbb{E}[Y]

It is important to note that the converse is not necessarily true, i.e. there exist dependent $X$ and $Y$ such that $\mathrm{Cov}(X, Y) = 0$. For example, let $X$ be uniformly distributed over $\{-1, 0, 1\}$. In other words, we have $\Pr[X = -1] = \Pr[X = 0] = \Pr[X = 1] = \frac{1}{3}$. Moreover, let $Y = X^2$. Note that $X$ and $Y$ are certainly dependent, since for example observing $Y = 0$ makes $X$ deterministic. Note that $XY = X^3$ is still uniformly distributed over $\{-1, 0, 1\}$ and hence $\mathbb{E}[XY] = \mathbb{E}[X] = 0$, so $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.

Moreover, observe that

.. math::
    \mathrm{Var}(X + Y) &= \mathbb{E}[(X + Y)^2] - \mathbb{E}[X + Y]^2 \\
    &= \mathbb{E}[X^2 + 2XY + Y^2] - (\mathbb{E}[X] + \mathbb{E}[Y])^2 \\
    &= \mathbb{E}[X^2] + 2\mathbb{E}[XY] + \mathbb{E}[Y^2] - \mathbb{E}[X]^2 - 2\mathbb{E}[X]\mathbb{E}[Y] - \mathbb{E}[Y]^2 \\
    &= (\mathbb{E}[X^2] - \mathbb{E}[X]^2) + (\mathbb{E}[Y^2] - \mathbb{E}[Y]^2) + 2(\mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]) \\
    &= \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\mathrm{Cov}(X, Y)

and so unlike expectation, in general there is no "linearity of variance" unless $X$ and $Y$ are independent. One can imagine that a more generalized calculation shows that

.. math::
    \mathrm{Var}\left(\sum_{i = 1}^n X_i\right) = \sum_{i = 1}^n\mathrm{Var}(X_i) + 2\sum_{i < j}\mathrm{Cov}(X_i, X_j) = \sum_{i, j}\mathrm{Cov}(X_i, X_j)

and in particular if $X_1, X_2, \cdots, X_n$ are pairwise independent, then $\mathrm{Var}\left(\sum_{i = 1}^n X_i\right) = \sum_{i = 1}^n\mathrm{Var}(X_i)$.

(*) Concentration Bounds
________________________

A very major application of probability theory in theoretical computer science is on establishing concentration bounds. Intuitively, a random variable is concentrated around its mean if it is very unlikely that it deviates too much from its mean. Say we need to design an algorithm that estimates some property of the input data (e.g. the input data is the binary string, and we want to estimate the number of $1$s in the string). If we can show that our algorithm output $\hat{X}$ satisfies $\mathbb{E}[\hat{X}] = X$ where $X$ is the true value, then establishing a concentration bound on $\hat{X}$ provides a theoretical guarantee that our algorithm produces a good estimate with high probability.

In this section, we will see three main tools for establishing such concentration bounds.

Markov's Inequality
^^^^^^^^^^^^^^^^^^^

Let $X$ be a non-negative random variable, i.e. for every $x\in R_X$ we have $x\geq 0$. Moreover, let $\alpha > 0$. By partitioning the sample space into whether $X\leq\alpha\mathbb{E}[X]$, we have

.. math::
    \mathbb{E}[X] = \Pr[X\leq\alpha\mathbb{E}[X]]\cdot\mathbb{E}[X\mid X\leq\alpha\mathbb{E}[X]] + \Pr[X > \alpha\mathbb{E}[X]]\cdot\mathbb{E}[X\mid X > \alpha\mathbb{E}[X]]

Recall that probabilities are non-negative. Since $X$ is non-negative, we have $\mathbb{E}[X\mid X\leq\alpha\mathbb{E}[X]]\geq 0$ in particular. It follows that we can drop the first term and be no larger, i.e.

.. math::
    \mathbb{E}[X]\geq\Pr[X > \alpha\mathbb{E}[X]]\cdot\mathbb{E}[X\mid X > \alpha\mathbb{E}[X]]

Intuitively, given $X > \alpha\mathbb{E}[X]$, the mean of $X$ must always be strictly larger than $\alpha\mathbb{E}[X]$ as well, so

.. math::
    \mathbb{E}[X] > \Pr[X > \alpha\mathbb{E}[X]]\cdot\alpha\mathbb{E}[X]\implies\Pr[X > \alpha\mathbb{E}[X]] < \frac{1}{\alpha}

This is known as Markov's inequality.

In our balls into bins example, let $Y_i$ be indicating whether ball $i$ enters bin $1$, so that the total number of balls in bin $1$ is $Y := \sum_{i = 1}^n Y_i$. Note that $\mathbb{E}[Y_i] = \Pr[\text{ball }i\text{ enters bin }1] = \frac{1}{n}$, and so by the linearity of expectation we have

.. math::
    \mathbb{E}[Y] = \sum_{i = 1}^n\mathbb{E}[Y_i] = 1

By Markov's inequality, for any $\alpha\geq 0$ we have $\Pr[Y > \alpha] < \frac{1}{\alpha}$. The more balls we want to enter bin $1$, there is a less chance that we will be happy.

Chebyshev's Inequality
^^^^^^^^^^^^^^^^^^^^^^

For any random variable $X$, note that $(X - \mathbb{E}[X])^2$ is a non-negative random variable. Therefore, by Markov's inequality, for any $\alpha\geq 0$ we have

.. math::
    &\Pr[(X - \mathbb{E}[X])^2 > \alpha^2\mathbb{E}[(X - \mathbb{E}[X])^2]] < \frac{1}{\alpha^2} \\
    &\implies\Pr[(X - \mathbb{E}[X])^2 > \alpha^2\mathrm{Var}(X)] < \frac{1}{\alpha^2} \\
    &\implies\Pr\left[| X - \mathbb{E}[X] | > \alpha\sqrt{\mathrm{Var}(X)}\right] < \frac{1}{\alpha^2}

This is known as Chebyshev's inequality. Via a change of variables, we can equivalently state the inequality as

.. math::
    \Pr\left[| X - \mathbb{E}[X] | > \alpha\right] < \frac{\mathrm{Var}(X)}{\alpha^2}

Recall that in our balls into bins example, we let $X_i$ be indicating whether bin $i$ is empty, for every $i\neq j$ we had $\mathbb{E}[X_i] = \left(1 - \frac{1}{n}\right)^n$ and $\mathrm{Cov}(X_i, X_j)\leq 0$. We can moreover calculate that

.. math::
    \mathrm{Var}(X_i) = \left(1 - \frac{1}{n}\right)^n - \left(1 - \frac{1}{n}\right)^{2n}
    
Now let $X := \sum_{i = 1}^n X_i$ be the total number of empty bins. We show that $\Pr[| X - \mathbb{E}[X] | > \alpha n]$ is small for every $\alpha\geq 0$ using Chebyshev's inequality. To do so, we first need to compute $\mathrm{Var}(X)$.

.. math::
    \mathrm{Var}(X) &= \sum_{i = 1}^n\mathrm{Var}(X_i) + 2\sum_{i < j}\mathrm{Cov}(X_i, X_j)\leq\sum_{i = 1}^n\mathrm{Var}(X_i) \\
    &= n\left(\left(1 - \frac{1}{n}\right)^n - \left(1 - \frac{1}{n}\right)^{2n}\right)

To simplify notations, denote $a := \left(1 - \frac{1}{n}\right)^n$, so that $\mathrm{Var}(X) = na(1 - a)$. Since $0\leq a\leq 1$, it follows that $a(1 - a)\leq\frac{1}{4}$, and so $\mathrm{Var}(X)\leq\frac{n}{4}$. Applying Chebyshev's inequality, for any $\alpha\geq 0$, we have

.. math::
    \Pr\left[| X - \mathbb{E}[X] | > \alpha n\right] < \frac{\mathrm{Var}(X)}{\alpha^2n^2}\leq\frac{n}{4\alpha^2n^2} = \frac{1}{4\alpha^2n}

so intuitively it is extremely unlikely that there are a lot more empty bins than expected, so much so that the probability is upper-bounded by a value that tends to $0$ as $n$ tends to infinity. The number of empty bins is really concentrated around its expectation.

Chebyshev's inequality is especially applicable when $X$ can be written as a sum $X = \sum_{i = 1}^n X_i$ for pairwise independent random variables $X_1, X_2, \cdots, X_n$. Since $\mathrm{Var}(X) = \sum_{i = 1}^n\mathrm{Var}(X_i)$, there is no need to worry about covariances, and the calculation of $\mathrm{Var}(X_i)$ should be simpler than that the calculation of $\mathrm{Var}(X)$ given that each $X_i$ is an indicator random variable.

In our balls into bins example, recall that $Y_i$ indicates whether ball $i$ enters bin $1$, and we had $\mathbb{E}[Y] = 1$ where $Y$ is the number of balls in bin $1$. Since $Y_1, Y_2, \cdots, Y_n$ are pairwise independent, it is easy to apply Chebyshev's inequality to establish a concentration bound on $Y$. In particular, we will aim to show that $\Pr[| Y - \mathbb{E}[Y] | \geq\alpha\mathbb{E}[Y]] = \Pr[| Y - \mathbb{E}[Y] | \geq\alpha]$ is small. First, note that

.. math::
    \mathrm{Var}(Y_i) &= \frac{1}{n} - \frac{1}{n^2} \\
    \implies\mathrm{Var}(Y) &= \sum_{i = 1}^n\mathrm{Var}(Y_i) = 1 - \frac{1}{n} < 1

and so by Chebyshev's inequality, for any $\alpha\geq 0$, we have

.. math::
    \Pr\left[| Y - \mathbb{E}[Y] | > \alpha\right] < \frac{\mathrm{Var}(Y)}{\alpha^2} < \frac{1}{\alpha^2}

so again, it is extremely unlikely that there are a lot more (or a lot less) balls in bin $1$ than expected.

Note that $Y_1, Y_2, \cdots, Y_n$ are not only pairwise independent, but also mutually independent and identically distributed indicator random variables. This specific structure allows us to establish even stronger concentration bounds on $Y$ via the following tool.

Chernoff Bounds
^^^^^^^^^^^^^^^

Let $X := \sum_{i = 1}^n X_i$ where $X_1, X_2, \cdots, X_n$ are mutually independent and identically distributed (often abbreviated i.i.d.) random variables whose ranges are a subset of $[0, 1]$. Moreover, denote $\mu := \mathbb{E}[X]$. The Chernoff bounds assert the following for any $\delta\geq 0$.

.. math::
    \Pr[X\geq (1 + \delta)\mu]\leq\left(\frac{e^\delta}{(1 + \delta)^{1 + \delta}}\right)^\mu

Due to the complicated expression on the right hand side, the following looser upper bound is typically more helpful.

.. math::
    \Pr[X\geq (1 + \delta)\mu]\leq e^{-\frac{\delta^2\mu}{2 + \delta}}

Moreover, for any $0\leq\delta < 1$, we have

.. math::
    \Pr[X\leq (1 - \delta)\mu]\leq\left(\frac{e^{-\delta}}{(1 - \delta)^{1 - \delta}}\right)^\mu

A looser bound but more helpful bound asserts that for any $0\leq\delta\leq 1$, we have

.. math::
    \Pr[| X - \mu | \geq\delta\mu]\leq 2e^{-\frac{\delta^2\mu}{3}}

Lastly, it is also helpful that for any $\delta > 1$, we have

.. math::
    \Pr[X\geq (1 + \delta)\mu]\leq e^{-\frac{\delta\mu}{3}}

As we can see, the Chernoff bounds are not one inequality, but a family of inequalities helpful in various situations, and they all establish upper bounds that are exponential with respect to the expectation. We will not prove the Chernoff bounds here, but essentially it involves an application of Markov's inequality (much like the proof of Chebyshev's inequality) to arrive at the moment generating function of $X$, which can in turn be further bounded using the i.i.d. assumption to arrive at the Chernoff bounds.

In our balls into bins example, we will establish a much sharper concentration bound on $Y$, i.e. the number of balls in bin $1$ using the Chernoff bound that asserts that for any $0\leq\alpha\leq 1$, we have

.. math::
    \Pr[| Y - \mu | \geq\alpha\mu]\leq 2e^{-\frac{\alpha^2\mu}{3}}

where $\mu := \mathbb{E}[Y] = 1$. This gives us

.. math::
    \Pr[| Y - \mathbb{E}[Y] | \geq\alpha]\leq 2e^{-\frac{\alpha^2}{3}}

This is a much sharper bound compared to $\frac{1}{\alpha^2}$, in the sense that the dependence on $\alpha$ is now exponential rather than polynomial.

.. note::
    While we're at it, let us also recall the union bound. Say there are now $\lceil 10n\ln n\rceil$ balls to be distributed into $n$ bins, and we are considered successful if and only if no bin is empty. We can therefore define the bad events $A_i$ as the event that bin $i$ is empty, and we are successful if and only if we avoid all these bad events. In other words, the error probability is
    
    .. math::
        \Pr\left[\bigcup_{i = 1}^n A_i\right]\leq\sum_{i = 1}^n\Pr[A_i]

    where the inequality is the application of the union bound. Since there are now $\lceil 10n\ln n\rceil$ balls, for every $i$ we have
    
    .. math::
        \Pr[A_i] &= \left(1 - \frac{1}{n}\right)^{\lceil 10n\ln n\rceil}\leq\left(1 - \frac{1}{n}\right)^{10n\ln n} \\
        &\leq e^{-\frac{1}{n}\cdot 10n\ln n} = \frac{1}{n^{10}}
        
    where the second inequality uses the fact that $1 + x\leq e^x$ for all $x$, as can be proven via the Taylor expansion of $e^x$. It then follows from the union bound that the error probability is

    .. math::
        \Pr\left[\bigcup_{i = 1}^n A_i\right]\leq n\cdot\frac{1}{n^{10}} = \frac{1}{n^9}

    so intuitively it is extremely unlikely that we make an error.
