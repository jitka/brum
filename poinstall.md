# Ubuntu

### Prerekvizity
stáhnout aktuální iso
vyrobit flešku
nainstalovat
nastavit dvořáka
přihlásit se do firexu a githubu

https://github.com/jitka/brum/security
```
sudo apt update; sudo apt upgrade
```
```
snap youtube-music-desktop
```
* choose hostname ```hostnamectl set-hostname kren```
* add ssh-keygen && cat ~/.ssh/id_rsa.pub key to [github](https://github.com/settings/ssh/new)
* settings -> user -> fingerprint
* setting -> appereance -> dark

```
sudo apt install docker.io git tilix  ruby npm python-is-python3 httpie gnome-tweaks vim htop tldr datovka mc ack gimp mpv texlive

python3-virtualenvwrapper influxdb-client

mysql

steam
pycharm
slack
```

```
cd && rm -r .bashrc .gitconfig .vimrc .ideavimrc
for i in bashrc gitconfig vimrc ideavimrc; do ln -s $HOME/git/brum/config/$i .$i; done
```
