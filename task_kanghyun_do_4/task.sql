create table tbl_post(
    id bigint auto_increment primary key,
    title varchar(255) not null,
    body varchar(255) not null,
    user_id bigint not null,
    constraint fk_post_user foreign key(user_id)
                     references tbl_users(id)
);

create table tbl_users(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    username varchar(255) not null,
    email varchar(255) not null,
    phone varchar(255) not null,
    website varchar(255) not null
);

create table tbl_address(
    id bigint auto_increment primary key,
    street varchar(255) not null,
    suite varchar(255) not null,
    city varchar(255) not null,
    zipcode varchar(255) not null,
    user_id bigint not null,
    constraint fk_address_user foreign key(user_id)
    references tbl_users(id)
);


create table tbl_geo(
    id bigint auto_increment primary key,
    lat varchar(255) not null,
    lng varchar(255) not null,
    address_id bigint not null,
    constraint fk_geo_address foreign key(address_id)
    references tbl_address(id)
);


create table tbl_company(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    catchPhrase varchar(255) not null,
    bs varchar(255) not null,
    user_id bigint not null,
    constraint fk_company_user foreign key(user_id)
    references tbl_users(id)
);


select * from tbl_address;
select * from tbl_company;
select * from tbl_post;

select * from tbl_users;

