NUS CS Course Reviews Part 3
============================

The almost-one-month gap between part 2 and part 3 is mostly due to my engagement as a CS2040S TA in the upcoming semester. Long story short, I was told to finish 7 problem sets as soon as possible. This, together with course registration, internship work and my patriotism arising from the 2024 Paris Olympics contributed significantly to this delay.

|

.. figure:: images/cs_foundation_courses.png
   :width: 600
   :alt: List of CS Foundation Courses

   `NUS CS Foundation Courses <https://www.comp.nus.edu.sg/programmes/ug/cs/curr/#summary-of-degree-requirements-for-bachelor-of-computing-computer-science>`_

|

We are left with CS2106, CS2109S and CS3230. At this point, since course registration is mostly over, this series of reviews should just serve as a reference on the projected semester workload based on the courses the audience is allocated.

CS2106 Introduction to Operating Systems
________________________________________

I took this in AY23/24 Sem 1 under Prof. Colin Tan Kheng Yan and Li Jialin. My final grade is A.

* Tutorial Participation (5%)
* Midterm (20%)
* Labs (25%)
* Final (50%)

I find this course relatively more enjoyable as a continuation from CS2100. It covered many of the "computer terms" that I hear about every once in a while and never understand in-depth. I don't have a good summary of the contents, but here are some of the interesting questions I have had over the years of using a computer, that finally got briefly answered by the course:

* What is a process? What am I looking at in the task manager?
* How does a modern computer does so many things at once? How does it decide how much attention to give to each task and perform context switches so flawlessly?
* How did the OS locate and load a given program into memory? (this is a relatively recent question I had after learning about program counters in CS2100)

.. figure:: images/cs2106_abstraction_layers.png
   :width: 600
   :alt: Abstraction Layers from CS2100 Slides

   `This slide from CS2100 gives a big picture on what an operating system is <https://www.comp.nus.edu.sg/~cs2100/2_resources/lectures.html>`_

While CS2100 dives into the CPU and RAM hardware to investigate what exactly is happening to the 1s and 0s, CS2106 bridges the gap between hardware and software. It is therefore a natural overarching theme of the course to establish mappings between various hardware and software components. Addresses we allocate in the heap map to physical memory addresses. Folders and files map to actual disk locations.

Another overarching theme of the course is the clever use of caches to establish multiple layers of memory. We see things like "maintain a table to cache these things", then "maintain another table to cache this table", and so on and so forth. Tricks like these are super fun to learn, but also super tedious to execute by hand. Unfortunately, the latter is what will be tested in the exams.

The model of processes is introduced as an abstraction of the various tasks a computer needs to perform. Once we have this abstraction, the course starts to talk about things like how much memory to allocate to which processes (memory management) and when to run which processes (process scheduling).

A significant portion of the course is also dedicated to introducing us to parallel computing. For this reason, we get to write multi-threaded programs in C and we learn about fundamental topics of parallel computing like locks, semaphores and mutual exclusion. Finally, we learn a lot of miscellaneous and (actually) practically useful concepts such as writing bash scripts, performing IPC, system calls as well as the entire idea of a kernel.

**Content Difficulty: 5/10.** Honestly, the contents are fun and not too difficult to learn. I don't exactly know how to elaborate it further. Paying attention to the lectures and actively thinking about what is being done in the lab assignments is all we need to get a good grasp on the contents.

**Workload: 5/10.** 2 hour weekly lecture, 1 hour of tutorial and 1 hour of lab session. Lectures are super fun to attend. Tutorial sheets are of moderate difficulty with a mix of tedious tracing and actually thought-provoking questions. Nothing really goes on during the lab sessions. We attend them to present our work on the lab assignments.

Sometimes lab assignments can get a bit too annoying/difficult to do. Make sure ample time is allocated to complete them. I have personally missed one deadline and also witnessed one of my friends not able to complete one in time. I juggled this course together with CS2109S, CS3230 and two TA positions. This is the one with the lightest workload and that I worry the least about.

