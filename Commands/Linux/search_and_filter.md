# NOTES
* rules of thumbs for using grep and find
    * use find + grep if you want to search for filenames
    * use grep if you want to search file's content

# SNIPPETS
:deb:apt:grep:find:
* search for "deb" type files installed by apt
    * `grep -r --include '*.list' '^deb ' /etc/apt/sources.list /etc/apt/sources.list.d/`


:find:grep:
* find filename in current directory with regex recursively
    * `find . -name "foo*"`
    * `find . | grep "foo*"`

 * split output of command by columns using Bash
    * :ps:grep:tr:cut:
        * eg
            * `ps | egrep 11383 | tr -s ' ' | cut -d ' ' -f 4`
    * :awk:
        * eg 
            * `echo "11383 pts/1    00:00:00 bash" | awk '{ print $4; }'`

