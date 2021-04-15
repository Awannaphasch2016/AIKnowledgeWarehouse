:git:
* git checkout remote branch
    * refg
        * https://stackify.com/git-checkout-remote-branch/
    ```
    git fetch origin
    git checkout -track origin/xyz
    ```
:git:git pull:
* check if git repo is up to date 
* check if git repo needs pull
    * ref
        * https://stackoverflow.com/questions/3258243/check-if-pull-needed-in-git 
    ```
    git fetch <remote>
    git log HEAD..origin/main
    ```
:git:pull:commit:fetch:remote:branch:
* how to see code changes after git pull?
    * requirement 
        * before you pull
         ```
         git fetch
         git log --name-status origin/master..
        ```
            * Will show you what commits you are about to retrieve, along with the names of the files
    * `git log --name-status -2`
        * will show you the names of the files that changed for the last two commits
    * `git log -p -2` 
        * Will show you the changes themselves. 

:git:commit:remote:
* compare Commit differences between local and remote
    * ref
        * https://stackoverflow.com/questions/7057950/commit-differences-between-local-and-remote
    ```
    git fetch
    git log master..origin/master
    ```
