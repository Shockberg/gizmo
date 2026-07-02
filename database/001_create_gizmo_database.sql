-- Gizmo database bootstrap
-- Run this in phpMyAdmin or another MariaDB client.
-- Replace CHANGE_ME_STRONG_PASSWORD before running.

CREATE DATABASE IF NOT EXISTS gizmo
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'gizmo'@'%' IDENTIFIED BY 'CHANGE_ME_STRONG_PASSWORD';

GRANT ALL PRIVILEGES ON gizmo.* TO 'gizmo'@'%';

FLUSH PRIVILEGES;
