create table tbl_Album(
    id bigint auto_increment primary key,
    user_id bigint not null,
    title varchar(255) not null
);

create table tbl_photos(
    id          bigint auto_increment primary key,
    title       varchar(255) not null,
    url         varchar(255) not null,
    thumbnaiUrl varchar(255) not null,
    Album_id bigint not null,
    constraint fk_photos_Album foreign key(Album_id)
        references tbl_album (id)
);

select * from tbl_photos;
