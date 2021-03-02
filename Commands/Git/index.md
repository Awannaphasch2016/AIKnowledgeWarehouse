:git:
* git checkout remote branch
    * ref
        * https://stackify.com/git-checkout-remote-branch/
    ```
    git fetch origin
    git checkout -track origin/xyz
    ```
:git:
* check if git repo is up to date 
* check if git repo needs pull
    * ref
        * https://stackoverflow.com/questions/3258243/check-if-pull-needed-in-git 
    ```
    git fetch <remote>
    git log HEAD..origin/main
    ```
