#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'
sudo yum -y install tcl 

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
       SCRIPTPATH=/vagrant
   fi
  
  mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
 ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS

echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros

cd $HOME/rpmbuild/SOURCES
wget http://download.redis.io/releases/redis-3.0.7.tar.gz
