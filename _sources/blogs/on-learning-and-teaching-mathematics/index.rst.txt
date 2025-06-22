On Learning and Teaching Mathematics
====================================

The following content is adapted from my submission to the individual essay assignment of the course EL1101E The Nature of Language. The given instruction is to find some original data and discuss the data from the perspective of semantics, pragmatics, sociolinguistics, or ethnolinguistics, or a combination of these perspectives. Essentially, I took an introductory course in linguistics, wrote an essay for an assignment, and decided to put it here. Note that what follows is almost a direct copy-paste from my essay, e.g. I did not bother to modify the tone/wordings to align more closely to a blog post than a homework submission.

As a person who enjoys mathematics and as an undergraduate tutor under NUS School of Computing currently in his third semester of teaching discrete mathematics, I constantly think about different ways to make learning mathematics easier and to teach mathematics more effectively. Motivated by Terence Tao's article `"There's More to Mathematics Than Rigour and Proofs" <https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/>`_, as well as drawing insights from the various perspectives of linguistics, I want to make an observation that in order to learn or teach any piece of maths (can be a mathematical definition, proof, or a result), one must break it down into its extension and intension, the latter of which is typically buried within the formalism of the language. Note that the discussion that follows will be focused on written maths.

Unlike in daily conversations, there is little need for "politeness" in mathematical writing. Mathematical statements are typically written as direct, expressed, and literal speech acts with a representative illocutionary type. Despite enjoying these properties, which presumably lower the effort required for comprehension, people still typically find mathematics to be difficult to understand. One possible explanation for this is that the language of mathematics is artificial rather than natural. Indeed, the language of maths is evolved to minimize ambiguity and maximize efficiency in terms of the number of symbols required to precisely communicate a given idea. As a result, every piece of modern maths is written in a way that appears to be cryptic to the general public. Now, suppose one learns the various mathematical notations and conventions required to read written maths. Can this person now effortlessly understand any piece of maths simply by reading through it?

In daily conversations and non-technical writings, it is typically easy for one to figure out an intension of a speech act whenever it is relevant to do so. The same cannot be said for mathematical statements, especially when they are written formally, as they typically are. The following is the definition of a continuous real-valued function given in a typical introductory calculus class:

.. math::

    \text{A function }f : \mathbb{R} \to \mathbb{R}\text{ is continuous }\iff\forall c\in\mathbb{R}\left(\lim_{x\rightarrow c} f(x) = f(c)\right)

One who is familiar with standard mathematical notations may read out the definition as it is, to obtain an extension of this definition: "A function :math:`f`, whose domain and codomain is the set of real numbers, is continuous if and only if for every real number :math:`c`, the limit of :math:`f` evaluated at :math:`x` as :math:`x` approaches :math:`c`, equals :math:`f` evaluated at :math:`c`".

Unfortunately, this is not a good way to think about continuous functions. At least, the person who initially came up with this definition definitely did not think about continuous functions in this way. It is after an intuition was formed regarding the concept to be captured that the author had to write down a definition in a more formal language so as to prevent any form of ambiguity. It follows that in order to really understand continuous functions, one has to go deeper and explore the intension of this definition. In other words, what is the concept that this definition is trying to capture? The following is a less formal definition of continuous functions, which does a good job at communicating this buried intuition, and is clearly less overwhelming to understand for students in the pre-rigorous stage of their maths education:

.. math::

    \begin{gather*}
        \text{If you can draw the curve of the function without ever lifting your pencil,}\\\text{then the function is continuous.}
    \end{gather*}

Here are more examples of this phenomenon, where (a) is the formal definition of a mathematical concept, and (b) is the underlying intuition.

\(a\) The cardinality of a finite set :math:`S` is a non-negative integer :math:`n\in\mathbb{Z}_{\geq 0}` such that there exists a bijection :math:`f:\{1, 2, \cdots, n\}\to S`.

\(b\) Cardinality means number of elements.

\(a\) The gradient of a linear equation :math:`ax + by + c = 0`, where :math:`a, b, c\in\mathbb{R}` and :math:`b\neq 0`, is defined to be :math:`-\frac{a}{b}`.

\(b\) Gradient means how steep the line is.

Remarkably, in each of these examples, one can also say that the mathematical definition entails the intuition. For instance, it is indeed a consequence from the mathematical definition of continuous functions that one is able to draw its curve in real life without ever picking up their pencil. Note that this is exactly our motivation for defining continuous functions this way. We generally want to give formal definitions that entail our intuitions merely as special cases and are general enough to include all objects of interest. This is exactly what is giving rise to the extension and intension of these definitions in the first place. Being aware of both of these layers of meaning is therefore crucial to enable one to wrap their head around seemingly cryptically defined mathematical objects.

Beyond mathematical definitions, we can also find examples of the same phenomenon occurring in mathematical theorems, as demonstrated in the following two examples:

\(a\) :math:`\forall a, b\in\mathbb{Z}^+\exists! q, r\in\mathbb{Z}^+ (a = bq + r\wedge 0\leq r < b)`.

\(b\) We can divide one number by another and get a quotient and a remainder.

\(a\) For every function :math:`f:A\to B` such that :math:`|A|\geq |B|`, :math:`f` is not injective.

\(b\) If there are more people than chairs, at least one chair must be shared.

The overarching theme here is that these results look overwhelming when written formally, but as it turns out, they are merely stating reasonably intuitive facts. From a learner's perspective, it is therefore a corollary that one cannot understand mathematics by merely knowing how to interpret and manipulate mathematical notations. On the other hand, as a maths educator, one cannot simply read through a well-written proof line-by-line and expect students to learn anything from the proof, exactly because the intension of the proof is typically buried within the various notations and formalisms. By providing insights on why the result is intuitively true before proceeding to present a formal proof, we basically give an answer to students asking "how can I ever come up with such proofs in the exam?". Simply put, problem solving does not begin with writing proofs. Proof writing commences only when one has formed an intension it wants to communicate using mathematical symbols.


If one ever gets exposed to rigorous maths, this exposure typically happens in their early undergraduate years. At this stage, students typically get lost within the ocean of formalism and notations, forgetting to remind themselves of the intension behind whatever they are studying. Through this short discussion, I hope that I have made a point that in order to truly understand (or enable one to understand) maths, it is equally important to explore both layers of meaning: one needs the extension to correctly deal with the fine details and the intension to deal with the big picture.
