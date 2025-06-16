Teaching
========

.. note::

  I heavily adapted the layout of this page from `Dr. Eric Han's personal website <https://eric-han.com/teaching>`_. He was my tutor for *CS2109S Introduction to AI and Machine Learning* and he is also a very inspiring educator.

I have been an undergraduate teaching assistant (TA) for two courses per semester since my sophomore year. This means that I host weekly tutorial/laboratory sessions with a class size of less than 20 students for at least twice a week. These sessions usually involve a recap on lecture contents followed by a discussion on an assigned worksheet. I also contribute/check/grade assignment/exam questions as well as invigilate examinations to make sure no one is doing anything nasty.

My main goal as a TA is to help students learn. It is important to emphasize that I am not here to help them optimize their grades, but rather to help them learn the materials and develop a genuine interest in the subject. I do not assume that a good understanding of the subject will naturally translate to better grades, for there are many other factors that can affect a student's performance in an exam, but at the end of the day what benefits students in the long run is their solid understanding of the subject, not their grades. I share the same values in my own learning.

Teaching Philosophy
-------------------

*[WIP]* idk man i just explain and they just get it like wth

Teaching Feedback
-----------------

Over the years I have received many kind words from my students, all of which I am very grateful for. Pressing the button below generates one random positive feedback.

.. raw:: html

  <div style="margin-top: 2em;">
    <div style="text-align: center;">
      <button id="show-button" onclick="showRandomTestimonial()" style="
        padding: 0.5em 1em;
        background-color: var(--color-guilabel-background);
        color: var(--color-background);
        border: none;
        border-radius: 6px;
        font-size: 1em;
        cursor: pointer;
      ">
        Show Another
      </button>
    </div>

    <div id="testimonial-box" style="
      margin-top: 2em;
      padding: 1em;
      border-left: 4px solid var(--color-background-border);
      background-color: var(--color-background-secondary);
      color: var(--color-foreground-primary);
    ">
      <div id="testimonial-quote"></div>
      <div id="testimonial-meta" style="
        text-align: right;
        font-weight: 600;
        margin-top: 0.75em;
        color: var(--color-foreground-primary);
      "></div>
    </div>
  </div>

  <script>
    let testimonials = [];
    const quoteBox = document.getElementById("testimonial-quote");
    const metaBox = document.getElementById("testimonial-meta");

    fetch("_static/testimonials.json")
      .then(response => response.json())
      .then(data => {
        testimonials = flattenTestimonials(data);
        showRandomTestimonial();
      })
      .catch(error => {
        quoteBox.innerText = "Failed to load testimonials.";
        metaBox.innerText = "";
        console.error("Error loading testimonials:", error);
      });

    function flattenTestimonials(data) {
      const flat = [];
      for (const semester in data) {
        for (const course in data[semester]) {
          for (const quote of data[semester][course]) {
            flat.push({ quote, course, semester });
          }
        }
      }
      return flat;
    }

    function showRandomTestimonial() {
      if (testimonials.length === 0) return;
      const t = testimonials[Math.floor(Math.random() * testimonials.length)];
      quoteBox.innerText = `“${t.quote}”`;
      metaBox.innerText = `— Student from ${t.course}, ${t.semester}`;
    }
  </script>

.. note::

  Special thanks to `Pallon <https://www.linkedin.com/in/palloncx/>`_ for suggesting the idea of a random testimonial generator. You can find the full list of testimonials in `my GitHub repository <https://github.com/chin-herng/chin-herng.github.io/blob/main/docs/_static/testimonials.json>`_.

Effectiveness
-------------

.. list-table::
  :widths: 16 48 16 16
  :header-rows: 1
  :align: center

  * - Academic Year
    - Course
    - Score
    - Nomination
  * - AY2024/25 S2
    - CS2040S Data Structures and Algorithms
    - 5.0/5.0
    - 5/13 (38%)
  * - AY2024/25 S2
    - CS1231S Discrete Structures
    - 4.4/5.0
    - 6/22 (27%)
  * - AY2024/25 S1
    - CS2040S Data Structures and Algorithms
    - 4.9/5.0
    - 5/16 (31%)
  * - AY2024/25 S1
    - CS1231S Discrete Structures
    - 4.8/5.0
    - 13/37 (35%)
  * - AY2023/24 S2
    - CS2040S Data Structures and Algorithms
    - 4.6/5.0
    - 6/17 (35%)
  * - AY2023/24 S2
    - CS1231S Discrete Structures
    - 4.9/5.0
    - 6/19 (32%)
  * - AY2023/24 S1
    - TIC2001 Data Structures and Algorithms
    - 4.3/5.0
    - 2/10 (20%)
  * - AY2023/24 S1
    - CS1231S Discrete Structures
    - 4.6/5.0
    - 4/19 (21%)
