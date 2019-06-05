# HOW TO USE GIT

## Setting up Git!

Sets up your `user.name`.

```
git config --global user.name "%MY_NAME%"
```

Sets up your `user.email`.

```
git config --global user.email "%MY_EMAIL%"
```

Checks the `user.name` & `user.email`.

```
git config --global --list
```

## Commands

How do I clone a new repository onto my local workspace?

```
git clone https://github.com/%USER_NAME%/%REPO_NAME%.git
cd %REPO_NAME%
touch %SOME_FILE%
git add %SOME_FILE%
git commit -m "put your message here"
git push -u origin master
```

How do I add my local workspace onto a new repo?

```
Open up a terminal
Change directory to respective folder
git init
git remote add origin https://github.com/%USER_NAME%/%REPO_NAME%.git
git add .
git commit -m "put your message here"
git push -u origin master
```

How do I merge multiple repositories into one repository?

```
Create new repo on hosting platform (Github)
Open up a terminal
Change directory to respective folder
git remote -v
git remote add -f %OTHER_REPO% https://github.com/%USER_NAME%/%OTHER_REPO%.git
git merge -s ours --no-commit --allow-unrelated-histories %OTHER_REPO%/master
git read-tree --prefix=%OTHER_REPO%/ -u %OTHER_REPO%/master
git commit -m "Merge %OTHER_REPO% into %NEW_REPO%"
git push
```

What if I clone another repo into an existing repo?

```
Open up a terminal
Change directory to respective parent folder
git rm --cached %PATH/TO/CLONED/REPO%
git add .
git push
```

## Ignoring Files

Create a `.gitignore` file stating the specific folders and files you would like not to be tracked.

Be aware that files already on a repository online can not be "untracked" unless deleted or hidden away else where.

## Rebasing

If you only ever commit to your `master` branch, your directed acyclic graph (DAG) will look like this:

```
A ---> B ---> C ---> D [master]
```

...where A, B, C, and D are commits, and commit D is labeled as the `master` branch.

`Git` supports something called "branching", where you can do something like this:

```
A ---> B ---> C ---> D [master]
       \
        +----> X ---> Y ---> Z [experiment-1]
```

Here, what's happened is that after `commit B`, we made a branch called `experiment-1`. In this branch, we added `commits X, Y, and Z` which are completely independent from the commits that were added to the `master` branch.

(Perhaps we wanted to play around with an experimental and potentially risky feature without breaking any working code in the `master` branch? So that we, if experiment-1 is broken, we don't piss off our coworkers who would prefer to work with non-broken code).

What rebasing lets us do is take the graph that looks like the above, and make it look something like this:

```
A ---> B ---> C ---> D [master]
                      \
                       +----> X ---> Y ---> Z [experiment-1]
```

There are many potential applications to this (since git is a data structure, you can do arbitrarily complex/creative/nasty things to the underlying DAG), but the two usual use cases are when...

1. Somebody commits something really nice to the `master` branch (like a bug fix!) and you'd really like to have that in your work-in-progress.
2. You're happy with the results of your experiment, and want to add it to `master`, but don't want to do a merge, since that could look messy/you like having `master` be a straight line without splits.

More specifically, if you start from here:

```
A ---> B ---> C ---> D [master]
        \
         +----> X ---> Y ---> Z [experiment-1]
```

...and merge `experiment-1` into `master` and update the `master` branch, you'll end up with your DAG looking like this:

```
A ---> B ---> C ---> D -------> M [master]
        \                      /
         +----> X ---> Y ---> Z [experiment-1]
```

...where M is a new commit representing what happens when you combine diffs X, Y, and Z.

In contrast, if you rebase `experiment-1` into `master` and update the `master` branch, you'll end up with your DAG looking like this:

```
A ---> B ---> C ---> D
                      \
                       +----> X ---> Y ---> Z [experiment-1, master]
```

...which is exactly identical to this:

```
A ---> B ---> C ---> D ---> X ---> Y ---> Z [experiment-1, master]
```

So, if you'd prefer keeping an exact historical record, you might go with merges, but if you prefer keeping an idealized and clean historical record, you might go with rebasing.

## Technical Terms

Any terms above used are listed here.

```
Term Definition

--allow-unrelated-histories
        Provides ease of merge.
--no-commit
        Doesn't perform the commit as actions aren't finished yet.
--prefix
        Name of new file/folder.
-f
        Download objects and refs from another repo.
-m
        Message to be attached to commit.
-s
        Short output.
-u
        Update the files in the work tree with the result of the merge.
-v
        Be verbose and show remote url after name.
add %FILE_NAME%
        Add the said files.
add .
        Add all the files.
commit
        Changes are ready to be pushed.
init
        Makes a directory ready to work with git.
master
        The most important branch.
merge
        Combine branches into one branch.
origin
        Remote repo that a project was cloned from.
read-tree
        Reads tree info into the new repo index.
remote
        Manage the set of remotes whose branches you track.
```