**Profs/TAs: 10/10.** First half of the lectures are given by Prof. Jialin while Prof. Colin covers the second half. Both of them had been extremely engaging and entertaining during the lectures. I never get bored/fall asleep exactly for this reason. Prof. Jialin's illustration of a deadlock is so funny I still remember it till this date. Prof. Colin's illustration of virtual memory via HDB is still in my Instagram story archives and I get a good laugh every time I revisit it. They are perhaps the reason I enjoyed CS2106 content so much.

Special mention to my lab TA Shi Zheng for his patience and tolerance to me and my friends for completing some of the lab assignments during the lab session, when we should have been presenting our work.

Extremely special mention to Shi Zheng and the Profs for giving me a chance for resubmission when I told them that I mistook the deadline of one of the lab assignments. I really did. There is no catch here. I mistook 12am as 12pm and started working on the assignment at 4am only to realize that I was already late by 4 hours. I am so glad that I was honest about this entire incident.

**Assessment.** Lab assignments are lowkey fun to work on. I get to work with Unix commands and write low-level system calls in C, also touching a little bit on parallel computing. It is pretty cool to see concepts like semaphores in action and how C actually has a library for all these low-level stuff. It felt exactly like how the teaching team wanted them to feel like -- enjoyable, practical, sometimes challenging, generally fun.

Exams are honestly not as bad as CS2100. Midterm was the perfect type of assessments in my opinion, where we are given MCQs that purely test on concepts rather than computations. Finals involve computation-heavy questions but at least they were not as tedious as CS2100 (and I was able to prepare better given the experience from CS2100). In my semester, the scope of the final was simply memory management and file system. I was honestly very shocked to get an A because I literally gave up on file systems.

CS2109S Introduction to AI and Machine Learning
_______________________________________________

I took this in AY23/24 Sem 1 under Prof. Muhammad Rizki Aulia Rahman Maulana and Ben Leong Wing Lup (for the sake of consistency with all reviews, I have to write the names in full). My final grade is B.

* Coursemology (30%)
* Midterm (35%)
* Final (35%)

I have a neutral view on the course but also whole-heartedly agree with most of the negative comments under my semester in NUSMods. They actually raised very valid points regarding what went wrong in that semester. With that said, I do not have a strong opinion on how AI/ML should be taught. For a field that got popular relatively recently, there remains a huge room of discussion and exploration on the best way for it to be taught effectively.

First of all, expect high workload and steep learning curve if you have never done any AI/ML whatsoever. Do not take this course alongside any other heavy commitments. I took it alongside CS2106, CS3230 and two TA positions. I ended up giving up on almost half of the course contents.

It was actually pretty enlightening to learn about AI as a more general concept than ML. The first four weeks of the course is mostly dedicated to classical AI, which I relate with the bots we encounter in various video games/board games. We had a review on various search algorithms like DFS, BFS and Dijkstra's Algorithm, but using slightly different terminologies. I also first learnt about the A* search algorithm, which is pretty interesting considering my interest in algorithms.

The course then slowly transitions into modern-day AI, a.k.a. machine learning, where we actually feed data into our program so that it can build a model out of it, and then use that model to make predictions. We started with linear regression, logistic regression and decision tree. I was still able to catch up with most of these concepts to the point where I can appreciate how machine learning is simply fitting a function to a bunch of points.

Then comes hell. The second half of the semester is pure hell. I vividly remember that there was a lecture about Support Vector Machines (SVM). That lecture was a mess. Nothing from that lecture is tested anyways. You see, I am extremely theoretically minded and interested in math. Prof. Rizki decided to tell us about support vector machines while skipping most of the math and telling us that these are too technical. In my view, he just tickled my curiosity towards SVMs and refused to elaborate further. I was pretty pissed off from that lecture because I basically learnt nothing.

The rest of the semester is dedicated to neural networks (feed-forward neural networks, CNNs and RNNs) and unsupervised learning. My semester workload has gotten unexpectedly high at this point. I stopped attending the lectures and, essentially, unofficially gave up the course. This is upon the realization that I don't really need what was taught in the lectures to do the problem sets. All I need is Google and some help from my peers. The final is purely practical and does not require any of the heavy math covered in the lectures.

