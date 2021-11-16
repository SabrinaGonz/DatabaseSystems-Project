-- SQLite
-- Database Systems Project 
-- Creation of database with tables
-- Sabrina Gonzalez & Jude Orsua 


CREATE TABLE Movies (
    m_sid           decimal(15,0) not null,
    m_title         char(50) not null,
    m_cast          char(152) not null,
    m_description   char(152) not null
);
CREATE TABLE Shows (
    s_sid           decimal(15,0) not null,
    s_title         char(50) not null,
    s_cast          char(152) not null,
    s_description   char(152)
);
CREATE TABLE Release (
    re_sid          decimal(20,0) not null,
    re_release      decimal(20,0) not null,
    re_added        decimal(20,0) not null
);
CREATE TABLE Genre (
    g_sid           decimal(20,0) not null,
    g_genre         char(50) not null,
);
CREATE TABLE Rating (
    ra_sid          decimal(10,0) not null,
    ra_rating       char(8,0) not null,
    ra_stars        decimal(5,0) not null
);
CREATE TABLE Dislike (
    d_sid           decimal(9,0) not null,
    d_dislike       char(117) not null
);
CREATE TABLE Link (
    l_sid           decimal(9,0) not null,
    l_dislike       char(117) not null
);