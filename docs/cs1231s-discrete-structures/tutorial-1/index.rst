Tutorial 1
==========

While application of logic appears to be intuitive, the study of logic itself can get quite philosophical at times, having been developed from the movement of `analytic philosophy <https://en.wikipedia.org/wiki/Analytic_philosophy>`_.

Statements and Statement Variables
__________________________________

A *statement* is a sentence that is either true or false.

.. note:: You can then ask "how do we define a sentence?" or even "what is a definition?" and these would be valid questions, though we won't bother answering them. For the purpose of mathematics, anything that you think is a sentence is a sentence, and it is reasonable to assume that this will not cause any ambiguity in a thousand years.

A *variable* is a symbol used to represent an object. For example, a *statement variable* is a symbol that represents a statement. We could define $p$ to be the statement "I did not go to Universal Studios Singapore" and henceforth $p$ would be a statement variable. Sometimes they are used as shorthands for actual statements, other times they are necessary to represent a general statement.

Logical Connectives
___________________

A *logical connective* is a symbol used in between statements to form new statements. Such statements are known as *compound statements*.

A *propositional statement*, or a *proposition*, is a statement formed using statement variables and logical connectives.

We will introduce three logical connectives: $\wedge$, $\vee$, and $\sim$. Let $p$ and $q$ be statement variables.

* $p\wedge q$ is known as the *conjunction* of $p$ and $q$, read "$p$ and $q$".
* $p\vee q$ is known as the *disjunction* of $p$ and $q$, read "$p$ or $q$".
* $\sim p$ (also $\neg~p$) is known as the *negation* of $p$, read "not $p$".

Each logical connective is defined using a truth table, which exhaustively lists down the truth of the resulting proposition for every possible combination of truth values of $p$ and $q$ (or just $p$ for negation). Below, $T$ denotes true and $F$ denotes false.

.. container:: tables

  .. container:: center-table

    .. list-table:: $p\wedge q$ is always false unless both $p$ and $q$ are true.
      :widths: 33 33 34
      :header-rows: 1

      * - $p$
        - $q$
        - $p\wedge q$
      * - $T$
        - $T$
        - $T$
      * - $T$
        - $F$
        - $F$
      * - $F$
        - $T$
        - $F$
      * - $F$
        - $F$
        - $F$

  .. container:: center-table

    .. list-table:: $p\vee q$ is always true unless both $p$ and $q$ are false.
      :widths: 33 33 34
      :header-rows: 1

      * - $p$
        - $q$
        - $p\vee q$
      * - $T$
        - $T$
        - $T$
      * - $T$
        - $F$
        - $T$
      * - $F$
        - $T$
        - $T$
      * - $F$
        - $F$
        - $F$

  .. container:: center-table

    .. list-table::
      :widths: 50 50
      :header-rows: 1

      * - $p$
        - $\sim p$
      * - $T$
        - $F$
      * - $F$
        - $T$

We are now ready to see an example of "translating an English sentence into the language of mathematics". Remember that part of the course objectives is to learn how to write mathematics. Here, the idea to communicate is given (in English) and we are just communicating it mathematically.

Let $p$ be the statement "I went to Universal Studios Singapore" and $q$ be the statement "I rode the Battlestar Galactica". To communicate "I went to Universal Studios Singapore and I rode the Battlestar Galactica", we may write $p\wedge q$. The choice of using $\wedge$ here really stems from our interpretation of the sentence, in particular the English word "and".

.. note:: There are many other ways to do this. In particular, note that there is nothing stopping us from letting $p$ be the entire statement, and then writing down $p$. Do you need the statement "I went to Universal Studios Singapore" elsewhere? If so, it might be a good idea to separate it out.

A compound statement is also a statement, so we can in fact use logical connectives to connect it with other statements, forming propositions like $p\wedge q\wedge r$ or $\sim p\vee q$.

Conditionals
^^^^^^^^^^^^

We will now introduce another logical connective: $\rightarrow$. Let $p$ and $q$ be statement variables. $p\rightarrow q$ is read "$p$ implies $q$", and have the following definition via a truth table.

.. container:: center-table

  .. list-table::
    :widths: 33 33 34
    :header-rows: 1

    * - $p$
      - $q$
      - $p\rightarrow q$
    * - $T$
      - $T$
      - $T$
    * - $T$
      - $F$
      - $F$
    * - $F$
      - $T$
      - $T$
    * - $F$
      - $F$
      - $T$

