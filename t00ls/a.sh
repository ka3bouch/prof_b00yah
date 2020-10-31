
#!/bin/bash
name=36
#export name=$(($name+1))
fonc_init(){
	bacck=$(pwd)
	rm -rf ~/.mozilla
	rm -rf /tmp/*
	wget -q https://github.com/ka3bouch/prof_b00yah/raw/master/muz_prof/default.tar.bz2
	tar xf default.tar.bz2 -C ~/
	cd ~/
	pwd 
	cd $bacck
	pwd
}

fonc_init
python3 p.py
#firefox --start-debugger-server 6000  https://booyah.live/channels/10919460

tar -jcvf $name.tar.bz2 ~/.mozilla && cp $name.tar.bz2 ~/noVNC/
#rm -rf ~/.mozilla

