alias subl="open -a /Applications/Sublime\ Text.app"
alias ll="ls -l"
alias python="python3"
alias pip="pip3"
alias grep="grep --color=auto"

export PS1="${debian_chroot:+($debian_chroot)}\[\\033[01;34m\]\u@\h\[\033[00m\]:\[\033;34m\]\W\[\033[00m\]"

#Git stuff
function git-current-branch {
	git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

#Terminal openning >>
export PS1="$PS1\[\033[01;32m\]\$(git-current-branch)\[\033[00m\]\$ "
#export PS1="neha~$ "

#color
export CLICOLOR=1

#Environment variables
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
export PATH=/opt/apache-maven-3.5.4/bin:$PATH
#export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home:$JAVA_HOME

