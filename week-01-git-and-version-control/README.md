# Week 01: Git And Version Control
## Curriculum Tracker - Stage 1: Git & Version Control

### 🎯 Key Learning Objectives
- Learn basic and advanced Git commands (clone, branch, merge, rebase, stash).
- Set up a personal GitHub profile and learn SSH-key authentication.
- Practice collaborative workflows: branches, pull requests, resolving merge conflicts, and code reviews.

### 📝 Actionable Lab Checklist
- [ ] Initialize a new Git repository locally
- [ ] Create a feature branch, make commits, and merge it into main
- [ ] Push a test project to GitHub/GitLab using SSH
- [ ] Practice resolving a forced merge conflict
- [ ] Document this week's learnings in `notes/`
- [ ] Commit source code/configuration files to `labs/` or `projects/`

### 📓 Study Notes & Resources
*Use this section to log key concepts, diagnostic commands, tool interactions, and links.*

---
*Created using the DevOps 2026 Workspace Setup Script.*
# Week 1 Study Notes: Git & Version Control Foundations

## 1. Core Paradigm: Snapshots vs. File Differences (Deltas)
To truly master Git, it is critical to understand how it differs from older Version Control Systems (VCS) like Subversion (SVN) or CVS.

*   **Traditional VCS (Delta-Based)**: Older systems store information as a list of file-based changes. They look at a base file and keep a sequential log of the differences (deltas) made to that file over time. To reconstruct any historical version, the system must chain these deltas together.
*   **Git's Paradigm (Snapshot-Based)**: Git does not store changes as individual file deltas. Instead, every time you commit your work, **Git takes a picture of what all your files look like at that exact moment and stores a reference to that snapshot** [1]. 
    *   To keep storage highly efficient, if a file has not changed in a commit, Git does not copy the file again; it simply creates a reference link pointing to the identical previous file version it already has stored.
    *   This snapshot architecture is what makes operations like branching, merging, and rolling back history incredibly rapid and reliable in Git.

---

## 2. Git's Core Architecture: The Three Local States
In Git, your files always reside in one of three local states or sections. Understanding this structure helps you predict exactly how files will move into your repository:

[ Working Directory ] --------> [ Staging Area ] --------> [ Git Directory (.git) ] (Sandbox/Draft)     git add      (Index/Ready)   git commit     (Permanent Snapshot)

1.  **The Working Directory (Sandbox / Local Workspace)**: This is the single checkout of one version of your project on your local computer's disk. You modify these files directly in your editor.
2.  **The Staging Area / Index (The Prep Zone)**: This is a file, generally contained in your Git directory, that stores information about what changes will go into your next commit. Think of it as a draft space where you compile exactly what you want to save.
3.  **The Git Directory (The Repository / `.git` Folder)**: This is where Git stores the metadata and object database for your project [1]. This is the most crucial part of Git, and it is what gets copied when you clone a repository from another computer [1].

---

## 3. Essential Command-Line Reference
Based on the 2026 DevOps Roadmap curriculum, these are the core operations you must commit to muscle memory [1]:

### Repository Setup
*   `git init`: Initializes a brand new local Git repository inside your current directory [1].
*   `git clone <url>`: Copies an existing Git repository (including its full history and `.git` metadata) from a remote platform like GitHub or GitLab to your local machine [1].

### The Staging-to-Commit Cycle
*   `git status`: Shows the state of the Working Directory and Staging Area (identifies untracked, modified, or staged files).
*   `git add <file>`: Moves a modified file from the Working Directory into the Staging Area.
*   `git commit -m "<message>"`: Captures a permanent snapshot of the staged files and writes it to the `.git` directory history.

### Branching & Merging (Non-Linear Workflows)
*   `git branch <branch-name>`: Creates a new independent development timeline (branch) [1].
*   `git checkout -b <branch-name>`: Shortcut to create a new branch and immediately switch your Working Directory to it.
*   `git merge <branch-name>`: Integrates the snapshot history from another branch into your current active branch [1].

---

## 4. Collaborative Engineering via Pull Requests
Git handles code tracking locally, but platforms like **GitHub** and **GitLab** enable teams to collaborate globally [1]. 

The industry-standard collaboration mechanism is the **Pull Request (PR)** [1]:
1.  **Isolate**: You create a separate feature branch to build your code or write notes without disrupting the stable `main` branch [1].
2.  **Publish**: You push your feature branch to the remote host (GitHub/GitLab) [1].
3.  **Request Review**: You open a Pull Request [1]. This acts as a dedicated forum where team members can review your code diffs, run automated integration tests (like the Markdown linter we configured!), leave comments, and suggest refinements.
4.  **Merge**: Once approved and all automated checks pass, the PR is merged into `main`, bringing your updates securely into production [1].

---

## 5. High-Value Learning Resource Shortlist
Keep these bookmarked as your go-to references for this module [2]:

*   **[Pro Git Book](https://git-scm.com/book/en/v2)** (Chapters 1-3): The canonical deep-dive on Git's internal architecture, snapshot mechanics, and branching models [2].
*   **[Learn Git Branching](https://learngitbranching.js.org/)**: A fantastic interactive game to visually master merging, rebasing, cherry-picking, and pointer movements [2].
*   **[Git Command Explorer](https://gitexplorer.com/)**: A useful reference UI to search and find the exact command string you need when troubleshooting [2].
*   **[Learn Git by Atlassian](https://www.atlassian.com/git)**: High-quality conceptual tutorials explaining merge conflicts and tracking models [2].
