# Assignment 0: Course Setup (No Terminal)

Your very first file. Three tiny warm-up functions to get you used to the loop of "edit the code, then run the tests." Each one is a single line of code.

## What to build

1. `hello()` — return the exact text `Hello, world!`.
2. `favorite_language()` — return the name of the programming language this course is taught in.
3. `double_text(text)` — return `text` written out twice in a row, with nothing in between.
   - Helpful example: `double_text("ab")` → `"abab"`

## Helpful examples & notes

- A function hands a value back to whoever called it with the `return` keyword.
- Text wrapped in quotes is called a "string".
- Two strings can be combined into one longer string with the `+` operator.

> Tip: open `test_assignment.py` to see the exact inputs and expected outputs.

## Setup and submission steps

Follow every step using only the GitHub and Codespaces interface.

1. **Fork the repository**
   - Open the repository page in GitHub.
   - Click the **Fork** button in the top-right corner.
   - Create the fork in your own account.

   📖 [Fork a repo docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=HbSjyU2vf6Y)

   <iframe src="https://www.youtube-nocookie.com/embed/HbSjyU2vf6Y" title="How to fork a GitHub repository" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

2. **Deploy to Vercel**
   - In your fork, open the `README.md` file.
   - Click the **Deploy with Vercel** button.
   - Authorize Vercel if prompted.
   - Keep the default project settings and click **Deploy**.

   📖 [Vercel deployments docs](https://vercel.com/docs/deployments) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=1HN3RaYb7xo)

   <iframe src="https://www.youtube-nocookie.com/embed/1HN3RaYb7xo" title="Deploy a website to Vercel (beginner tutorial)" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

3. **Create a branch off `main` in the GitHub UI**
   - In your fork, open the branch selector near the top-left file list and make sure **`main`** is selected.
   - Type a branch name such as `assignment00-yourname`.
   - Click **Create branch** — it will branch from `main`.

   📖 [GitHub flow (branching) docs](https://docs.github.com/en/get-started/using-github/github-flow) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=1AIZaqeOCrI)

   <iframe src="https://www.youtube-nocookie.com/embed/1AIZaqeOCrI" title="Branching and pull requests in GitHub" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

4. **Open a Codespace**
   - Click the green **Code** button.
   - Select the **Codespaces** tab.
   - Click **Create codespace on assignment00-yourname**.

   📖 [GitHub Codespaces docs](https://docs.github.com/en/codespaces) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=gnC_NwDfkmI)

   <iframe src="https://www.youtube-nocookie.com/embed/gnC_NwDfkmI" title="How to use GitHub Codespaces (step by step)" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

5. **Edit your student file**
   - In Codespaces, open `assignments/week-00-assignment/student_work.py`.
   - Complete the three short functions described in **What to build** above.
   - Save the file.

6. **Run tests from the Testing panel**
   - Click the **Testing** beaker icon in the left sidebar.
   - Find `assignments/week-00-assignment/test_assignment.py`.
   - Click the **Run Test** play button.
   - Confirm the test passes.

   📖 [Testing in VS Code docs](https://code.visualstudio.com/docs/python/testing) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=V-1Sgv3xaaI)

   <iframe src="https://www.youtube-nocookie.com/embed/V-1Sgv3xaaI" title="Run Python tests in the VS Code Testing panel" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

7. **Commit with Source Control UI**
   - Click the **Source Control** icon in the left sidebar.
   - Review the changed file.
   - Enter a commit message like `Complete assignment00`.
   - Click **Commit**.

   📖 [VS Code Source Control docs](https://code.visualstudio.com/docs/sourcecontrol/overview) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=4dkNn93DIx4)

   <iframe src="https://www.youtube-nocookie.com/embed/4dkNn93DIx4" title="Commit and push from VS Code Source Control" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

8. **Push changes with UI controls**
   - In Source Control, click **Sync Changes**.
   - Confirm the push when prompted.

   📖 [Push & sync changes (VS Code Source Control)](https://code.visualstudio.com/docs/sourcecontrol/overview) — pushing is also shown in the commit & push video above.

9. **Create a Pull Request back into `main`**
   - Return to your fork on GitHub.
   - Click **Compare & pull request**.
   - Set the **base** branch to **`main`** and the **compare** branch to your branch.
   - Add a clear title and short description.
   - Click **Create pull request**.

   📖 [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) · [GitHub Skills](https://skills.github.com/) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=nCKdihvneS0)

   <iframe src="https://www.youtube-nocookie.com/embed/nCKdihvneS0" title="How to create a pull request in 4 minutes" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

10. **Merge the Pull Request into `main`**
    - After checks pass, click **Merge pull request**.
    - Click **Confirm merge**.
    - Click **Delete branch** after merging.

    📖 [Merging a pull request docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request) · 📺 [Watch on YouTube](https://www.youtube.com/watch?v=FDXSgyDGmho)

    <iframe src="https://www.youtube-nocookie.com/embed/FDXSgyDGmho" title="How to merge a pull request" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
