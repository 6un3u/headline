CREATE TABLE PUB (pubId text, pub text);
CREATE TABLE TITLE (day date,  pubId text, title text, url text primary key);
CREATE VIEW headline AS SELECT TITLE.day, PUB.pub, TITLE.title, TITLE.url FROM TITLE join PUB using(pubId);