$\rightarrow$ is often used to write down ideas exhibiting conditional relationships. Let $p$ be "it is raining" and $q$ be "the ground is wet". The sentence "if it is raining, then the ground is wet" is written as $p\rightarrow q$.

The truth tables for $\wedge$, $\vee$ and $\sim$ quite intuitively captures the idea of "and", "or" and "not" in English. This is not quite the case for $\rightarrow$.

The second row makes the most sense to us: hypothetically if we observe that it is raining, but then we observe that the ground is not wet, the conditional relationship "if it is raining, then the ground is wet" cannot be true, so $p\rightarrow q$ being false captures this intuition.

Observe that $p\rightarrow q$ is required to be true when both $p$ and $q$ are true, as otherwise we cannot differentiate it from the case where $p$ is true and $q$ is false. Unfortunately, this makes sentences like "if you are reading this, then Paris is in France" true, and this intuition mismatch is what we have to accept.

What does our intuition tell us about $p\rightarrow q$ when $p$ is false? Well, nothing. We said "if $p$, then $q$". We did not intend to draw conclusions when $p$ is false. It is therefore our freedom to define $p\rightarrow q$ to be whatever we find convenient when $p$ is false. What we eventually settled on is to have it be true. One tutorial question later will give a justification on this decision.

.. note:: If you're interested, check out `paradoxes of material implication <https://en.wikipedia.org/wiki/Paradoxes_of_material_implication>`_ for more examples of intuition mismatch arising from the definition of $p\rightarrow q$.

As a result, when $p\rightarrow q$ is true, the only information we have is that it is impossible that $p$ is true but $q$ is false.

Biconditionals
^^^^^^^^^^^^^^

$p\leftrightarrow q$ is read "$p$ if and only if $q$" and is defined by the following truth table:

.. container:: center-table

  .. list-table:: $p\leftrightarrow q$ is true when $p$ and $q$ are both true or both false.
    :widths: 33 33 34
    :header-rows: 1

    * - $p$
      - $q$
      - $p\leftrightarrow q$
    * - $T$
      - $T$
      - $T$
    * - $T$
      - $F$
      - $F$
    * - $F$
      - $T$
      - $F$
    * - $F$
      - $F$
      - $T$

Intuitively, $p\leftrightarrow q$ is the conjunction of $p\rightarrow q$ and $q\rightarrow p$.

Ambiguity in Propositions
^^^^^^^^^^^^^^^^^^^^^^^^^

At this point, it should be understood that propositions have a truth value under a truth assignment of its statement variables. For example, the proposition $p\vee q\vee r$ is false if we assign $p$, $q$, $r$ to all be false.

An issue arises if we consider the expression $p\wedge q\vee r$. This statement could represent the conjunction of $p$ and $q\vee r$, or the disjunction of $p\wedge q$ and $r$. When $p$ is false, $q$ is true and $r$ is true, the statement is false in the former interpretation, but true in the latter.

This issue is similar to that of evaluating the arithmetic expression $3 + 4\times 5$. In both cases, ambiguity arises if we do not establish a conventional order of operations and/or introduce parentheses to the expression.

CS1231S establishes the convention that $\sim$ should be performed first, followed by $\wedge$ and $\vee$, which are coequal. This means that parentheses must be used to distinguish between the two possible interpretations of $p\wedge q\vee r$ as $(p\wedge q)\vee r$ or $p\wedge(q\vee r)$. Note that there is no "left-to-right evaluation rule". The expression $p\wedge q\vee r$ is deemed ambiguous and thus meaningless.

Continuing the order of operations, $\rightarrow$ and $\leftrightarrow$ are coequally performed last. This means, for example, that the statement $\sim p\wedge q\rightarrow r$ is unambiguous.