Again, I'm not claiming any content from the course to be useless. The theory involved is very fundamental and important, so is the practical aspects in terms of familiarity with various libraries. Due to how this course is designed at the moment, theory enjoyers like myself are almost doomed to struggle, because theory is obviously way more difficult than a few lines of library code. We would get stuck on the theory without moving on to getting more hands-on experience on data preprocessing and actually training some models.

.. figure:: images/cs2109s_meme.png
   :width: 600
   :alt: Relevant meme to avoid the pain of CS2109S

   `Relevant meme to avoid the pain of CS2109S <https://www.linkedin.com/posts/chandramoulisubramanian_deep-learning-activity-7064546803328708608-iYo9/>`_

**Content Difficulty: 10/10.** The learning curve is extremely steep. Probably, I got used to being advantageous at early fundamental courses like CS1231S and CS2040S. Probably, I am finally getting a taste of the helplessness my peers felt when they took CS2040S without having any prior experience. Probably, this is not the case. We will never know.

The mathematics involved is tedious. I was too used to writing out linear equations and listing out the variables with careful subscripting. I didn't manage to get comfortable with condensing everything with matrices and performing matrix transpose/multiplication. It didn't help that the lectures are skipping most of the essential mathematics and just throwing out formulae on the screen.

Difficult course content does not imply difficult exams. This is especially the case for this course, because only around 20% of the lecture content is useful in the final.

**Workload: 10/10.** 2 hour weekly lecture and 1 hour of tutorial. Tutorial sheets are super difficult and I gave up preparing answers for them from around week 5 onwards.

Most of the workload comes from working on the weekly problem sets. They tend to introduce new libraries/concepts and we do have to spend time reading about them. Each of the problem sets was also very long and can often get challenging to complete.

**Profs: 7/10.** Honestly, Prof. Rizki is entertaining. I like how he plays funny TED Talks during lecture breaks. He is also very patient and responsive with students' questions, both during lectures and in the course forum.

We basically almost never interact with Prof. Ben so I can't give too much comments on him regarding this course. It suffices to say that he has been very distinctive and bold with his semi-rude/informal tone whenever he shows up in the course forum or announcements.

My TA Eric Han has been very kind and can explain things pretty well during tutorial sessions. The teaching page of this personal website is heavily inspired from `his <https://eric-han.com/>`_.

