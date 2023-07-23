* ip adress `37.205.14.245`
* hostaname **zazvor**
```
ssh root@jitka.ucw.cz
```
heslo a virtuální konzole:
https://vpsadmin.vpsfree.cz/ -> vps -> id 

vypout ssh příhlašování heslem
```
root@zazvor:~ $ cat /etc/ssh/sshd_config 
X11Forwarding yes
AllowAgentForwarding yes
PermitRootLogin yes
PasswordAuthentication no
```


```
apt install git docker-compose vim
mkdir git && cd git
git clone git@github.com:jitka/brum.git
cd && rm -r .bashrc .gitconfig .vimrc
for i in bashrc gitconfig vimrc; do ln -s $HOME/git/brum/configs/.$i .$i; done
```

link nginx configuratin
```
ln -s /root/git/brum/config/jitka.ucw.cz.conf /etc/nginx/conf.d/jitka.ucw.cz.conf 
```
### homepage

[nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-debian-10)
```
vim /var/www/html/index.html
```
[letsencrypt](https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/)
```
root@zazvor:~# rm /etc/nginx/sites-enabled/default
root@zazvor:~# cat /etc/nginx/conf.d/jitka.ucw.cz.conf
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    server_name jitka.ucw.cz www.jitka.ucw.cz;
}
root@zazvor:~# certbot --nginx --email jitka@ucw.cz -d jitka.ucw.cz
```
#### přesměrování z http -> https
```
root@zazvor:~ $ cat /etc/nginx/conf.d/jitka.ucw.cz.conf 
server {
    listen 80;

    server_name jitka.ucw.cz www.jitka.ucw.cz;
    return 301 https://jitka.ucw.cz$request_uri;
}

server {

    root /var/www/html;
    server_name jitka.ucw.cz www.jitka.ucw.cz;

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/jitka.ucw.cz/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/jitka.ucw.cz/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    location /tt-rss/ {
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $remote_addr;
          proxy_set_header X-Forwarded-Proto $scheme;

          proxy_pass http://127.0.0.1:8280/tt-rss/;
          break;
    }
}
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

### home assitant port fowarding

on haos
```
ssh -N -R 44400:localhost:8123 homeassistant@jitka.ucw.cz
```

on haos for test to test

```
echo "pokus" > index.html
python -m http.server 8080
ssh -N -R 44400:localhost:8080 homeassistant@jitka.ucw.cz
```
