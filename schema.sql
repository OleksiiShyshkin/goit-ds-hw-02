pragma foreign_keys = on;

drop table if exists users;

create table users (
    id integer primary key autoincrement,
    fullname varchar(100) not null,
    email varchar(100) not null unique
);

drop table if exists status;

create table status (
    id integer primary key autoincrement,
    name varchar(50) not null unique
);

drop table if exists tasks;

create table tasks (
    id integer primary key autoincrement,
    title varchar(100) not null,
    description text,
    status_id integer not null,
    user_id integer not null,
    foreign key (status_id) references status(id),
    foreign key (user_id) references users(id) on delete cascade
);