**Assessment.** Problem sets cover the practical aspects of AI/ML by introducing us to various libraries like NumPy, Pandas, scikit-learn and PyTorch, as well as data processing and augmentation techniques like oversampling and normalization. These are often what the lectures did not emphasize, because the lectures are designed to be theoretical (but then they skip all the math in the lectures so I actually don't know what they are doing at this point).

Midterm was a complete waste of time. I could not possibly fathom any rationale for its existence. I had the exact same feelings as how I felt about the CS2100 assessments. The paper was mostly computation-heavy and was designed so that any sane person could never complete it in time. Again, I know an algorithm that can multiply any two arbitrarily large numbers, but that does not mean I can multiply two 10-digit numbers by hand under time pressure. Assessments like these can never accurately reflect how much a student has learnt from the course. If anything, they only evaluate how fast a student can perform mechanical, boring and brainless work.

The final was a 28-hour take-home assessment. We were given a dataset without any context and we were supposed to train a model out of it. This is when most students realize that understanding everything from the lecture has nothing to do with how well they will perform in the final, because the final is purely practical in nature.

In my semester, it was a classification task. A lot of time was spent on observing, cleaning and augmenting the data. There wasn't a lot of choices when it comes to the deciding model architecture. Instead, there are very specific things we need to do to the data to get a huge improvement in the performance of the model, and it all boils down to knowing how to stare at the given data, and staring at it for long enough to gain insights.

CS3230 Design and Analysis of Algorithms
________________________________________

I took this in AY23/24 Sem 1 under Prof. Arnab Bhattacharyya and Rahul Jain. My final grade is B+.

* Tutorial Participation (10%)
* 2 Programming Assignments (10%)
* Weekly Assignments (20%)
* Midterm (20%)
* Final (40%)

I actually really enjoyed this course and I heavily regret taking this course alongside other heavy commitments. I wish I had spent more time on the course to get the most out of it. It remains one of the things in my todo list to revisit the course content, especially the second half of it.

The first half of the course takes the content CS2040S and make it rigorous with the help of mathematical reasonings developed from CS1231S. Excluding the weird kick-off of the course on stable matching, the course starts with a more rigorous approach to algorithm analysis, followed by various algorithm design paradigms, i.e. divide-and-conquer, greedy and DP. These topics are all within my comfort zone, and I am relatively confident with mathematical proof writing, so I was not struggling too much.

You thought I would have no trouble acing this course, but everything after the recess week was completely new to me, because they were no longer within the scope of competitive programming. Max-flow min-cut theorem is introduced as yet another novel algorithm design approach, followed by an introduction to computational intractability. This is where I had the most fun. I get to rigorously learn about a few complexity classes and reason about them via problem reduction. The course concludes with various methods to cope with intractability, such as approximation and randomization.

The second half of the semester really widened my view on algorithms and gave me a sneak peek into what theoretical computer science would look like. Especially now that I have decided to specialize in theoretical computer science, I eventually need to brush up on whatever I have missed while taking this course.

**Content Difficulty: 7/10.** Overall pretty challenging and fun. The first half of the semester, although contributing nothing new to what I already know, helped me to revisit the various topics in a more rigorous approach. For example, I was relatively less experienced in proving the correctness of greedy algorithms. This course gave me a good amount of practice in doing so.

To be fair, I took this course under a teaching team that sets easier assessments. On a different semester, this course will be run by none other than Prof. Steven Halim. I have seen my friends taking CS3230 under him. His problem sets are way more difficult and his lectures cover way more content than what I had experienced in my semester.

**Workload: 6/10.** 2 hour weekly lecture and 1 hour of tutorial. Tutorials would discuss the weekly problem sets. Each weekly problem set consists of around 3 problems which could often be challenging to solve/write a prove on. Problem sets would therefore be the main source of workload of the course, although I find it equally important to revise the lecture contents from time to time.

.. figure:: images/cs3230_kleinberg_tardos.png
   :width: 600
   :alt: Cover page of Algorithm Design by Jon Kleinberg and Éva Tardos

   `Cover page of Algorithm Design by Jon Kleinberg and Éva Tardos <https://archive.org/details/AlgorithmDesign1stEditionByJonKleinbergAndEvaTardos2005PDF/mode/2up>`_

**Profs/TAs:** 7/10: The textbook was way more informative than the lectures. I highly recommend reading Algorithm Design by Jon Kleinberg and Éva Tardos. It is more lightweight than CLRS (the bible) and also quite engaging to read. If one does not like the idea of reading textbooks, I alternatively recommend taking the course under Prof. Steven Halim instead, simply because the course will then be more engaging overall.

The 7 marks are given to my TA named Arpan Losalka. He is pretty engaging and responsive during his tutorial sessions. He summarizes lecture contents pretty well and is very patient when guiding students on providing their solutions to the problem sets.

**Assessment.** Midterm and final share very similar format as that of the problem sets. There are no MCQs/MRQs. We are typically required to write pseudo-code for an algorithm that solves a given problem, give proof for the correctness, and provide a running time analysis of the algorithm in question. There are various commonly-used techniques for various topics of the course. They can often be learned by looking at past-year papers or the problems on the textbook.

I did exceptionally well on the midterm due to my prior experiences in competitive programming and mathematics. I did not do very well on the final because so many things are new to me and I did not have time to digest them due to other heavy commitments. With that said, I did pretty well specifically on the topic of problem reducibility and complexity classes. This helped to motivate me to specialize in theoretical computer science.
