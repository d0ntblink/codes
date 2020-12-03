#aliaes
alias ls='ls --color=always -rthla'
alias ll='ls -al'
alias install='apt-get install'
alias aptg='apt-get'

function apt-updater {
	apt-get update &&
	apt-get dist-upgrade -Vy &&
	apt-get autoremove -y &&
	apt-get autoclean &&
	apt-get clean &&
	reboot
	}

clear
figlet -f swampland "d0nt blink" | lolcat -a -d 1 -p 1 -F 0.2
