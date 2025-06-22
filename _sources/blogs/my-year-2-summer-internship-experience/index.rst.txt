My Year 2 Summer Internship Experience
======================================

Apart from creating a personal website, one of the more significant things I have done during the recently-concluded summer vacation was that I did an internship as a software engineer in a startup going by the name of MixtureAI.

I am aware that there are only at most 3 summer internships one can do over the course of a 4-year degree, and I am already on the second one, so I was really trying to get the most out of it. This is exactly why I have been documenting my experience throughout the journey, so that I can conveniently look back right now and have a clear record of what happened during the internship. I then sort of promised my supervisor to write a blog about the experience, so here I am.

.. figure:: images/y2_intern_batch.png
   :width: 600
   :alt: The summer intern batch during a sharing session

   The summer intern batch during a sharing session

How I Got the Internship In the First Place
___________________________________________

So I was actually extremely busy during both semesters of my year 2, to the point where I didn't really end up applying for many internships. In fact, I think Optiver and TikTok were the only two companies that I had applied for (mostly out of peer pressure). I was not too worried about it and thought I would just enjoy my summer vacation without any internships, since I have already fulfilled the industry experience requirements from the CVWO programme I took back in year 1 summer.

Very briefly, partially thanks to my role as a CS2040S TA in year 2 semester 2, I got to know another graduate TA in the teaching team going by the name of Eldric, through a student of mine called Yen Xing, who informed me that Eldric's friend is the CEO of a startup that had some open internship positions. I was made aware that we will working around large language models (LLM). Despite the fact that I literally gave up CS2109S one semester earlier, I thought that my role as a software engineer intern would have less to do with ML.

I indicated my interest, sent my resume across, went through a pretty casual interview and got the offer. My biggest appreciation goes to Yen Xing and Eldric for bridging this opportunity. During the interview, I was honest that I am leaning more towards research and academia, and less towards industrial practices. Thankfully, the interviewer (who is also the CEO mentioned earlier) Ming Liang also seemed to be quite theory-oriented and we actually ended up having some discussions on mathematics side of machine learning.

.. figure:: images/convex.png
   :width: 600
   :alt: Convex function, one of the concepts Ming Liang tested me on during the interview

   `Convex function, one of the concepts Ming Liang tested me on during the interview <https://www.researchgate.net/figure/Figure-A2-Graph-of-a-convex-function_fig34_45667524>`_

Week 1 to Week 7: NLP Research
______________________________

My internship was effectively broken down into two halves, the first was mainly regarding LLM research and the second was about actual software engineering, where I get to actually work on an ongoing project. I guess this is a thing that happens when we work in a startup - we might not end up doing whatever was written on the job description.

From Giving Up on CS2109S to Reading NLP Research Papers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Even prior to the first week of the internship, I received a reading package from my supervisor (who is also the CEO mentioned earlier) Ming Liang, consisting of three NLP research papers. Having never read any research paper prior to this, I felt a bit overwhelmed but also excited on the experience.

Ironically, I didn't even had a solid foundation on the theories behind neural networks. For context, due to unexpectedly high workload two semesters ago, I gave up CS2109S halfway and just hoped for a pass (which I got). It was around the time when the lecture was covering backpropagation that I started giving up. Prior to this internship, I had to spend time actually forcing myself to learn backpropagation, RNNs, LSTMs, and eventually transformers in the span of around one week. I honestly felt good afterwards knowing that I am starting to catch up on what was missed from giving up on CS2109S.

.. figure:: images/transformer.png
   :width: 300
   :alt: Architecture of a transformer as per the original paper

   `Architecture of a transformer as per the original paper <https://arxiv.org/abs/1706.03762>`_

Among the papers I was tasked to read, one of them is on a novel approach to augmenting LLMs with tools, which goes by the name of `ToolkenGPT <https://arxiv.org/abs/2305.11554>`_. I was required to give my review on the paper, especially on its experimental design. Consequently, this became the first research paper which I have really read thoroughly and gave a review on.