.. dropdown:: Question 2

  The following are common mistakes made by students. Can you explain the mistakes and correct them?

  a. $a\wedge\sim (b\wedge c)\equiv a\wedge\sim b\vee\sim c\quad\text{by De Morgan's law}$
  b. $\sim (x\vee y)\vee z\equiv\sim x\wedge\sim y\vee z\quad\text{by De Morgan's law}$

  .. dropdown:: Answer

    The expressions obtained after applying De Morgan's law is ambiguous. Correction:

    .. math::

      a\wedge\sim (b\wedge c)\equiv a\wedge (\sim b\vee\sim c)\quad\text{by De Morgan's law} \\
      \sim (x\vee y)\vee z\equiv (\sim x\wedge\sim y)\vee z\quad\text{by De Morgan's law}

.. hint::

  There is no need to remember the order of operations, as it could vary from courses to courses. In addition, it doesn't hurt to use parentheses whenever we are unsure of the order of operations, or to avoid confusing readers who might not be using the same conventions.

Tautologies and Contradictions
______________________________

A *tautology* is a proposition that is true under all possible truth assignments of its statement variables.

A *contradiction* is a proposition that is false under all possible truth assignments of its statement variables.

For example, the proposition $p\vee\sim p$ is a tautology, while the proposition $p\wedge\sim p$ is a contradiction, as can be seen from the following truth table:

.. container:: center-table

  .. list-table:: The column $p\vee\sim p$ is always $T$, while the column $p\wedge\sim p$ is always $F$.
    :widths: 25 25 25 25
    :header-rows: 1

    * - $p$
      - $\sim p$
      - $p\vee\sim p$
      - $p\wedge\sim p$
    * - $T$
      - $F$
      - $T$
      - $F$
    * - $F$
      - $T$
      - $T$
      - $F$

The intuition here is that a statement is always either true or false, but never both.

.. note:: At this point, it is important to realise that the number of rows in a truth table is decided by the number of statement variables involved. The propositions above only involve the variable $p$, which can either be true or false, resulting in two rows in the truth table.

Logical Equivalence
___________________

Two propositions $\phi$ and $\psi$ are *logically equivalent* (denoted $\phi\equiv\psi$) whenever their truth values are equal under all possible truth assignments to their statement variables.

.. note:: We tend to use Greek letters $\phi$ ("phi") and $\psi$ ("psi") to denote propositions. By our definition of propositions, this means for example that $\phi$ could consist of statement variables $p$, $q$ and $r$ alongside logical connectives.

For example, let $\phi$ be $p\rightarrow q$ and $\psi$ be $\sim p\vee q$. From the truth table below, we see that they share the same truth values under all possible truth assignments to $p$ and $q$.

.. container:: center-table

  .. list-table:: The column $p\rightarrow q$ is always the same as the column $\sim p\vee q$. Thus we have $p\rightarrow q\equiv\sim p\vee q$.
    :widths: 20 20 20 20 20
    :header-rows: 1

    * - $p$
      - $q$
      - $p\rightarrow q$
      - $\sim p$
      - $\sim p\vee q$
    * - $T$
      - $T$
      - $T$
      - $F$
      - $T$
    * - $T$
      - $F$
      - $F$
      - $F$
      - $F$
    * - $F$
      - $T$
      - $T$
      - $T$
      - $T$
    * - $F$
      - $F$
      - $T$
      - $T$
      - $T$

.. note:: What is the difference between $\leftrightarrow$ and $\equiv$? This is a question that has confused many students for extended periods of time, myself included. Some claim that they are interchangeable, some claim that there are philosophical differences. I am presenting below the differences as I understand it.

  * $\leftrightarrow$ is a logical connective. Hence, $\phi\leftrightarrow\psi$ can be viewed as one propositional statement.
  * $\equiv$ is an assertion on propositional statements. $\phi\equiv\psi$ cannot be viewed as one propositional statement. Rather, it is a statement asserting the logical equivalence between two propositional statements.

  If you are interested to dive into the rabbit hole, similar questions had been asked in the Mathematics Stack Exchange `here <https://math.stackexchange.com/questions/2432462/whats-the-difference-between-biconditional-iff-and-logical-equivalence>`_ and `here <https://math.stackexchange.com/questions/500644/distinction-between-equality-logical-equivalence-and-biconditionality>`_. The same question was also asked in the Philosophy Stack Exchange `here <https://philosophy.stackexchange.com/questions/65024/what-is-the-difference-between-logical-equivalence-and-material-equivalence>`_.

The equivalence between $p\rightarrow q$ and $\sim p\vee q$ is only one of a collection of laws establishing commonly used logical equivalences.

.. dropdown:: Laws of Logical Equivalences

  Let $p$, $q$, $r$ be statement variables, $\text{true}$ be a tautology, $\text{false}$ be a contradiction. One can verify using truth tables the following logical equivalences.

  * Commutative laws

    .. math::
      
      p\wedge q\equiv q\wedge p \\
      p\vee q\equiv q\vee p

  * Associative laws

    .. math::
      
      p\wedge q\wedge r\equiv (p\wedge q)\wedge r\equiv p\wedge(q\wedge r) \\
      p\vee q\vee r\equiv (p\vee q)\vee r\equiv p\vee(q\vee r)

    Note that due to the associative laws, propositions like $p\wedge q\wedge r$ is unambiguous.

  |

  * Distributive laws

    .. math::

      p\wedge(q\vee r)\equiv (p\wedge q)\vee (p\wedge r) \\
      p\vee(q\wedge r)\equiv (p\vee q)\wedge (p\vee r)

    Some students have trouble realizing that this is corresponding to the identities $a(b + c) = ab + ac$ and $(a + b)c = ac + bc$ for real numbers $a$, $b$, $c$.

  |

  * Identity laws

    .. math::

      p\wedge\text{true}\equiv p \\
      p\vee\text{false}\equiv p

  * Universal bound laws

    .. math::

      p\vee\text{true}\equiv\text{true} \\
      p\wedge\text{false}\equiv\text{false}

    Observe the similarities between the identity laws and the universal bound laws. Try not to confuse the two!

  |

  * Negation laws

    .. math::

      p\vee\sim p\equiv\text{true} \\
      p\wedge\sim p\equiv\text{false}

  * Double negative law

    .. math::

      \sim(\sim p)\equiv p

  * Idempotent laws

    .. math::
      
      p\wedge p\equiv p \\
      p\vee p\equiv p

  * De Morgan's laws

    .. math::

      \sim (p\wedge q)\equiv\sim p\vee\sim q \\
      \sim (p\vee q)\equiv\sim p\wedge\sim q

    It is helpful to see this law as "the distribution laws for negation".

  |

  * Absorption laws

    .. math::

      p\vee (p\wedge q)\equiv p \\
      p\wedge (p\vee q)\equiv p

    I used to forget this law exists until I needed it. Any time the same variable appears inside and outside the parentheses, and the two logical connectives are different, the proposition is logically equivalent to the repeated variable. In assignment 1, you will also see a variant of the absorption laws.

  |

  * Negation of $T$ and $F$

    .. math::

      \sim\text{true}\equiv\text{false} \\
      \sim\text{false}\equiv\text{true}

    To be pedantic, you can't quite see this using a truth table. We should rather just apply the definition of negation.

  |

  * Implication law

    .. math::

      p\rightarrow q\equiv\sim p\vee q

    Intuitively, $p\rightarrow q$ is only false when $p$ is true but $q$ is false, so $p\rightarrow q\equiv\sim (p\wedge\sim q)$. The equivalence then follows from De Morgan's Laws and the double negative law. Another way to remember this is to know that $p\rightarrow q$ is true the moment $p$ is false (hence the $\sim p$), but requires $q$ to be true when $p$ is true (hence the $q$).

With these laws at hand, we now have two methods to go around establishing the logical equivalence of two given propositions $\phi$ and $\psi$.

#. Use a truth table and compare the columns of $\phi$ and $\psi$. In general, the number of rows in the truth table should grow exponentially with respect to the number of variables involved.
#. Use the laws above to simplify $\phi$ and $\psi$ to the same proposition. More often than not, that same proposition is either $\phi$ or $\psi$.

.. dropdown:: Question 3
  :open:

  Simplify the propositions below using the laws given in **Theorem 2.1.1 (Epp)** and the **implication law** (if necessary) with only negation ($\sim$), conjunction ($\wedge$) and disjunction ($\vee$) in your final answers. Supply a justification for every step.

  a. $\sim a\wedge (\sim a\rightarrow (b\wedge a))$

  .. dropdown:: Answer

    .. math::
      \begin{align*}
        &\sim a\wedge (\sim a\rightarrow (b\wedge a)) \\
        &\equiv\sim a\wedge (\sim (\sim a)\vee (b\wedge a)) &\text{by the implication law} \\
        &\equiv\sim a\wedge (a\vee (b\wedge a)) &\text{by the double negative law} \\
        &\equiv\sim a\wedge (a\vee (a\wedge b)) &\text{by the commutative law} \\
        &\equiv\sim a\wedge a &\text{by the absorption law} \\
        &\equiv a\wedge\sim a &\text{by the commutative law} \\
        &\equiv\text{false} &\text{by the negation law}
      \end{align*}

  b. $(p\vee\sim q)\rightarrow q$

  .. dropdown:: Answer

    .. math::
      \begin{align*}
        &(p\vee\sim q)\rightarrow q \\
        &\equiv\sim (p\vee\sim q)\vee q &\text{by the implication law} \\
        &\equiv (\sim p\wedge\sim (\sim q))\vee q &\text{by the De Morgan's law} \\
        &\equiv (\sim p\wedge q)\vee q &\text{by the double negative law} \\
        &\equiv q\vee(\sim p\wedge q) &\text{by the commutative law} \\
        &\equiv q\vee(q\wedge\sim p) &\text{by the commutative law} \\
        &\equiv q &\text{by the absorption law}
      \end{align*}
    
  c. $\sim (p\vee\sim q)\vee (\sim p\wedge\sim q)$

    .. math::
      \begin{align*}
        &\sim (p\vee\sim q)\vee (\sim p\wedge\sim q) \\
        &\equiv (\sim p\wedge\sim (\sim q))\vee(\sim p\wedge\sim q) &\text{by the De Morgan's law} \\
        &\equiv (\sim p\wedge q)\vee (\sim p\wedge\sim q) &\text{by the double negative law} \\
        &\equiv\sim p\wedge (q\vee\sim q) &\text{by the distributive law} \\
        &\equiv\sim p\wedge\text{true} &\text{by the negation law} \\
        &\equiv\sim p &\text{by the identity law}
      \end{align*}

More on Conditionals
____________________

We will make the following definitions:

* The *converse* of the proposition $p\rightarrow q$ is $q\rightarrow p$.
* The *inverse* of the proposition $p\rightarrow q$ is $\sim p\rightarrow\sim q$.
* The *contrapositive* of the proposition $p\rightarrow q$ is $\sim q\rightarrow\sim p$.

There are several observations to make here:

#. The converse of the converse is the original proposition. The same applies to inverse and contraposition.
#. $p\rightarrow q$ is logically equivalent to its contrapositive, i.e. $p\rightarrow q\equiv\sim q\rightarrow\sim p$.

   * This means "if it is raining, then the ground is wet" can be rephrased as "if the ground is not wet, then it is not raining".
   * We can simplify $p\rightarrow q$ to $\sim q\rightarrow\sim p$ as follows:

   .. math::
      \begin{align*}
        p\rightarrow q &\equiv\sim p\vee q &\text{by the implication law} \\
        &\equiv q\vee\sim p &\text{by the commutative law} \\
        &\equiv\sim(\sim q)\vee\sim p &\text{by the double negative law} \\
        &\equiv\sim q\rightarrow\sim p &\text{by the implication law}
      \end{align*}

#. The contrapositive of the inverse is the converse (and vice versa).

   * By the previous observation, this tells us that $\sim p\rightarrow\sim q\equiv q\rightarrow p$.

To summarise, $p\rightarrow q$ is logically equivalent to its contrapositive $\sim q\rightarrow\sim p$. Its converse $q\rightarrow p$ is logically equivalent to its inverse $\sim p\rightarrow\sim q$, which is also the contrapositive of the converse.

In particular, it is a common logical fallacy to believe that "if $p$, then $q$" can be rephrased as "if not $p$, then not $q$" or "if $q$, then $p$". These two fallacies are known as *inverse error* and *converse error* respectively.

As alluded to earlier, the propsition $p\leftrightarrow q$ is in fact logically equivalent to the conjunction of $p\rightarrow q$ with its converse / inverse, i.e. $p\leftrightarrow q\equiv (p\rightarrow q)\wedge (q\rightarrow p)$. This can be verified using a truth table:

.. container:: center-table

  .. list-table:: The columns $p\leftrightarrow q$ and $(p\rightarrow q)\wedge (q\rightarrow p)$ are identical.
    :widths: 16 16 17 17 17 17
    :header-rows: 1
    
    * - $p$
      - $q$
      - $p\leftrightarrow q$
      - $p\rightarrow q$
      - $q\rightarrow p$
      - $(p\rightarrow q)\wedge (q\rightarrow p)$
    * - $T$
      - $T$
      - $T$
      - $T$
      - $T$
      - $T$
    * - $T$
      - $F$
      - $F$
      - $F$
      - $F$
      - $F$
    * - $F$
      - $T$
      - $F$
      - $T$
      - $F$
      - $F$
    * - $F$
      - $F$
      - $T$
      - $T$
      - $T$
      - $T$

So something "nice" happens when both $p\rightarrow q$ and its converse / inverse are true, in the sense that $p$ and $q$ are either both true or both false.

If, Only If, Necessary and Sufficient Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In English, the following four sentences all have the same meaning as "if $p$, then $q$", and are therefore all written mathematically as $p\rightarrow q$.

* $q$ if $p$.
* $p$ only if $q$.
* $q$ is a *necessary condition* of $p$.
* $p$ is a *sufficient condition* of $q$.

The only information that is communicated by the sentence "it is raining only if the ground is wet" is "if the ground is not wet, then it is not raining". In particular, it is not claiming that "if the ground is wet, then it is raining" -- there are other ways to make the ground wet. Hence generally, the sentence "$p$ only if $q$" is translated as $\sim q\rightarrow\sim p$, which is logically equivalent to $p\rightarrow q$, and not $q\rightarrow p$.

As a corollary, if it is both true that "$p$ if $q$" and "$p$ only if $q$", then mathematically we have $p\leftrightarrow q$. This justifies reading $p\leftrightarrow q$ as "$p$ if and only if $q$".

A more contrived way of saying "if $p$, then $q$" is "given that $p$ is true, it is necessary that $q$ is true". This is what we mean by "necessary condition". We also say that $p$ is a sufficient condition of $q$, since the condition of $p$ being true is sufficient for us to conclude that $q$ is true. There might be other ways to make $q$ true, but $p$ being true is already sufficient.

Similarly, if $p$ is a necessary and sufficient condition for $q$ (or vice versa), we write $p\leftrightarrow q$.

At this point, some students complain that this part of the course felt like an English lesson. Yes, I agree, we can't translate a sentence without being able to interpret it in the first place.

.. note:: This is a good place to mention that English (and every other natural language) can be ambiguous, and interpretations of English sentences can be highly subjective. In a sense, I only forcefully declared that we will interpret the four sentences above as $p\rightarrow q$. What I also hope is that you can gain some intuitions behind why we are interpreting them as such.

.. dropdown:: Question 1

  One of the most confusing concepts many students find is the difference between "if" and "only if", and the relationship among "if", "only if", "necessary condition" and "sufficient condition".

  a. Given these two statements: "I use the umbrella if it rains" and "I use the umbrella only if it rains". They may sound the same but in logic they are worlds apart! Now, rewrite them into propositional statements by using variable $p$ for "I use the umbrella", variable $q$ for "it rains" and the logical connective $\rightarrow$.

  .. dropdown:: Answer

    * "I use the umbrella if it rains" is rewritten as $q\rightarrow p$.
    * "I use the umbrella only if it rains" is rewritten as $p\rightarrow q$.

  b. "I use the umbrella if it rains": Is "I use the umbrella" a necessary condition for "it rains"? Or is "I use the umbrella" a sufficient condition for "it rains"? Is "it rains" a necessary condition for "I use the umbrella"? Or is "it rains" a sufficient condition for "I use the umbrella"?

  .. dropdown:: Answer

    * "I use the umbrella" is a necessary condition for "it rains".
    * "It rains" is a sufficient condition for "I use the umbrella".

  c. What if we say "I use the umbrella if and only if it rains"? How would you write a logic statement using variables $p$ and $q$, the imply connective $\rightarrow$, and either $\wedge$ or $\vee$? Is there a shorter way to write the logic statement using some other logical connective?

  .. dropdown:: Answer

    * Without using $\leftrightarrow$, "I use the umbrella if and only if it rains" is written as $(p\rightarrow q)\wedge (q\rightarrow p)$.
    * Using $\leftrightarrow$ gives us a shorter proposition $p\leftrightarrow q$.

  d. "I use the umbrella if and only if it rains". What kind of condition is "I use the umbrella" for "it rains"?

  .. dropdown:: Answer

    "I use the umbrella" is a necessary and sufficient condition for "it rains".

Arguments
_________

An *argument form* is a sequence of propositions $\phi_1, \phi_2, \cdots , \phi_k$ known as *premises*, followed by a proposition $\psi$ known as the *conclusion*. They can be denoted like so:

.. math::

  \begin{array}{l}
  \phi_1 \\
  \phi_2 \\
  \vdots \\
  \phi_k \\
  \hline
  \therefore\psi
  \end{array}

Moreover, if $\phi_1\wedge\phi_2\wedge\cdots\wedge\phi_k\rightarrow\psi$ is a tautology, we say that the argument form is *valid*.

For example, here is an argument with two premises $p\rightarrow q$ and $p$, followed by the conclusion $q$:

.. math::

  \begin{array}{l}
  p \\
  p\rightarrow q \\
  \hline
  \therefore q
  \end{array}

