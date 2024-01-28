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

insert into tbl_users (name, username, email, phone, website)
values ("Kurtis Weissnat", "Elwyn.Skiles", "Telly.Hoeger@billy.biz", "210.067.6132", "elvis.io");

insert into tbl_address (street, suite, city, zipcode, user_id)
values ("Rex Trail","Suite 280","Howemouth","58804-1099", 7);

insert into tbl_geo (lat, lng, address_id)
values ("24.8918", "21.8984", 7);

insert into tbl_company (name, catchPhrase, bs, user_id)
values ("Johns Group", "Configurable multimedia task-force", "generate enterprise e-tailers", 7);

###
insert into tbl_users (name, username, email, phone, website)
values ("Patricia Lebsack", "Karianne", "Julianne.OConner@kory.org", "493-170-9623 x156", "kale.biz");

insert into tbl_address (street, suite, city, zipcode, user_id)
values ("Hoeger Mall", "Apt. 692", "South Elvis", "53919-4257", 4);

insert into tbl_geo (lat, lng, address_id)
values ("29.4572", "-164.2990", 4);

insert into tbl_company (name, catchPhrase, bs, user_id)
values ("Robel-Corkery", "Multi-tiered zero tolerance productivity", "transition cutting-edge web services", 4);

###
insert into tbl_users (name, username, email, phone, website)
values ("Chelsey Dietrich", "Kamren", "Lucio_Hettinger@annie.ca", "(254)954-1289", "demarco.info");

insert into tbl_address (street, suite, city, zipcode, user_id)
values ("Skiles Walks","Suite 351", "Roscoeview", "33263", 5);

insert into tbl_geo (lat, lng, address_id)
values ("-31.8129", "62.5342", 5);

insert into tbl_company (name, catchPhrase, bs, user_id)
values ("Keebler LLC","User-centric fault-tolerant solution","revolutionize end-to-end systems", 5);

select * from tbl_address;
select * from tbl_company;
select * from tbl_users;