Prior to writing the review, I had an insightful conversation with Ming Liang with respect to how ML research is really like. This was what I had written down for myself, essentially rephrased from what Ming Liang told me:

   People always cheat in the section of experimental design to get a paper published. There is certainly a positive bias in ML literature. In general, this means that the section will be peer-reviewed the heaviest. As a scientist or an engineer, it is arguably a good practice to tend to look at this section of a paper. One can usually come up with some experiments that the authors will wish they did. One must also be fair to them, for they probably had little time. For each paper, data scientists/another research group can come in and perform more rigorous testing on the ideas proposed in the paper, either to write another paper building on them, or to present a better understanding of how to engineer a system using them.

vLLM
^^^^

One of the first practical tools I came in touch with is `vLLM <https://github.com/vllm-project/vllm>`_. It is essentially a tool that allows us to serve language models locally so that it can receive requests and perform inferences. We were using it to serve Mistral and I was tasked at finding out the optimal GPU memory utilization for it to perform decently well for a context length of at least 9000 tokens. I also remember running scripts to bombard the server with over 10 requests at once to observe its reliability.

vLLM have been useful for me to experiment with different local language models as switching between them is just a matter of changing a model name parameter. In the project that I was mainly working on in the second half, vLLM had also been a vital microservice for the application to send chat completion queries to it.

DSPy
^^^^

.. figure:: images/dspy.png
   :width: 600
   :alt: The DSPy framework

   `The DSPy framework <https://towardsdatascience.com/intro-to-dspy-goodbye-prompting-hello-programming-4ca1c6ce3eb9>`_

DSPy is a Python framework that I was told to pick up because it was the framework being adopted by the ongoing project. It essentially provides abstractions and optimizations on the various instances of language models used across different parts of a task flow.

The problem I was tasked to work on is a tool selection problem. Given a user's prompt, a set of tools (consisting of names and descriptions), we need to predict an appropriate tool to execute so as to fulfill the user's request in the prompt. Making use of the DSPy framework, we tried to approach this problem via zero-shot and few-shot in-context learning (ICL), which essentially means appending instructions together with a few (possibly zero) examples in the prompt in hopes that the LM is able to recognize relevant patterns and extrapolate to produce accurate predictions.

Using Jupyter Notebooks, I had to try out the performance of various different local models such as Mistral, Gorilla and Llama to figure out how well they can work with DSPy in the case of zero-shot learning and few-shot ICL, the most prominent issue being the limited context length of these models. This involves identifying failure modes and trying to create datasets that capture these cases. Next thing I know, the use of this framework in the ongoing project was deprecated, although the team did learn a lot using it.

The BERT Classifier
^^^^^^^^^^^^^^^^^^^

.. figure:: images/bert_classifier.png
   :width: 600
   :alt: How a BERT classifier works

   `How a BERT classifier works <https://www.geeksforgeeks.org/sentiment-classification-using-bert/>`_

At some point I was introduced to the BERT's bidirectional encoding approach, in particular that there is this special [CLS] token (CLS stands for classifier) whose final hidden state can essentially capture the semantics of the rest of the given prompt. We can then attach a feed-forward neural network taking in that hidden state as input and vector of class probabilities as output to accomplish a sequence classification task.

It became prominent that the problem we are trying to solve is, at its core, a sequence classification task, one classical example of which is the sentiment analysis problem. Thankfully, I vaguely remember what sentiment analysis is from `this Michael Reeves video <https://www.youtube.com/watch?v=USKD3vPD6ZA>`_ (yes, i am a big fan of Michael Reeves), which allowed me to draw connections. And so I started experimenting with fine-tuning a BERT classifier in the context of the tool selection problem. Thankfully, Hugging Face had an extremely helpful library that allows me to do exactly this.

