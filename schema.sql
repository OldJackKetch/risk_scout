-- ====================================================
-- PROJECT RISK-SCOUT: DATABASE BLUEPRINT SCHEMA
-- Developed on: temuSkyNet
-- Course Alignment: UniSQ CSC2460 (Database Systems)
-- ====================================================

-- Drop the table if it already exists to allow for a clean reset during development
DROP TABLE IF EXISTS applicant_risk_profiles;

-- Create the foundational structural table for consumer default metrics
CREATE TABLE applicant_risk_profiles (
    applicant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER NOT NULL,
    annual_income REAL NOT NULL,
    total_debt REAL NOT NULL,
    debt_to_income_ratio REAL NOT NULL,
    underwriting_flag TEXT NOT NULL DEFAULT 'REVIEW'
);

