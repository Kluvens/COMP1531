to effectively work on large projects, we need:
  - version control: tracks changes to our code
  - concurrent programming: multiple people to work on the same files at the same time
Git is a version control tool that enables to people to work concurrently on the same codebase.
Git is a distributed version control software.

Git - Single Machine
Stage 1. version control on a single machine
Getting setup: SSH keys, git clone
Status of work: git status, git log
Doing work: git add, git diff, git commit, git push

Git - Multiple of your machines
Stage 2. version control across multiple of your machines
Multiple machines: git pull, merge conflicts

A branch essentially is just a pointer to a particular commit.
You can create your own branch if you want to continue on a separate thread of working, unrelated to the master branch.
In most industries, you cannot merge your branch into master via the command line. Instead, we allow our git site (e.g. gitlab) to do this via a Merge Request

git add .
git commit -m "more updates on this function"
git push
git fetch (This Git command will get all the updates from the remote repository, including new branches.)
git fetch origin master
git pull
git pull origin master
git clone gitlab@gitlab.cse.unsw.EDU.AU:COMP1531/22T1/groups/F13B_BADGER/project-backend.git
git checkout -b new_branch_name
git checkout (You can use the checkout command to switch the branch that you are currently working on.)
git diff (You can use this command to see the unstaged changes on the current branch. Here’s an example of a branch with an edited feature file)
git status
git branch
git branch -d branch_name (to delete a branch)
git merge master (The merge command let's you specify the branch you want merged into your current branch. Merge from master to your branch)
