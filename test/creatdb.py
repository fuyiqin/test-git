create database TestDB;
show databases;

drop table <tablename>;
delete from car (where fram_id=)
alter table car_sub modify pos varchar(60)
alter table car change url URL(256)


create table FileMeta(DatasetName varchar(40),path varchar(256), Size int(20), N_Rows int(20),N_Columns int(20), Title varchar(100), Description text, Summary text, CreateTime datetime DEFAULT NULL, UpdateTime datetime DEFAULT NULL, DID varchar(40), Extension Varchar(100), PRIMARY KEY(DatasetName))DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;



create table filemeta(datasetname varchar(40),url varchar(256), sizeb int(20), nrows int(20),ncols int(20), Title varchar(100), Description text, Summary text, createtime datetime DEFAULT NULL, updatetime datetime DEFAULT NULL, DID varchar(40), Extension Varchar(100), PRIMARY KEY(DatasetName))DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;




create table datadictionary(did varchar(40),features text, Title varchar(40), Description text, Summary text, createtime datetime DEFAULT NULL, updatetime datetime DEFAULT NULL, Extension Varchar(100), PRIMARY KEY(DID))DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

show variables like 'character%';
 




delete from DataDictionary where DID='iris2';



/etc/mysql/my.conf
(1) client : default-character-set=utf8;
(2) mysql: default-character-set=utf8;
(3) mysqld: 
init_connect='SET collation_connection = utf8_unicode_ci'  
init_connect='SET NAMES utf8'  
character-set-server=utf8  
collation-server=utf8_unicode_ci  
skip-character-set-client-handshake  


 update  DataDictionary set Title='iris3',Description='the dataset';
update  DataDictionary set Title='iris3',Description='the dataset' where DID='iris2';



alter table filemeta  change  Url url varchar(256); #xiu gai field

alter table filemeta  modify  Url varchar(256);#xiu gai ron liang


                                                             ^
TEST=> CREATE TABLE filemeta (datasetname varchar(40),url varchar(256), sizeb int, nrows int,ncols int, Title varchar(100), Description text, Summary text, createtime timestamp, updatetime timestamp, DID varchar(40), Extension Varchar(100), PRIMARY KEY(DatasetName));
CREATE TABLE
TEST=> create table datadictionary(did varchar(40),features text, Title varchar(40), Description text, Summary text, createtime timestamp, updatetime timestamp, Extension Varchar(100), PRIMARY KEY(DID));




    # 创建新表
    CREATE TABLE user_tbl(name VARCHAR(20), signup_date DATE);

    # 插入数据
    INSERT INTO user_tbl(name, signup_date) VALUES('张三', '2013-12-22');

    # 选择记录
    SELECT * FROM user_tbl;

    # 更新数据
    UPDATE user_tbl set name = '李四' WHERE name = '张三';

    # 删除记录
    DELETE FROM user_tbl WHERE name = '李四' ;

    # 添加栏位
    ALTER TABLE user_tbl ADD email VARCHAR(40);

    # 更新结构
    ALTER TABLE user_tbl ALTER COLUMN signup_date SET NOT NULL;

    # 更名栏位
    ALTER TABLE user_tbl RENAME COLUMN signup_date TO signup;

    # 删除栏位
    ALTER TABLE user_tbl DROP COLUMN email;

    # 表格更名
    ALTER TABLE user_tbl RENAME TO backup_tbl;

    # 删除表格
    DROP TABLE IF EXISTS backup_tbl;





        \h：查看SQL命令的解释，比如\h select。
        \?：查看psql命令列表。
        \l：列出所有数据库。
        \c [database_name]：连接其他数据库。
        \d：列出当前数据库的所有表格。
        \d [table_name]：列出某一张表格的结构。
        \du：列出所有用户。
        \e：打开文本编辑器。
        \conninfo：列出当前数据库和连接的信息。






第二种方法，使用shell命令行。

添加新用户和新数据库，除了在PostgreSQL控制台内，还可以在shell命令行下完成。这是因为PostgreSQL提供了命令行程序createuser和createdb。还是以新建用户dbuser和数据库exampledb为例。

首先，创建数据库用户dbuser，并指定其为超级用户。

    sudo -u postgres createuser --superuser dbuser

然后，登录数据库控制台，设置dbuser用户的密码，完成后退出控制台。

    su postgres
     psql

    \password dbuser

    \q

接着，在shell命令行下，创建数据库exampledb，并指定所有者为dbuser。

    sudo -u postgres createdb -O dbuser exampledb

三、登录数据库

添加新用户和新数据库以后，就要以新用户的名义登录数据库，这时使用的是psql命令。

    psql -U dbuser -d exampledb -h 127.0.0.1 -p 5432

上面命令的参数含义如下：-U指定用户，-d指定数据库，-h指定服务器，-p指定端口。



