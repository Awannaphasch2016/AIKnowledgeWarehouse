:example:usecase:xargs:
* example usecase of xargs command
    * ref
        * https://shapeshed.com/unix-xargs/ 
    * how to print command that are executed
        ```
        echo 'one two three' | xargs -t echo
        ```
    * how to view command and prompt for execution
        ```
        echo 'one two tree' | xargs -p touch
        ```
    * how to run multiple command with xargs
        ```
            cat foo.txt
            one
            two
            three

            cat foo.txt | xargs -I % sh -c 'echo %; mkdir %'
            one 
            two
            three

            ls 
            one two three
        ```
