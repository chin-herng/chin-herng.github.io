CS1231S Discrete Structures
===========================

.. toctree::
    :hidden:

    tutorial-1/index
    
I intend to post write-ups for each of the 11 tutorials in the Semester 1 iteration of CS1231S. A write-up consists of reviews of lecture contents that are relevant for the tutorial, as well as solutions to the tutorial questions. It is possible that I interleave reviews of lecture contents and discussions of tutorial questions for ease of discussion throughout the tutorial. Each write-up more or less describes how I will usually host my physical tutorial sessions.

Below is an overview of the course, followed by some advice for students taking the course.

Overview
________

CS1231S is one of the first CS-coded courses every NUS Computer Science undergraduate will ever take that doesn't involve any coding. Instead, this course dives into the area of discrete mathematics, which is (up to some exceptions) essentially the intersection between computer science and mathematics. In MIT, this equivalent course seems to be "Mathematics for Computer Science", though that course covers many more equally important topics which we couldn't fit into CS1231S (e.g. asymptotic analysis). The NUS Mathematics Department offers an equivalent course known as MA1100 Basic Discrete Mathematics. The key difference between CS1231S and MA1100 lies on the topics covered towards the end of the semester. MA1100 goes into number theory, while CS1231S specialises into graph theory, which is in fact a lot more relevant to the field of computer science in general.

This course has two main objectives:

1. To teach students some topics in discrete mathematics. (duh)
2. To teach students how to read and write mathematical proofs.

There is nothing much to elaborate on the first objective, so let me focus on the second one.

The "Rigorous" Stage of Mathematical Education
______________________________________________

I strongly suggest reading Terence Tao's article `"There's more to mathematics than rigour and proofs" <https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/>`_. According to his division of mathematical education, all CS freshman taking the course is entering the "rigorous" stage, having been exposed to mathematics in a rather informal and intuitive manner with the exams being more computational than theoretical. I will also shamelessly promote my blog `"The Bridge Between Secondary School and University-Level Education" <../blogs/the-bridge-between-secondary-school-and-university-level-education/index.html>`_, in which I discuss how the expectation of students have been implicitly transitioned from simply scoring well in exams to actually learning the materials properly.

Indeed, one cannot get very far in mathematics relying on fuzzy notions and hand-waving. A certain amount of rigorousness are required to reason about an abstract concept concretely and thereafter draw non-trivial implications. One needs to develop theory based on careful logic. Definitions must be made explicit, thereafter theorems can be established only after they have been proven using logical arguments. This is what we mean by doing mathematics "properly", and teaching students this skill has been one of the main objectives of CS1231S.

The reason "properly" is put into quotes is because this is certainly not how mathematicians develop the mathematics you are studying today. Rather, mathematicians in their "post-rigorous" stage rely on intuitions and fuzzy notions to guide them towards believing a statement is true. Thereafter, they prove the statement rigorously to verify that their intuitions are correct.

I have had countless of students complaining that the entire course felt like an IQ test, and only the smartest students can think of what theorems / definitions to apply at which step. The issue about these students is that they are essentially treating the proof writing as the problem to solve, when in reality problem-solving never begins with proof writing. **Proof writing does not commence until one has gathered enough intuitions to do so.**

I also tend to hear students (and even some TAs) claiming that they should ignore their intuitions for the sake of CS1231S. I do not agree that we should just ignore our intuitions altogether, let alone the accusations that CS1231S is trying to mess up our brains for no good reason. Rather, the entire point of the "rigorous" stage is to repair bad intuitions developed in the "pre-rigorous" stage, i.e. things that we feel is correct but is logically false. Good intuitions, on the other hand, should be preserved. To enter the "post-rigorous" stage is to eliminate almost all the bad intuitions, thus allowing a more effective exploration of mathematics.

Symbols and Notations
_____________________

Mathematical symbols and notations are created to facilitate communication of mathematical ideas. For this reason, the language is artifically created and is designed to be unambiguous and effective, without the need for "politeness" considerations. CS1231S aims to teach us most of the conventional symbols and notations, so that we can start to read and write in the language of mathematics.

But let's not forget about intuitions. Suppose we have formed the necessary intuitions and are ready to write a proof. Due to how the language of mathematics is designed, we often find ourselves having to formally write down our ideas is a rather contrived manner. The resulting proof often resembles nothing like what went on in our mind initially. I like to say that the intuitions are "buried within" the ocean of formalisms. Consequently, written mathematics presented to the general public appear to be cryptic and overwhelming.

We should therefore also be aware of this phenomenon when we try to read a piece of mathematics (e.g. when digesting the various definitions, theorems and proofs in the course). It is insufficient to only understand what the symbols and notations mean in their literal sense. We should also start to think about what the author was thinking when they wrote down this piece of mathematics. We should aim to understand not just what the symbols are doing, but also what the author is trying to do. Apart from allowing us a deeper understanding in our reading, we also allow room to still understand the author to some extent even if a symbolic error is made in the final proof.

.. note::

    One more shameless self-promotion: my blog `"On Learning and Teaching Mathematics" <../blogs/on-learning-and-teaching-mathematics/index.html>`_ has an extensive discussion and some examples of intuitions buried within written mathematics, written from the lens of linguistics.

Conclusion
__________

Aligning to the course objectives listed above, it is insufficient to only intuitively understand the mathematical concepts being covered, or to only understand how to read and write mathematical proofs. You need the former to deal with the big picture, and the latter to correctly deal with the finer details. When you need to write down a proof, understand that an intuition must first be formed. When you are reading mathematics, do not stop at the symbolic level, but aim to go further into the author's mind.

With all of these out of the way, the course will spend the first two weeks on logic, to make sure we are familiar with the various logical connectives and the laws relating them, as well as working with quantifiers. We will then apply them in whatever further topics we explore (starting with set theory).
