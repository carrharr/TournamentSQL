# TournamentSQL
Tournament SQL database and logic

INSTRUCTIONS /

Ensure your machine is running virtualbox, vagrant, and that PostgreSQL
and Python 2.7 are installed in the vagrant environment.

Vagrant conf is available at : https://www.udacity.com/wiki/ud088/vagrant

1.- Open a terminal and move TournamentSQL inside ~/fullstack-nanodegree-vm/vagrant/
2.- Once its in the folder execute "vagrant ssh" (First "vagrant up" if its not
    running)
3.- Inside vagrant do:
    $ cd /vagrant/TournamentSQL (GO TO FOLDER WHERE TOURNAMENT IS)
    $ psql                      (open PostgreSQL)
    $ \i tournament.sql         (execute database script)
    $ \q                        (quit psql)
4.- Your database is ready, open python to interact with it, then:
    $>>> from tournament import *
    $>>>
5.- At this stage you will enter the funtions you require, more info on them
    inside tournament.py.
'
