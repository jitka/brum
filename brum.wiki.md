* ip adress `37.205.14.245`
* hostaname **zazvor**
```
ssh root@brum.wiki
```
heslo a virtuální konzole:
https://vpsadmin.vpsfree.cz/ -> vps -> id 

```
apt install git docker-compose vim
mkdir git && cd git
git clone git@github.com:jitka/brum.git
cd && rm -r .bashrc .gitconfig .vimrc
for i in bashrc gitconfig vimrc; do ln -s $HOME/git/brum/configs/.$i .$i; done
```

### homepage

[nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-debian-10)
```
vim /var/www/html/index.html
```
[letsencrypt](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/)
```
root@zazvor:~# rm /etc/nginx/sites-enabled/default
root@zazvor:~# cat /etc/nginx/conf.d/brum.wiki.conf
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    server_name brum.wiki www.brum.wiki;
}
root@zazvor:~# certbot --nginx --email jitka@ucw.cz -d brum.wiki -d www.brum.wiki

certbot certonly --agree-tos --email jitka@ucw.cz --webroot -w /var/lib/letsencrypt/ -d brum.wiki -d www.brum.wiki
```

### tiny-tiny-rss
[návod](https://git.tt-rss.org/fox/ttrss-docker-compose/src/static-dockerhub/README.md)
v env jsem měnila:
* postgre password 
* SELF_URL_PATH=http://37.205.14.245:8280/tt-rss
* HTTP_PORT=8280

```
docker-compose down && docker-compose up &
```
TODO [spouštění přes systemd](https://community.hetzner.com/tutorials/docker-compose-as-systemd-service)

v tuto chvílí běží [zde](http://37.205.14.245:8280/tt-rss/)

[nastavit ssl](https://git.tt-rss.org/fox/ttrss-docker-compose/wiki#using-ssl-with-letsencrypt)
přihlásit je jako `admin` `password`, změnit heslo, vytvořit uživatele `jitka`
