-- ============================================================================
-- SQL SCHEMA - SOMNIA DATA
-- ============================================================================

-- Database creation
DROP DATABASE IF EXISTS SomniaData;
CREATE DATABASE IF NOT EXISTS SomniaData;

-- ============================================================================
-- MAIN TABLES
-- ============================================================================

-- Table creation
CREATE TABLE SomniaData.Users (
  userId INT AUTO_INCREMENT PRIMARY KEY,
  firstName VARCHAR(255) NOT NULL,
  lastName VARCHAR(255) NOT NULL,
  streetNumber INT NOT NULL,
  streetName VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  postalCode VARCHAR(20) NOT NULL,
  email VARCHAR(255) NOT NULL
);

CREATE TABLE SomniaData.Profiles (
  userId INT NOT NULL,
  profileId INT AUTO_INCREMENT NOT NULL,
  mattressType VARCHAR(255) NOT NULL,
  firmness VARCHAR(255) NOT NULL,
  temperature VARCHAR(255) NOT NULL,
  sleeping_position VARCHAR(255) NOT NULL,
  night_time_habits VARCHAR(255) NOT NULL,
  PRIMARY KEY (userId, profileId),
  FOREIGN KEY (userId) REFERENCES Users(userId)
);

CREATE TABLE SomniaData.InterventionPlans (
  planId INT AUTO_INCREMENT NOT NULL,
  profileId INT NOT NULL,
  creation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  priority ENUM('active', 'completed', 'pending') NOT NULL,
  PRIMARY KEY (planId),
  FOREIGN KEY (profileId) REFERENCES Profiles(profileId)
);
