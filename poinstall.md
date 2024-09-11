# Ubuntu

### Prerekvizity
stáhnout aktuální iso
vyrobit flešku
nainstalovat
nastavit dvořáka
přihlásit se do firexu a githubu


```
git clone root@jitka.ucw.cz:git/private.git
git clone git@github.com:jitka/brum.git
```

```
sudo apt update; sudo apt upgrade
```
```
snap install --edge youtube-music
sudo snap install pycharm-community --classic
```
* choose hostname ```hostnamectl set-hostname kren```
* add ssh-keygen && cat ~/.ssh/id_rsa.pub key to [github](https://github.com/settings/ssh/new)
* settings -> user -> fingerprint
* setting -> appereance -> dark

```
sudo apt install docker.io git tilix ruby npm python-is-python3 httpie gnome-tweaks vim htop tldr mc ack gimp mpv gdebi curl

python3-virtualenvwrapper influxdb-client

mysql

steam
pycharm
slack
```

```
cd && rm -r .bashrc .gitconfig .vimrc .ideavimrc
for i in bashrc gitconfig vimrc ideavimrc; do ln -s $HOME/git/brum/config/$i .$i; done
mkdir ~/.config/nvim && ln -s $HOME/git/brum/config/vimrc ~/.config/nvim/init.vim
```

### Syncthing
```
sudo ln -s $HOME/git/brum/config/syncthing@.service /etc/systemd/system/syncthing@.service
sudo su
systemctl daemon-reload
systemctl start syncthing@root
systemctl enable syncthing@root
```

### Tilix

https://github.com/gnunn1/tilix/issues/571

```
dconf load /com/gexperts/Tilix/ < ~/git/brum/config/tilix.dconf
```

### Docker

```
sudo usermod -aG docker ${USER}
su - ${USER}
docker run hello-world
```

### Prusa
```
ln -s ~/git/private/prusa/env ~/git/Prusa-Connect-API/env
```

