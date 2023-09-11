# Programming Assignment: Planning using Heuristic Search  <img align="right" src="UoA Vertical.svg"/>

**Prof. Felipe Meneguzzi**  

Artificial Intelligence (CS3033/QC3001):

- Assigned: Week 12
- Due: Week 18 (Monday 9am)

**REMINDERS:**  

1. Do not under any circumstances rename the files you get from this repo. Your assignment must be in a notebook called ```AI-Jupyternotebook.ipynb```;
2. Your implementation must not rely on any additional libraries (i.e., it must work with the standard Python 3.6 distribution);
3. Do not use any **generative AI models** (e.g., Co-Pilot, ChatGPT, etc) to write any portion of your code, as this constitutes plagiarism.

## Assignment Overview

<img align="right" style="margin:20px" src="planning-assignment.svg"/>

The goal of this work is to implement the core functions of an automated planner. You will implement three main functions in this assignment:
- Implement the **Max-Cost** heuristic function.
- Implement a function capable of validating a plan given a domain and a problem.
- Finally, implement the heuristic search **A\***

After implementing the required functions, you must write a 2-page paper. The entire package must be delivered using GitHub, where your implemented functions must be contained in this Jupyter Notebook, and the paper as a separate **pdf** file committed in the same Github repository in the ```paper``` folder.

## Experimentation

- You can test your implementation with the provided domains and problems:
  - [blocksworld](examples/blocksworld)
  - [dinner](examples/dinner)
  - [dwr](examples/dwr)
  - [tsp](examples/tsp)
  - [dompteur](examples/dompteur)
  - [logistics](examples/logistics)

- Planning tools and extra domains and problems to sanity check your own implementation:
  - [Web-Planner](https://web-planner.herokuapp.com/)
  - [editor.planning.domains](http://editor.planning.domains/)
  - IPC domains and problems can be found in [potassco/pddl-instances](https://github.com/potassco/pddl-instances)

## Grading

In order to properly evaluate your work and thought process, you will write a **2-page** report in the AAAI two-column format explaining your encoding and experiments.
These guidelines are to be followed **exactly**.
**Reports that are less than two pages of actual content, or not in format will receive 0 marks for the report criterion.** 
This report will be included in the deliverables of the assignment.
[The formatting instructions are available at Overleaf (AAAI Press)](https://www.overleaf.com/latex/templates/aaai-press-latex-template/jymjdgdpdmxp).
The report must have the following sections:

- An introduction with your understanding of the problem domain, outlining the remainder of the paper;
- Three sections explaining each part of your implementation (search, heuristic, and validator).
- One experimentation section where you measure the performance of the planner using your action formalisation for each of the domains, on multiple problems.
- One conclusion section, where you will summarise your experience in encoding planning domains and discuss the performance of the planner, and any limitations encountered in solving the problems you encoded.

Grading will consider elements of your encoding, experimentation, and reporting of the work done. 
The criteria, as well as their weight in the final grade is as follows:

- Implementation (70%):
  - Heuristic function (20%);
  - Validator (20%);
  - Heuristic search (30%):
    - Correctness and optimality (20%); and
    - Runtime efficiency (10%).
- Overall report readability (20%) — how accessible and coherent your explanation of your implementation is;
- Code readability (10%).

## Python Instructions
In a preconfigured computer you can just run (in Linux):
```zsh
jupyter notebook
```
and for Windows you should execute Jupyter Notebook from the start menu. Open the given URL in a browser, and navigate to the folder of the cloned repository of this assignment.

[Conda](https://conda.io) is required to run this assignment, and will install Jupyter for you.
The following sequence of steps creates a virtual environment and installs the required dependencies for Python 3.6:
```zsh
conda create -n py36_heu python=3.6
conda activate py36_heu #For windows: conda activate py36_heu

pip install ipykernel jupyterlab matplotlib nose
python -m ipykernel install --name py36_heu --user
```

## Important Information

**Corrections:** From time to time, students, or staff find errors (e.g., typos, unclear instructions, etc.) in the assignment specification. In that case, a corrected version of this file will be produced, announced, and distributed for you to commit and push into your repository. Because of that, you are NOT to modify this file in any way to avoid conflicts.

**Late submissions & extensions:** You have a 24-hour grace period with a penalty of 10% of the maximum mark, which increases to 50% until 48 hours after the due date, and 100% penalty thereafter. Extensions will only be permitted in _exceptional_ circumstances.

**About this repo:** You must ALWAYS keep your fork private and never share it with anybody in or outside the course, even after the course finishes. You are not allowed to make another repository copy outside the provided GitHub Classroom without the written permission of the teaching staff.

> **_Please do not distribute or post solutions to any of the projects and notebooks._**

<!-- **Collaboration Policy:** You must work on this project **individually** and follow the [university's academic integrity policy](https://www.abdn.ac.uk/staffnet/teaching/academic-integrity-12935.php).
You are free to discuss high-level design issues with the people in your class, but every aspect of your actual implementation must be entirely your own work.
Furthermore, there can be no textual similarities in the reports generated by each student.
Plagiarism, no matter the degree, will result in forfeiture of the entire grade of this assignment. -->
**Collaboration Policy:** You must work on this project **individually** and follow the [university's academic integrity policy](https://www.abdn.ac.uk/staffnet/teaching/academic-integrity-12935.php).
You are free to discuss high-level design issues with the people in your class, but every aspect of your actual implementation must be entirely your own work.
Furthermore, there can be no textual similarities in the reports generated by each student.

**Academic Dishonesty:** This is an advanced course, so we expect full professionalism and ethical conduct. Plagiarism is a serious issue, so please do not let us down and risk our trust. The staff take academic misconduct very seriously. We use sophisticated software for plagiarism detection to check your code against other submissions in the class as well as resources available on the web for logical redundancy. 
These systems are really smart, so just do not risk it and keep professional.
If you do violate the university's policy on academic integrity, we will pursue the strongest consequences available to us according to the University Academic Integrity policy.

**We are here to help!:** We are here to help you! But we don't know you need help unless you tell us. We expect reasonable effort from you side, but if you get stuck or have doubts, please seek help by creating an issue in the repository and assigning it to the instructor. Always keep the most updated version of your code pushed to Git so when you create an issue, the teaching staff can look into your code to help.

**Silence Policy:** A silence policy will take effect **48 hours** before this assignment is due. This means that no question about this assignment will be answered, whether it is asked on Moodle, by email, or in person. Use the last 48 hours to wrap up and finish your project quietly as well as possible if you have not done so already. Remember it is not mandatory to do all perfect, try to cover as much as possible. By having some silence we reduce anxiety, last minute mistakes, and unreasonable expectations on others.

Please remember to follow all the submission steps as per project specification.
