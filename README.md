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

- `assignments/week-00-assignment` through `assignments/week-15-exam`
- `src/app/components/`
- `src/app/page.tsx`

Each assignment-style folder contains:

- `INSTRUCTIONS.md`
- `student_work.py` (the single editable coding file)
- `test_assignment.py`

## Course Schedule

- **Week 0:** week-00-assignment - Orientation
- **Week 1:** week-01-assignment - Python Basics
- **Week 2:** week-02-assignment - Variables/Deployment
- **Week 3:** week-03-assignment - Logic/Control Flow
- **Week 4:** week-04-assignment - Functions/Modular Programming
- **Week 5:** week-05-assignment - Data Structures
- **Week 6:** week-06-review - Review assignment
- **Week 7:** week-07-exam - Test 1 practice
- **Week 8:** week-08-assignment - OOP Classes
- **Week 9:** week-09-assignment - Advanced OOP
- **Week 10:** week-10-assignment - Error Handling/File IO
- **Week 11:** week-11-assignment - Unit Testing
- **Week 12:** week-12-assignment - Advanced Unit Testing
- **Week 13:** week-13-assignment - Best Practices
- **Week 14:** week-14-review - Review assignment
- **Week 15:** week-15-exam - Test 2 practice

## Week 0

`assignments/week-00-assignment/INSTRUCTIONS.md` provides UI-only onboarding steps for:

- forking the repository
- deploying to Vercel
- creating a branch
- launching Codespaces
- editing `student_work.py`
- running tests from the Testing panel
- committing and syncing via Source Control
- creating and merging a pull request
