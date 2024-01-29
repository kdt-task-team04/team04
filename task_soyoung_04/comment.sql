create table tbl_users(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    username varchar(255) not null,
    email varchar(255) not null,
    phone varchar(255) not null,
    website varchar(255) not null
);


create table tbl_post(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    body varchar(255) not null,
    user_id bigint not null,
    constraint fk_post_user foreign key(user_id)
                     references tbl_users(id)
);

create table tbl_comment(
    id bigint auto_increment primary key,
    post_id bigint not null,
    name varchar(255) not null,
    email varchar(255) not null,
    content varchar(255) not null,
    constraint fk_comment_post foreign key(post_id)
                        references tbl_post(id)
);


select * from tbl_users;
select * from tbl_post;
select * from tbl_comment;

create database comments;

use comments;