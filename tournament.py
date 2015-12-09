#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import contextlib


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

@contextlib.contextmanager
def myCursor():
    """Function to consolidate db transaction code."""
    conn = connect()
    cursor = conn.cursor()
    try:
        yield cursor
    except:
        print("Database Cursor Error")
    else:
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def deleteMatches():
    """Remove all the match records from the database."""
    with myCursor() as cursor:
        query = "DELETE FROM matches;"
        cursor.execute(query)


def deletePlayers():
    """Remove all the player records from the database."""
    with myCursor() as cursor:
        query = "DELETE FROM players;"
        cursor.execute(query)

def countPlayers():
    """Returns the number of players currently registered."""
    with myCursor() as cursor:
        query = "SELECT count(players.id) FROM players ;"
        cursor.execute(query)
        result = cursor.fetchone()
        count = result[0]
        return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    with myCursor() as cursor:
        query = "INSERT INTO players (name) VALUES (%s);"
        parameters = (name,)
        cursor.execute(query, parameters)

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    with myCursor() as cursor:
        query = "SELECT id, name, wins, matches_played FROM standings;"
        cursor.execute(query)
        standings = cursor.fetchall()
        return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    with myCursor() as cursor:
        query = "INSERT INTO matches (winner, loser) values (%s, %s) SET round = round +1;"
        parameters = (winner, loser)
        cursor.execute(query, parameters)

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    with myCursor() as cursor:
        query = ""
        parameters= ""
        cursor.execute(query, parameters)
