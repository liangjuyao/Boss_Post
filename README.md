# Boss-Post

## 介绍
 使用selenium自动化获取Boss直聘的首页[互联网/AI](https://www.zhipin.com/?city=100010000&ka=city-sites-100010000)标签的数据并遍历点击获取岗位详细信息保存数据库
<img src="https://github.com/liangjuyao/Boss_Post/blob/master/statis/%E4%BA%92%E8%81%94%E7%BD%91.jpg">
## 使用
1、安装依赖
```python
pip install -r requirements.txt
```

2、Boss文件夹下Boss.py修改main()
```mysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='798lhh', database='BossDB')
```
|     字段     |               含义               |                                 更改                             |
| :----------: | :----------------------------------: | :--------------------------------------------------------------: |
|  user |           账号             |                   自己数据库账号              |
|  password |           密码             |                   自己数据库密码              |
|  database |           数据库名称             |                   自己数据库名称              |


3、在135行找到下面sql，然后修改post, post是表名，改为你自己的
```mysql
sql = '''insert into post(category, sub_category,job_title,province,job_location,job_company,job_industry,job_finance,job_scale,job_welfare,job_salary_range,job_experience,job_education,job_skills,create_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
```

4、SQL语句创建
```mysql
create database BossDB;
use BossDB;

create table BossDB.post
(
    category         varchar(255) null ,
    sub_category     varchar(255) null ,
    job_title        varchar(255) null ,
    province         varchar(100) null ,
    job_location     varchar(255) null ,
    job_company      varchar(255) null ,
    job_industry     varchar(255) null ,
    job_finance      varchar(255) null ,
    job_scale        varchar(255) null ,
    job_welfare      varchar(255) null ,
    job_salary_range varchar(255) null ,
    job_experience   varchar(255) null ,
    job_education    varchar(255) null ,
    job_skills       varchar(255) null ,
    create_time      varchar(50)  null 
);
```
