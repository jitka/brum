ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIiR4PhPkO5jgxwSZtrm506wmyqn83riPCsWyk9vZ9/P jitka@ucw.cz
* ip adress `37.205.14.245`
* hostaname **zazvor**
```
ssh root@jitka.ucw.cz
```
heslo a virtuální konzole:
https://vpsadmin.vpsfree.cz/ -> vps -> id 

vypout ssh příhlašování heslem & vytvořit uživatele
```
apt install vim
root@zazvor:~ $ cat /etc/ssh/sshd_config 
PermitRootLogin yes
PasswordAuthentication no
root@zazvor12:~# systemctl restart sshd
adduser jitka
mkdir -p /home/jitka/.ssh && cp /root/.ssh/authorized_keys /home/jitka/.ssh/ && chmod 700 /home/jitka/.ssh && chmod 600 /home/jitka/.ssh/authorized_keys && chown -R jitka:jitka /home/jitka/.ssh
usermod -aG sudo jitka
locale-gen
update-locale LANG=en_US.UTF-8
```

```
sudo apt install git docker-compose nginx python3-certbot-nginx certbot wget
ssh-keygen -t ed25519 -C "jitka@ucw.cz"
cat ~/.ssh/id_ed25519.pub
mkdir git && cd git
git clone git@github.com:jitka/brum.git
cd && rm -r .bashrc .gitconfig .vimrc
for i in bashrc gitconfig vimrc; do ln -s $HOME/git/brum/config/$i .$i; done
```

## nginx / homepage

```
sudo certbot --nginx --email jitka@ucw.cz -d jitka.ucw.cz
sudo ln -s /home/jitka/git/brum/server/index.html /var/www/html/index.html
sudo ln -s /home/jitka/git/brum/server/jitka.ucw.cz.conf /etc/nginx/sites-avilable/jitka.ucw.cz.conf
sudo ln -s /home/jitka/git/brum/server/planka.jitka.ucw.cz.conf /etc/nginx/sites-available/planka.jitka.ucw.cz.conf
sudo ln -s /home/jitka/git/brum/server/home.jitka.ucw.cz.conf /etc/nginx/sites-available/home.jitka.ucw.cz.conf
sudo ln -s /etc/nginx/sites-available/jitka.ucw.cz.conf /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/planka.jitka.ucw.cz.conf /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/home.jitka.ucw.cz.conf /etc/nginx/sites-enabled/
sudo chmod o+x /home/jitka /home/jitka/git /home/jitka/git/brum /home/jitka/git/brum/server

sudo nginx -t
sudo tail -f /var/log/nginx/error.log
sudo service nginx restart
```

## docker / services

```
sudo usermod -aG docker $USER
# log out & log in
docker run hello-world
```

### planka

[planka docker-compose](https://docs.planka.cloud/docs/installation/docker/production_version)
```
mkcd services/planka
wget https://raw.githubusercontent.com/plankanban/planka/master/docker-compose.yml
# manual changes
docker-copmose up &
```


### tiny-tiny-rss
[návod](https://git.tt-rss.org/fox/ttrss-docker-compose/src/static-dockerhub/README.md)
v env jsem měnila:
* postgre password 
* SELF_URL_PATH=https://jitka.ucw.cz/tt-rss old: SELF_URL_PATH=http://37.205.14.245:8280/tt-rss
* HTTP_PORT=8280

```
docker-compose down && docker-compose up &
```
TODO [spouštění přes systemd](https://community.hetzner.com/tutorials/docker-compose-as-systemd-service)

v tuto chvílí běží [zde](http://37.205.14.245:8280/tt-rss/)

[nastavit ssl](https://git.tt-rss.org/fox/ttrss-docker-compose/wiki#using-ssl-with-letsencrypt)
[nastavit nginx](https://git.tt-rss.org/fox/ttrss-docker-compose/wiki#how-do-i-put-this-container-behind-a-reverse-proxy) v docker-compose zakomentovat `web` odkomentovat `web-nginx`, ta konfigurace patří do části server v `/etc/nginx/conf.d/jitka.ucw.cz.conf` 


přihlásit je jako `admin` `password`, změnit heslo, vytvořit uživatele `jitka`

### sync thing

### calibre
[official manual](https://manual.calibre-ebook.com/server.html#accessing-the-server-from-devices-on-your-home-network)

### home assitant tunel

* [nonexistent add ong with correct port settings](https://carly.be/expose-home-assistant-through-ssh-tunnel/)
* [general direct](https://community.home-assistant.io/t/ssh-tunneling-using-a-remote-server/318644)
* [fix-http proxy setting](https://community.home-assistant.io/t/home-assistant-400-bad-request-docker-proxy-solution/322163)

on haos
* sshkeygen -> copy to vpsfree admin sshkeys
```
ssh -N -R 8123:homeassistantlocalhost:8123 root@jitka.ucw.cz
```


```
echo "pokus" > index.html
python -m http.server 8080
ssh -N -R 44400:localhost:8080 homeassistant@jitka.ucw.cz
```

## samba

(source)[https://askubuntu.com/questions/781963/simple-samba-share-no-password]

```
sudu su
mkdir /data/
mkdir /data/nase
mkdir /data/video
sudo chown -R nobody.nogroup /data
sudo chown -R nobody.nogroup /data/nase
sudo chown -R nobody.nogroup /data/video
sudo chmod -R 777 /data/nase
sudo chmod -R 777 /data/video
```

### jekyll webs
[install](https://jekyllrb.com/docs/installation/ubuntu/)
