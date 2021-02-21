:Heroku:deploy:app:
* how to deploy app on Heroku?
    * ref
        * https://github.com/heroku/python-getting-started
    * running locally 
        * note:
            * see ref, I haven't yet try it myself
    * deploy to heroku
        ```
        $ make sure that you have done `git init`
        $ heroku create # (make sure that you haven't run the command already)
        $ git remote -v # ( should match name given by "heroku create")
        $ git add . | git commit -m "updated"
        $ git push heroku main (or git push heroku master)
        $ heroku run python mange.piy migrate 
        $ heroku open
        ```

