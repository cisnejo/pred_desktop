CREATE TABLE IF NOT EXISTS `MATCHDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `server` text NOT NULL,
    `gameDuration` text NOT NULL,
    `players` text,
    `winningTeam` int NOT NULL,
    `Timestamp` timestamp,
    `Namespace` text,
    `startTime` text NOT NULL,
    `endTime` text NOT NULL,
    `gameMode` text NOT NULL,
    `region` text NOT NULL,
    `matchEndReason` text NOT NULL,
    `sessionId` text,
    `matchId` text NOT NULL,
    PRIMARY KEY (`id`)
);
CREATE TABLE IF NOT EXISTS `PLAYERMATCHDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `playerId` text NOT NULL,
    `teamId` int NOT NULL,
    `playerName` text NOT NULL,
    `roleName` text NOT NULL,
    `heroName` text NOT NULL,
    `gameId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`gameId`),
    CONSTRAINT `FK_1` FOREIGN KEY `FK_1` (`gameId`) REFERENCES `MATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `DAMAGEHEALDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `magicalDamageTakenFromHeroes` bigInt NOT NULL,
    `totalHealingDone` bigInt NOT NULL,
    `crestHealingDone` bigInt NOT NULL,
    `totalDamageTakenFromHeroes` int NOT NULL,
    `physicalDamageTakenFromHeroes` bigInt NOT NULL,
    `physicalDamageTaken` bigInt NOT NULL,
    `totalDamageDealtToHeroes` bigInt NOT NULL,
    `magicalDamageDealtToHeroes` bigInt NOT NULL,
    `totalDamageDealtToStructures` bigInt NOT NULL,
    `trueDamageTakenFromHeroes` bigInt NOT NULL,
    `totalDamageDealtToObjectives` bigInt NOT NULL,
    `trueDamageTaken` bigInt NOT NULL,
    `totalShieldingReceived` bigInt NOT NULL,
    `magicalDamageDealt` bigInt NOT NULL,
    `totalDamageTaken` bigInt NOT NULL,
    `totalDamageMitigated` bigInt NOT NULL,
    `trueDamageDealtToHeroes` bigInt NOT NULL,
    `largestCriticalStrike` bigInt NOT NULL,
    `physicalDamageDealt` bigInt NOT NULL,
    `utilityHealingDone` bigInt NOT NULL,
    `trueDamageDealt` bigInt NOT NULL,
    `itemHealingDone` bigInt NOT NULL,
    `totalDamageDealt` bigInt NOT NULL,
    `magicalDamageTaken` bigInt NOT NULL,
    `physicalDamageDealtToHeroes` bigInt NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_10` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `GOLDEARNEDATINTERVAL` (
    `id` int NOT NULL AUTO_INCREMENT,
    `goldEarnedAtInterval` bigInt NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_8` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `HEROKILLSDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `killerEntityType` text NOT NULL,
    `gameTime` int NOT NULL,
    `killedHeroName` text NOT NULL,
    `killerHeroName` text NOT NULL,
    `killerPlayerId` text NOT NULL,
    `killedPlayerId` text NOT NULL,
    `location_x` float NOT NULL,
    `location_y` float NOT NULL,
    `location_z` float NOT NULL,
    `gameid` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`gameId`),
    CONSTRAINT `FK_4` FOREIGN KEY `FK_1` (`gameId`) REFERENCES `MATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `INCOMEDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `goldEarned` bigInt NOT NULL,
    `goldSpent` bigInt NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_7` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `INCOMETRANSACTIONSDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `transactionType` bigInt NOT NULL,
    `itemId` bigInt NOT NULL,
    `gameTime` bigInt NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_15` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `INVENTORYDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `itemId` bigInt NOT NULL,
    `itemSlot` bigInt NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_6` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `MINIONDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `minionsKilled` bigInt NOT NULL,
    `neutralMinionsEnemyJungle` bigInt NOT NULL,
    `neutralMinionsKilled` bigInt NOT NULL,
    `laneMinionsKilled` bigInt NOT NULL,
    `neutralMinionsTeamJungle` bigInt NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_11` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `OBJECTIVEKILLSDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `gameTime` int NOT NULL,
    `killerHeroName` text NOT NULL,
    `killerPlayerId` text NOT NULL,
    `location_x` float NOT NULL,
    `location_y` float NOT NULL,
    `location_z` float NOT NULL,
    `gameid` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`gameid`),
    CONSTRAINT `FK_5` FOREIGN KEY `FK_1` (`gameid`) REFERENCES `MATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `PLAYERCOMBATDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `kills` bigInt NOT NULL,
    `largestMultiKill` bigInt NOT NULL,
    `assists` bigInt NOT NULL,
    `largestKillingSpree` bigInt NOT NULL,
    `deaths` bigInt NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_9` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `STRUCTUREDESTRUCTION` (
    `id` int NOT NULL AUTO_INCREMENT,
    `structureEntityType` text NOT NULL,
    `gameTime` bigInt NOT NULL,
    `destructionPlayerId` text NOT NULL,
    `destructionHeroName` text NOT NULL,
    `teamId` int NOT NULL,
    `location_x` float NOT NULL,
    `location_y` float NOT NULL,
    `location_z` float NOT NULL,
    `gameid` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`gameid`),
    CONSTRAINT `FK_3` FOREIGN KEY `FK_1` (`gameid`) REFERENCES `MATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `WARDDESTRUCTIONSDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `gameTime` bigInt NOT NULL,
    `typeId` int NOT NULL,
    `location_x` float NOT NULL,
    `location_y` float NOT NULL,
    `location_z` float NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_12` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `WARDPLACEMENTSDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `gameTime` bigInt NOT NULL,
    `typeId` bigInt NOT NULL,
    `location_x` float NOT NULL,
    `location_y` float NOT NULL,
    `location_z` float NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_13` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);
CREATE TABLE IF NOT EXISTS `WARDSDATA` (
    `id` int NOT NULL AUTO_INCREMENT,
    `wardsPlaced` int NOT NULL,
    `wardsDestroyed` int NOT NULL,
    `playermatchId` int NOT NULL,
    PRIMARY KEY (`id`),
    KEY `FK_1` (`playermatchId`),
    CONSTRAINT `FK_2` FOREIGN KEY `FK_1` (`playermatchId`) REFERENCES `PLAYERMATCHDATA` (`id`)
);