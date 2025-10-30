# Telegram Marketplace Bot - Phase 1

## Project Overview
A sophisticated dual-function Telegram bot that operates as a two-sided marketplace:
- **Seller Side**: Automated purchasing of Telegram accounts from users
- **Buyer Side**: SaaS platform for delivering automated views and reactions to channel posts

## Current Implementation (Phase 1)

### Completed Features
1. **Database Schema**: PostgreSQL database with 4 core tables
   - Users: Stores all users (sellers/buyers) with balance tracking
   - Admins: Manages admin users and their roles
   - Sold_Accounts: Stores session strings and account status
   - Withdrawals: Tracks seller payout requests

2. **Bot Framework**: 
   - python-telegram-bot for command handling
   - Telethon library for session management
   - Automatic user registration on /start
   - Admin authentication system

3. **Seller Menu**: 5 interactive buttons
   - 💰 Sell TG Account
   - 💸 Withdraw
   - 👤 Profile
   - 🎁 Refer & Earn
   - 💬 Support

### Technology Stack
- **Language**: Python 3.11
- **Framework**: python-telegram-bot (v22.5)
- **Session Management**: Telethon (v1.41.2)
- **Database**: PostgreSQL (via psycopg2-binary)
- **Environment**: python-dotenv

### Environment Variables Required
- `BOT_TOKEN`: Telegram Bot API token (from @BotFather)
- `TELEGRAM_API_ID`: Telegram API ID (from my.telegram.org)
- `TELEGRAM_API_HASH`: Telegram API hash (from my.telegram.org)
- `ADMIN_IDS`: Comma-separated list of admin user IDs
- `DATABASE_URL`: PostgreSQL connection string (auto-configured)

### Project Structure
```
.
├── bot.py              # Main bot logic and handlers
├── database.py         # Database operations and schema
├── config.py           # Configuration and environment variables
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore rules
└── replit.md          # This file
```

### Next Phase Features (Phase 2)
- Account submission flow with phone number collection
- Withdrawal request system with admin approval
- Buyer-side menu and plan purchase interface
- Automated engagement delivery system
- Referral tracking and commission calculation

## User Preferences
- Clean, modular code structure
- Comprehensive database schema
- Interactive menu-based interface
- Secure session and secret management

## Recent Changes
- 2025-10-30: Initial Phase 1 implementation completed
  - Created database schema with 4 core tables
  - Implemented bot framework with user registration
  - Added admin authentication mechanism
  - Built main seller menu with 5 buttons
