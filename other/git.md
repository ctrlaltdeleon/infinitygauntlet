# GIT

Contains all git workflows and the variance.

## Setting up git

```
git config --global --list
```

- Checks the user.name & user.email
- To access config, go to 'Users' then look for '.gitconfig'

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

## Technical Terms

Any terms above used are listed here.

```
Term                            Definition

--allow-unrelated-histories     Provides ease of merge
--no-commit                     Doesn't perform the commit as actions aren't finished yet
--prefix                        Name of new file/folder
-f                              Download objects and refs from another repo
-m                              Message to be attached to commit
-s                              Short output
-u                              Update the files in the work tree with the result of the merge
-v                              Be verbose and show remote url after name
add                             Add the said files
add .                           Add all the files
commit                          Changes are ready to be pushed
init                            Makes a directory ready to work with git
master                          The most important branch
merge                           Combine branches into one branch
origin                          Remote repo that a project was cloned from
read-tree                       Reads tree info into the new repo index
remote                          Manage the set of remotes whose branches you track
```