The accuracy scores are initially bad, but not for so long, because I would eventually notice the class imbalance in the training data used to perform the fine-tuning. I implemented oversampling on the training data, and also augmented more data using a not-so-reliable-but-usable library named `textaugment <https://github.com/dsfsi/textaugment>`_. Surprisingly, this allowed me to push the accuracy of the model to over 90%.

Miscellaneous NLP Techniques
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are many other different techniques here and there commonly used in LLM fine-tuning that I have got myself to play around with.

.. figure:: images/lora.png
   :width: 600
   :alt: Illustration of LoRA

   `Illustration of LoRA <https://www.run.ai/guides/generative-ai/lora-fine-tuning>`_

* `Diagonal Attention Pooling (Ditto) <https://arxiv.org/pdf/2305.10786>`_, a.k.a. "pick a particular attention head from a particular layer in a transformer and use the diagonal values of its attention matrix to compute a weighted average of hidden states to be used as sentence embedding".
* `P-Tuning <https://huggingface.co/docs/peft/en/package_reference/p_tuning>`_, which adds and optimizes additional prompt embeddings to the input prompt, intended to replace manual prompt tuning.
* `Quantization <https://medium.com/@techresearchspace/what-is-quantization-in-llm-01ba61968a51>`_, a technique to reduce memory consumption by loading the model weights in reduced precision.
* `Low-Rank Adaptation (LoRA) <https://arxiv.org/pdf/2106.09685>`_, a technique that allows for fine-tuning large language models by injecting trainable low-rank matrices into the transformer while keeping the pre-trained model weights frozen.

Each of the topics above are what I have worked with extensively, especially throughout the end of the first half of the internship.

Week 8 Onwards: Software Engineering
____________________________________

During the first half of the internship, I did get instructed every once in a while either to test, containerize, or make very little changes to the project repository. It was around week 8 onwards, when deadlines are coming in, that I eventually got called upon to help out more comprehensively on this ongoing project that is essentially an office assistant with the capabilities to perform tool calls such as sending emails via Microsoft Graph.

