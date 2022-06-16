# Git practices

Git practices concerning branching, merging and devops strategies.

## This repository strategies

Branching model:

* `master` - production/release tagged branch ready to be deployed/delivered at any time - a stable version;

* `dev` - the primary trunk of development, giving rise to every branches: features, hotfixes and so forth.

The `dev` trunk consists of so-called thematic branches:
* `core` - Python interpreter environment;
* `cli` - command line interface;
* `gui` - graphic user interface.

**Note**: you are not discouraged to create any other branches if necessary  - the `dev` is just for this purpose. *If the model increasingly does not fit into needs of the project, change the former and don't forget to document a new one.*

A rule of thumb: commits merged into `master` should obey 2 (two) points:
1. the commits come only from `dev`;
2. every commit into `master` counts as a new release and should be tagged. 

## References

* Git Flow Atlassian:
	* en - https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow;
	* ru - https://www.atlassian.com/ru/git/tutorials/comparing-workflows/gitflow-workflow;

* https://www.gitkraken.com/learn/git/best-practices/git-branch-strategy;

* a successful git branching model:
	* en - https://nvie.com/posts/a-successful-git-branching-model/;
	* ru - https://habr.com/ru/post/106912.
