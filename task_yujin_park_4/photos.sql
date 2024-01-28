create table tbl_users(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    username varchar(255) not null,
    email varchar(255) not null,
    phone varchar(255) not null,
    website varchar(255) not null
);

create table tbl_album(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    users_id bigint not null,
    constraint fk_album_users foreign key (users_id)
    references tbl_users(id)

);

create table tbl_photos(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    url varchar(255) not null,
    thumbnail_url varchar(255) not null,
    album_id bigint not null,
    constraint fk_photos_album foreign key(album_id)
    references tbl_album (id)
);

select * from tbl_users;