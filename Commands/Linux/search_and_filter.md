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

:awk:example: 
* ref
    * https://stackoverflow.com/questions/6284560/how-to-split-a-variable-by-a-special-character/6284596
    * https://www.gnu.org/software/gawk/manual/html_node/Using-BEGIN_002fEND.html

* split input text by 'x'
    * `echo 1920x1080 | awk -F"x" '{print $1, $2}'`
* split input text from a line 
    * `echo '$2 = 1920x1080' | awk -F"x" 'sub(/\$[0-9] += +/, "", $1){print $1, $2}'`
* `awk '(PATTERN1){...print something..} (PATTERN2){..print something..}`
* `awk 'PATTERN1{...print something..} PATTERN2{..print something..}`
    * awk:terminology:example:
    * note
        * for each line, if PATTERNN is matched, command in {} will be executed.
    * terminology 
        * syntax 
            * `awk 'NR==1{print}' [FILE]` 
            * `awk 'NR==1' [FILE]` 
                * note
                    * for line 1, print whole line 
            * `awk 'NR==1{}' [FILE]`
                * note
                    * for line 1, {} = don't do anything 
            * `awk 'NR==1{print} {print}' [FILE]` 
                * note
                    * {} without condition is the same as condition always set to True.
                    * for eaech line, each condition will be read 1 time
                        * so this example line 1 will be printed 2 times while the rest of the line 
                            will be printed 1 time.
            * `awk '($0 ~ /e$/){print $0}' [FILE]`
            * `awk '$0 ~ /e$/{print $0}' [FILE]`
            * `awk '/e$/{print $0}' [FILE]`
                * :awk:regex:example:terminology
                * note 
                    * print line if first value ends with e.
                    * ~ indicate that if statement of the rigth is matched, condition will be true.
                    * /\<\>/ is regex

:display:imagemagick:picture:
* open list of picture using display command.
    * `ls | grep "._rate_of_change.png" | xargs -n1 display` 


