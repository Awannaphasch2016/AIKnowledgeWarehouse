:deb:apt:
* search for "deb" type files installed by apt
    * `grep -r --include '*.list' '^deb ' /etc/apt/sources.list /etc/apt/sources.list.d/`
