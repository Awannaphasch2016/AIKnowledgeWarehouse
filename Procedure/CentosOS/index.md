:instruction:setup:root:sudo:CentosOS:Ubuntu
* how to install package to without sudo root priviledge?  
    * reference
        * stackoverflow
            * https://unix.stackexchange.com/questions/16375/keeping-track-of-programs?noredirect=1&lq=1
    1. compile and install into ~/bin (edit your .bashrc to set the PATH to include it).
        * libraries can be compiled and installed into ~/lib (set LD_LIBRARY_PATH to point to it), and
         developement headers can be installed into e.g. ~/includes.
    2. depending on the specific details of the progrms you want to install and the library they depend upon,
     you can download the .deb files and use 'dpkg-deb -x' to extract them underneath your home directoyr. You will then have a lot of "fun" setting the PATH LD-LIBRARY_PATH, and other variables. 
        * The more complex the program or app you're installing the more fun you'll be up for. 
        * you will not be able to install setuid binaries this ways they'll install but (since you don't hae permission to chown them to root or set the estuid bit on them) they'll just be 
         normal binaries owned by your.
        * daemons and system service that expect to be runnig as a certain UID or have the ability to change uid, or expect files to be int /etc rather ~/etc and so on aren't likely to work 
         well, if at all
    3. Most sysadmins would ocnsider mc and mcedit to be 'mostly harmless', innocuous program
        * however, very few would consider installing a torrent client to be harmless, especially if they have to pay for bandwidth or endup being legally liable. Most sysadmins would 
          probably not be netirely happey for end-users to be installing such sofware without permissiong
            * in this case, you should always ask
    * Examples
        * process should loook like the following for Ubuntu
        ```
        apt-get source PACKAGE
        ./configure --prefix=$HOME/myapps
        make
        make install
        ```
    


