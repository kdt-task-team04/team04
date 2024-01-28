use test;

create table tbl_albums(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    user_id bigint not null,
    constraint fk_albums_user foreign key(user_id)
                     references tbl_user(id)
);

create table tbl_user(
    id bigint auto_increment primary key
);

select * from tbl_albums;

