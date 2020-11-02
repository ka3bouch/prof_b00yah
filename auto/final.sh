#!/bin/bash
name=$2
#export name=$(($name+1))
git config --global user.email "ka3bouch@protonmail.com"
cat <<EOF > ~/.netrc
machine github.com
login ka3bouch
password agoon007A*

EOF



nick=$name
echo $nick
git_commit () {
   bz2_path=~/noVNC/$nick.tar.bz2
   echo "TRANSFER TO GIT " $bz2_path 
   echo 'GO TO TMP'
   cd /tmp
   #pwd && ls -al
   git clone -q "https://github.com/ka3bouch/prof_b00yah.git" && cd prof_b00yah
   ls *
   cd new_prof/ && ls
   mv -f $bz2_path ./
   git add --all .
   git commit -m "sed comlmit"
   git push origin master
   rm -rf /tmp/prof_b00yah
}




fonc_init(){
   bacck=$(pwd)
   rm -rf ~/.mozilla
   rm -rf /tmp/*
   wget -q https://github.com/ka3bouch/prof_b00yah/raw/master/muz_prof/tst3.tar.bz2
   tar xf tst3.tar.bz2 -C ~/
   cd ~/
   pwd 
   cd $bacck
   pwd
}

fonc_init
python3 p.py $1
cd ~/
tar -jcf $name.tar.bz2 .mozilla && cp $name.tar.bz2 ~/noVNC/
#MUV THE NEW PROFILE TO NOVNC PATH 
git_commit $nick
cd ~/
tar -jcf after.tar.bz2 .mozilla && cp after.tar.bz2 ~/noVNC/
#rm -rf ~/.mozilla
#firefox --start-debugger-server 6000  https://booyah.live/channels/10919460
