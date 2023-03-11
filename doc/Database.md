# Database Installation & Config

## MySQL

- [How To Install MySQL on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)

  ```bash
  sudo apt-get update
  sudo apt-get upgrade -y 
  sudo apt install mysql-server
  sudo mysql_secure_installation # 全选No
  ```
- 远程访问，需要修改下配置文件，binding 到 `0.0.0.0:3306`，再打开防火墙
- 重启服务，发现本地 root 账户不能登陆，可以参考[这里](https://blog.csdn.net/qq_34771403/article/details/73927962)
  - 先 su 到 root，然后 mysql，就可以登进去
  - 然后运行如下命令，重启服务

    ```sql
    mysql> update mysql.user set authentication_string=PASSWORD('newPwd'), plugin='mysql_native_password' where user='root';
    mysql> flush privileges;
    ```
- 此时再参考[这里](https://blog.csdn.net/leroy008/article/details/16116847)，令远程也能访问：`GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'newPwd' WITH GRANT OPTION;`
- phpmyadmin
  - `sudo apt-get install phpmyadmin`
  - 访问: `http://65.52.172.145/phpmyadmin/`

## PostGre

[参考](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

## Sqlite3
