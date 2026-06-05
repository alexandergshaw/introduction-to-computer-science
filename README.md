# Introduction to Computer Science - Student Portfolio Dashboard

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/alexandergshaw/introduction-to-computer-science)

This repository is a semester-long course scaffold for **Introduction to Computer Science**.
Students complete Python activities in the `assignments/` directory, and the Next.js dashboard displays module progress.

## Dashboard Purpose

The dashboard is built with **Next.js (App Router)** and **Tailwind CSS**. It reads each module's `student_work.py` file and marks progress cards as completed when assignment requirements are met.

- Locked modules remain inaccessible in the tracker until prior modules are completed.
- Completed modules display a checkmark in the dashboard.
- Review and exam practice modules are included in the semester flow.

## Repository Layout

- `assignments/assignment0` through `assignments/assignment16`
- `assignments/review6`, `assignments/review14`
- `assignments/exam7`, `assignments/exam15`
- `src/app/components/`
- `src/app/page.tsx`

Each assignment-style folder contains:

- `INSTRUCTIONS.md`
- `student_work.py` (the single editable coding file)
- `test_assignment.py`

## Course Schedule

- **Week 1:** assignment1 - Environment Setup
- **Week 2:** assignment2 - Variables/Deployment
- **Week 3:** assignment3 - Logic/Control Flow
- **Week 4:** assignment4 - Functions/Modular Programming
- **Week 5:** assignment5 - Data Structures
- **Week 6:** review6 - Review assignment
- **Week 7:** exam7 - Test 1 practice
- **Week 8:** assignment8 - OOP Classes
- **Week 9:** assignment9 - Advanced OOP
- **Week 10:** assignment10 - Error Handling/File IO
- **Week 11:** assignment11 - Unit Testing
- **Week 12:** assignment12 - Git/Branching
- **Week 13:** assignment13 - Best Practices
- **Week 14:** review14 - Review assignment
- **Week 15:** exam15 - Test 2 practice
- **Week 16:** assignment16 - Final Project

## Assignment 0

`assignments/assignment0/INSTRUCTIONS.md` provides UI-only onboarding steps for:

- forking the repository
- deploying to Vercel
- creating a branch
- launching Codespaces
- editing `student_work.py`
- running tests from the Testing panel
- committing and syncing via Source Control
- creating and merging a pull request
