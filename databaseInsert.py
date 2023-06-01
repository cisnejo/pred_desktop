import json
import os
import importlib.resources as pkg_resources
import sys
import mysql.connector
from dotenv import load_dotenv
import urllib.parse
import urllib.request
import requests
from datetime import datetime
import time

# Parse the JSON object
# Parse JSON data

import json


# Connect to the database
def DatabaseInsert(json_response):
    load_dotenv()

    MYSQL_PW = os.getenv("MYSQL_PW")
    for data in json_response:
        db = mysql.connector.connect(
            host="127.0.0.1", user="root", password=MYSQL_PW, database="pred"
        )
        cursor = db.cursor()
        query = "SELECT * FROM MATCHDATA WHERE matchId = %s"
        cursor.execute(query, (data["matchId"],))

        result = cursor.fetchone()
        if result:
            continue
        match_timestamp = None
        match_namespace = None
        match_sessionid = None
        
        if "Timestamp" in data:
            match_timestamp = data["Timestamp"]
        if "Namespace" in data:
            match_namespace = data["Namespace"]
        if "SessionID" in data:
            match_sessionid = data["SessionID"]

        matchdata_query = "INSERT INTO MATCHDATA (server, gameDuration, winningTeam, Timestamp, Namespace, matchId, startTime, endTime, gameMode, region, matchEndReason, sessionId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        matchdata_values = (
            data["server"],
            data["gameDuration"],
            data["winningTeam"],
            match_timestamp,
            match_namespace,
            data["matchId"],
            data["startTime"],
            data["endTime"],
            data["gameMode"],
            data["region"],
            data["matchEndReason"],
            match_sessionid,
        )
        cursor.execute(matchdata_query, matchdata_values)
        matchdata_id = cursor.lastrowid
        db.commit()

        for player in data["playerData"]:
            playerdata_query = "INSERT INTO PLAYERMATCHDATA (playerId, teamId, playerName, roleName, heroName, gameId ) VALUES (%s, %s, %s, %s, %s, %s)"
            playerdata_values = (
                player["playerId"],
                player["teamId"],
                player["playerName"],
                player["roleName"],
                player["heroName"],
                matchdata_id,
            )
            cursor.execute(playerdata_query, playerdata_values)
            playermatch_id = cursor.lastrowid
            # ------------------------------------------
            damagehealdata = player["damageHealData"]
            dmghealdata_query = "INSERT INTO DAMAGEHEALDATA (magicalDamageTakenFromHeroes, totalHealingDone, crestHealingDone, totalDamageTakenFromHeroes, physicalDamageTakenFromHeroes, physicalDamageTaken, totalDamageDealtToHeroes,magicalDamageDealtToHeroes ,totalDamageDealtToStructures ,trueDamageTakenFromHeroes ,totalDamageDealtToObjectives , trueDamageTaken,totalShieldingReceived,magicalDamageDealt,totalDamageTaken,totalDamageMitigated,trueDamageDealtToHeroes,largestCriticalStrike,physicalDamageDealt,utilityHealingDone,trueDamageDealt,itemHealingDone,totalDamageDealt,magicalDamageTaken,physicalDamageDealtToHeroes,playermatchId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"
            dmghealdata_values = (
                damagehealdata["magicalDamageTakenFromHeroes"],
                damagehealdata["totalHealingDone"],
                damagehealdata["crestHealingDone"],
                damagehealdata["totalDamageTakenFromHeroes"],
                damagehealdata["physicalDamageTakenFromHeroes"],
                damagehealdata["physicalDamageTaken"],
                damagehealdata["totalDamageDealtToHeroes"],
                damagehealdata["magicalDamageDealtToHeroes"],
                damagehealdata["totalDamageDealtToStructures"],
                damagehealdata["trueDamageTakenFromHeroes"],
                damagehealdata["totalDamageDealtToObjectives"],
                damagehealdata["trueDamageTaken"],
                damagehealdata["totalShieldingReceived"],
                damagehealdata["magicalDamageDealt"],
                damagehealdata["totalDamageTaken"],
                damagehealdata["totalDamageMitigated"],
                damagehealdata["trueDamageDealtToHeroes"],
                damagehealdata["largestCriticalStrike"],
                damagehealdata["physicalDamageDealt"],
                damagehealdata["utilityHealingDone"],
                damagehealdata["trueDamageDealt"],
                damagehealdata["itemHealingDone"],
                damagehealdata["totalDamageDealt"],
                damagehealdata["magicalDamageTaken"],
                damagehealdata["physicalDamageDealtToHeroes"],
                playermatch_id,
            )
            cursor.execute(dmghealdata_query, dmghealdata_values)
            db.commit()
            # ------------------------------------------
            incomedata = player["incomeData"]
            incomedata_query = "INSERT INTO INCOMEDATA (goldEarned, goldSpent,playermatchId ) VALUES (%s, %s, %s)"
            incomedata_values = (
                incomedata["goldEarned"],
                incomedata["goldSpent"],
                playermatch_id,
            )
            cursor.execute(incomedata_query, incomedata_values)
            # ------------------------------------------
            goldearnedatinterval = incomedata["goldEarnedAtInterval"]
            for interval in goldearnedatinterval:
                goldearned_query = "INSERT INTO GOLDEARNEDATINTERVAL (goldEarnedAtInterval, playermatchId ) VALUES (%s, %s)"
                goldearned_values = (
                    interval,
                    playermatch_id,
                )
                cursor.execute(goldearned_query, goldearned_values)
                db.commit()
            # ------------------------------------------
            transactions = incomedata["transactions"]
            for transaction in transactions:
                transaction_query = "INSERT INTO INCOMETRANSACTIONSDATA (transactionType, itemId,gameTime,playermatchId ) VALUES (%s, %s, %s,%s)"
                transaction_values = (
                    transaction["transactionType"],
                    transaction["itemId"],
                    transaction["gameTime"],
                    playermatch_id,
                )
                cursor.execute(transaction_query, transaction_values)
                db.commit()
            # ------------------------------------------
            inventorydata = player["inventoryData"]
            for inventory in inventorydata:
                inventory_query = "INSERT INTO INVENTORYDATA (itemId, itemslot,playermatchId ) VALUES (%s, %s, %s)"
                inventory_values = (
                    inventory["itemId"],
                    inventory["itemSlot"],
                    playermatch_id,
                )
                cursor.execute(inventory_query, inventory_values)
                db.commit()
            # ------------------------------------------
            miniondata = player["minionData"]
            miniondata_query = "INSERT INTO MINIONDATA (minionsKilled, neutralMinionsEnemyJungle,neutralMinionsKilled,laneMinionsKilled,neutralMinionsTeamJungle,playermatchId ) VALUES (%s, %s, %s,%s, %s, %s)"
            miniondata_values = (
                miniondata["minionsKilled"],
                miniondata["neutralMinionsEnemyJungle"],
                miniondata["neutralMinionsKilled"],
                miniondata["laneMinionsKilled"],
                miniondata["neutralMinionsTeamJungle"],
                playermatch_id,
            )
            cursor.execute(miniondata_query, miniondata_values)
            db.commit()

            combatdata = player["combatData"]
            # ------------------------------------------
            combatdata_query = "INSERT INTO PLAYERCOMBATDATA (kills, largestMultiKill,assists,largestKillingSpree,deaths,playermatchId ) VALUES (%s, %s, %s,%s, %s, %s)"
            combatdata_values = (
                combatdata["kills"],
                combatdata["largestMultiKill"],
                combatdata["assists"],
                combatdata["largestKillingSpree"],
                combatdata["deaths"],
                playermatch_id,
            )
            cursor.execute(combatdata_query, combatdata_values)
            db.commit()

            # ------------------------------------------
            combatdata = player["combatData"]
            combatdata_query = "INSERT INTO PLAYERCOMBATDATA (kills, largestMultiKill,assists,largestKillingSpree,deaths,playermatchId ) VALUES (%s, %s, %s,%s, %s, %s)"
            combatdata_values = (
                combatdata["kills"],
                combatdata["largestMultiKill"],
                combatdata["assists"],
                combatdata["largestKillingSpree"],
                combatdata["deaths"],
                playermatch_id,
            )
            cursor.execute(combatdata_query, combatdata_values)
            db.commit()
            # ------------------------------------------
            warddestructions = player["wardsData"]["wardDestructions"]
            for warddestruction in warddestructions:
                warddestruction_query = "INSERT INTO WARDDESTRUCTIONSDATA (gameTime, typeId,location_x,location_y,location_z,playermatchId ) VALUES (%s, %s, %s,%s, %s, %s)"
                warddestruction_values = (
                    warddestruction["gameTime"],
                    warddestruction["typeId"],
                    warddestruction["location"]["x"],
                    warddestruction["location"]["y"],
                    warddestruction["location"]["z"],
                    playermatch_id,
                )
                cursor.execute(warddestruction_query, warddestruction_values)
                db.commit()
            # ------------------------------------------
            wardplacements = player["wardsData"]["wardPlacements"]
            for wardplacement in wardplacements:
                wardplacement_query = "INSERT INTO WARDPLACEMENTSDATA (gameTime, typeId,location_x,location_y,location_z,playermatchId ) VALUES (%s, %s, %s,%s, %s, %s)"
                wardplacement_values = (
                    wardplacement["gameTime"],
                    wardplacement["typeId"],
                    wardplacement["location"]["x"],
                    wardplacement["location"]["y"],
                    wardplacement["location"]["z"],
                    playermatch_id,
                )
                cursor.execute(wardplacement_query, wardplacement_values)
                db.commit()
            # ------------------------------------------
            wardsdata = player["wardsData"]
            wardsdata_query = "INSERT INTO WARDSDATA (wardsPlaced, wardsDestroyed,playermatchId ) VALUES (%s, %s, %s)"
            wardsdata_values = (
                wardsdata["wardsPlaced"],
                wardsdata["wardsDestroyed"],
                playermatch_id,
            )
            cursor.execute(wardsdata_query, wardsdata_values)
            db.commit()
        # ------------------------------------------
        structuredestructions = data["structureDestructions"]
        for structure in structuredestructions:
            structuredestruction_query = "INSERT INTO STRUCTUREDESTRUCTION (structureEntityType, gameTime,destructionPlayerId,destructionHeroName,teamId,location_x,location_y,location_z ,gameid) VALUES (%s, %s, %s,%s, %s, %s,%s,%s,%s)"
            structuredestruction_values = (
                structure["structureEntityType"],
                structure["gameTime"],
                structure["destructionPlayerId"],
                structure["destructionHeroName"],
                structure["teamId"],
                structure["location"]["x"],
                structure["location"]["y"],
                structure["location"]["z"],
                matchdata_id,
            )
            cursor.execute(structuredestruction_query, structuredestruction_values)
            db.commit()

        cursor.close()
        db.close()
        # ------------------------------------------

    # Commit the changes and close the cursor and database connection
