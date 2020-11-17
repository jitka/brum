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
[appache](https://linuxize.com/post/how-to-install-apache-on-debian-10/) část o firewal ignoruju
```
vim /var/www/html/index.html
```
[letsencrypt](https://linuxize.com/post/secure-apache-with-let-s-encrypt-on-debian-10/)
```
certbot certonly --agree-tos --email jitka@ucw.cz --webroot -w /var/lib/letsencrypt/ -d brum.wiki -d www.brum.wiki
```
`vim /etc/apache2/sites-available/brum.wiki.conf`
```
<VirtualHost *:80> 
  ServerName brum.wiki
  ServerAlias www.brum.wiki

  Redirect permanent / https://brum.wiki/
</VirtualHost>

<VirtualHost *:443>
  ServerName brum.wiki
  ServerAlias www.brum.wiki

  Protocols h2 http/1.1

  <If "%{HTTP_HOST} == 'www.brum.wiki'">
    Redirect permanent / https://brum.wiki/
  </If>

  DocumentRoot /var/www/brum.wiki/public_html
  ErrorLog ${APACHE_LOG_DIR}/brum.wiki-error.log
  CustomLog ${APACHE_LOG_DIR}/brum.wiki-access.log combined

  SSLEngine On
  SSLCertificateFile /etc/letsencrypt/live/brum.wiki/fullchain.pem
  SSLCertificateKeyFile /etc/letsencrypt/live/brum.wiki/privkey.pem

  # Other Apache Configuration

</VirtualHost>
```

[nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-debian-10)

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
