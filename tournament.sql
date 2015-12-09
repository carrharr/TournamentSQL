-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament

CREATE TABLE players (
  id SERIAL PRIMARY KEY  ,
  name varchar(88) NOT NULL ,
  bye boolean
);

CREATE TABLE matches (
  match_id SERIAL primary key ,
  --match_date date NOT NULL ,
  --match_start time NOT NULL ,
  --match_ends time NOT NULL,
  winner INT references players (id),
  loser INT references players (id),
  round INT,
  bye boolean
);

CREATE VIEW standings AS (
SELECT
players.id,
players.name,
count(match_winner.winner) AS wins,
count(match_winner.winner) + count(match_loser.loser) as matches_played
FROM players
LEFT JOIN matches match_winner ON players.id = match_winner.winner
LEFT JOIN matches match_loser ON players.id = match_loser.loser
GROUP BY players.id
);
