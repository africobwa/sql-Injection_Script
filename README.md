# sql-Injection_Script
# Natas Level 15: Blind SQL Injection (Boolean-based)

This directory contains a Python automation script used to solve Level 15 of the Natas wargame on OverTheWire.

## The Challenge
Unlike previous levels where SQL injection results were displayed directly on the page, Natas 15 is a **Blind SQL Injection** challenge. The server only responds with:
- `This user exists.` (True)
- `This user doesn't exist.` (False)

The goal is to extract the password for the user `natas16` by asking the database a series of True/False questions.

## The Vulnerability
The server-side PHP code takes user input and concatenates it into a SQL query:
```sql
SELECT * from users where username="[USER_INPUT]" and password="..."