Google Cloud Platform (GCP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Almost exclusive to a startup internship experience, I get to access the GCP dashboard hosting several VM instances that forming development environment of the project. Most of the work has to be done on the VM instances so that we have access to the GPUs required for the underlying language model to perform inferences. I got to experience creating and deleting VM instances as well as building and deploying of the project via deploy hooks.

Docker and Containerization
^^^^^^^^^^^^^^^^^^^^^^^^^^^

I get called upon every once in a while to "containerize the app". Considering that I have never worked seriously with Docker before, it took me a while to figure out what this phrase exactly meant. In particular, the project I had been working on is a Flask app, and I need to work on a Dockerfile that can build a Docker image serving the Flask app when run.

I did this containerization thing sufficient number of times that I had started to get comfortable with it. I remember the resulting image size being too large to the point where the deployment of the project on GCP actually timed out, and it turns out that there are various tips and tricks to cut down on this size by editing the Dockerfile cleverly.

.. figure:: images/docker_meme.png
   :width: 600
   :alt: Relevant meme to avoid wall of text

   `Relevant meme to avoid wall of text <https://blog.zanalytics.io/ok-lets-talk-about-docker-4334a1a53c77>`_

In fact, I got so comfortable working with Docker that Ming Liang told me to give a presentation on it. Given my passion in teaching, I couldn't see myself talking about something that I personally do not understand in-depth, which is why I forced myself to go through the `Docker 101 Tutorial <https://www.docker.com/101-tutorial/>`_ just to prepare for that presentation.

Endless Software Engineering Routine Work
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The rest of the second half of the semester is mostly what a typical software engineer would do. In my case, my team and I worked exclusively on the backend, where we write code to handle the logic from the point where the assistant receives the user prompt all the way to response generation, while making sure that the assistant is coherent and does not hallucinate too much.

It takes nothing more than time for me to familiarize with the code base. I think I did unexpectedly learn to use a Python debugger on VS Code thanks to one of my coworkers Joseph. We did the usual implementing, testing, debugging and documenting, and every once in a while, we had to do system redesigns to accommodate for new requirements from the clients. It suffices to say that the design of the project when we left at the end of the summer is nothing similar at all to what we had in the beginning.

.. figure:: images/3000th_commit.png
   :width: 300
   :alt: Instagram story on me hitting the 3000th commit

   At some point the project hit 3000 commits and I had an Instagram story on this event

I guess a more memorable event was that we refactored the codebase and removed over 10,000 lines of deprecated code. We had a class named "GPT3_DspyBot" but the project was using none of these things. Both GPT3 and DSPy were already phased out from the project quite early on.

Perhaps a bit unfortunately, I wasn't there when the product is being shown to the clients, so I didn't really get to experience interacting with the clients as much as I did in CVWO.

Closing Remarks
_______________

Great, I did an internship and earned some money. Did I enjoy anything else besides money? Let's not forget that I have a dream of getting into academia and doing theoretical computer science. The first half of the internship was thus arguably more fun to me, though the second half did have me feel like I am making direct contributions to the company, for research has always been a long-term process and the value it can bring to the society has mostly been indirect. I guess either way, I get fulfilled for two different reasons, namely personal growth and adding value to the company.

**Edit, 22 June 2025.** It has been one year since the internship has concluded. I am migrating this post to the current website and so I got to re-read it. I guess the main value I extracted from the internship (apart from the money) is mostly on the side of personal growth: I get to understand how ML research in the industry is heavily empirical, and I developed some degree of comfort reading research papers. I start to agree less on being fulfilled by simply value-adding a company, for I believe that another essential element is to be able to enjoy the process of doing so. I am not sure if I enjoyed the process of software engineering, but I did enjoy the process of learning and researching. I guess this is why I have been going almost all-in towards academia ever since.

.. figure:: images/ml_stats_meme.png
   :width: 600
   :alt: Relevant meme to avoid wall of text

   `Relevant meme to avoid wall of text (its just a meme okay i dont think ml is exactly glorified stats) <https://towardsdatascience.com/no-machine-learning-is-not-just-glorified-statistics-26d3952234e3>`_

One observation I made throughout my ML research is that a lot of times, the model architectures/techniques seemed so arbitrary, and the authors' attempt at explaining the theory behind how such techniques work has been pretty unconvincing. On a random day, I stumbled upon `a podcast <https://www.youtube.com/watch?v=sJXn4Cl4oww>`_ while having my lunch. From that podcast, it was pretty insightful to learn that most state-of-the-art results in ML research have been empirical, while theory has been lagging behind. This is what I whole-heartedly agree on.

Given that I enjoy CS theory and formal proofs, this reality of empirical research of course felt unmotivating. This does not look like the type of research I would be interested to do. If, for some reason, I ended up doing ML research, I guess I would more than likely be focusing on developing the theories behind all the state-of-the-art results and performances.

As for the software engineering side of things, there isn't much technical to say except that I gained some experience working with Flask as well as a deeper understanding of Docker and containerization, perhaps also experienced what it's like working with GCP.

.. figure:: images/sg_interns_meetup.png
   :width: 600
   :alt: Meetup between interns based in Singapore few weeks after the internship has concluded

   Meetup between interns based in Singapore few weeks after the internship has concluded

The experience of working with a team is what brought it home for me. Being a 3-month remote internship work with the first half being ML research, it did feel like I am doing nothing productive. It was until when the second half came around and I actually started to hop on Zoom calls with the other software engineers that I started to feel like I am doing actual work. If you are a hiring manager and is reading this right now, yes, you are the target audience for this paragraph, please feel free to ask me details (such as how do I resolve a team conflict) in the behavioral interviews.

Anyways, more than how much I have learnt from the internship, I guess it is important to at least recognize that I have made the most out of it, as least that is what I chose to believe, because self-doubt is a pretty bad thing to do. Also, I am glad that I am able to find time to spit out this blog in the middle of week 1 of my semester. Good night.
