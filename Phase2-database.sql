-- SQLite
-- Database Systems Project 
-- Creation of database with tables
-- Sabrina Gonzalez & Jude Orsua 

create table Netflix(
    n_sid decimal(15,0) primary key,
    n_type char(32),
    n_title char(152),
    n_director char(152),
    n_cast char(152), 
    n_country char(152),
    n_added varchar(152),
    n_release integer(4),
    n_rating varchar(32),
    n_duration varchar(32),
    n_listed char(152),
    n_description char(152)
);

CREATE TABLE Movies (
    m_sid           decimal(15,0) not null,
    m_title         char(50) not null,
    m_cast          char(152) not null,
    m_description   char(152) not null
);

insert into Movies (m_sid, m_title, m_cast, m_description)
select n_sid, n_title, n_cast, n_description
from Netflix
where n_type = "Movie";

CREATE TABLE Shows (
    s_sid           decimal(15,0) not null,
    s_title         char(50) not null,
    s_cast          char(152) not null,
    s_description   char(152)
);

insert into Shows (s_sid, s_title, s_cast, s_description)
select n_sid, n_title, n_cast, n_description
from Netflix
where n_type = "TV Show";

CREATE TABLE ReleaseDate (
    re_sid          decimal(20,0) not null,
    re_release      decimal(20,0) not null,
    re_added        decimal(20,0) not null
);

insert into ReleaseDate (re_sid, re_release, re_added)
select n_sid, n_release, n_added
from Netflix;

create table Genre(
    g_sid decimal(20,0),
    g_genre char(50)
);

insert into Genre (g_sid, g_genre)
select n_sid, n_listed
from Netflix;

CREATE TABLE Rating (
    ra_sid          decimal(10,0) not null,
    ra_rating       char(8,0) not null,
    ra_stars        decimal(5,0) not null
);


CREATE TABLE Dislike (
    d_sid           decimal(9,0) not null,
    d_dislike       char(117) not null
);

CREATE TABLE LikeList (
    l_sid           decimal(9,0) not null,
    l_dislike       char(117) not null
);
 