create table tbl_post(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    body varchar(255) not null,
    user_id bigint not null,
    constraint fk_post_user foreign key(user_id)
                     references tbl_user(id)
);

create table tbl_user(
    id bigint auto_increment primary key
);



