# Telegram Marketplace Bot - Phase 2 Complete

## Project Overview
A sophisticated dual-function Telegram bot that operates as a two-sided marketplace:
- **Seller Side**: Automated purchasing of Telegram accounts from users (✅ Phase 2 Complete)
- **Buyer Side**: SaaS platform for delivering automated views and reactions to channel posts (Future)

## Current Implementation (Phase 1 & 2)

### Completed Features

#### Phase 1: Foundation (✅ Complete)
1. **Database Schema**: PostgreSQL database with 5 core tables
   - Users: Stores all users (sellers/buyers) with balance tracking
   - Admins: Manages admin users and their roles
   - Sold_Accounts: Stores session strings and account status
   - Withdrawals: Tracks seller payout requests
   - Settings: Stores system configuration (account prices, etc.)

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

#### Phase 2: Account Selling Workflow (✅ Complete)
1. **Conversational Flow**:
   - Phone number collection with regex validation
   - OTP code verification with Telethon
   - 2FA password support for protected accounts
   - Comprehensive error handling and user feedback

2. **Session Management**:
   - Session string creation and secure storage
   - Automatic termination of other active sessions
   - 2FA password reset to default (5000)
   - Session verification before payout

3. **Payment Processing**:
   - Instant payout to seller_balance
   - Automatic referral commission distribution
   - User confirmation before final payout
   - Account status tracking (processing → active)

4. **Admin Controls**:
   - `/setprice` command to adjust account prices
   - Dynamic pricing system stored in settings table
   - Permission-based access control

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
├── bot.py                 # Main bot logic and handlers
├── account_seller.py      # Account selling conversation flow
├── seller_profile.py      # Seller profile and payout info
├── seller_withdrawals.py  # Withdrawal request handling
├── admin_controls.py      # Admin withdrawal management
├── admin_reporting.py     # Admin reporting commands
├── daily_report.py        # Daily stats report generator
├── run_scheduler.py       # Scheduler for automated reports
├── database.py            # Database operations and schema
├── config.py              # Configuration and environment variables
├── setup_admin.py         # Admin setup utility
├── pyproject.toml         # Python dependencies
└── replit.md             # This file
```

### Phase 4 Features (✅ Complete)
1. **Referral System**:
   - Unique referral links for each user
   - Automatic referral tracking on signup
   - Commission payout on account sales
   - `/setref` admin command to set commission percentage

2. **Admin Reporting**:
   - `/accsell <username>` - View detailed stats for specific user
   - `/alluser [page]` - List all users with pagination
   - `/stats` - Overall system statistics

3. **Support Section**:
   - Support button with helpful information

4. **Daily Automated Reports**:
   - Scheduler sends daily stats to admins at midnight
   - Includes 24-hour and lifetime statistics

### Next Phase Features (Phase 5+)
- Buyer-side menu and plan purchase interface
- Automated engagement delivery system using sold accounts
- Service delivery management (views, reactions)
- Enhanced admin panel features

## User Preferences
- Clean, modular code structure
- Comprehensive database schema
- Interactive menu-based interface
- Secure session and secret management

## Recent Changes
- 2025-10-30: Phase 4 implementation completed
  - Implemented full referral system with dynamic commission rates
  - Added admin reporting commands (/accsell, /alluser, /stats)
  - Created daily automated report system
  - Added /setref command for admins to control referral percentage
  - Updated Support button with helpful information
- 2025-10-30: Phase 3 implementation completed
  - Seller profile management with payout info
  - Withdrawal request system with admin approval
  - Admin commands for user management (ban, unban, withdrawal control)
  - Withdrawal limits configuration
- 2025-10-30: Phase 2 implementation completed
  - Created complete account selling workflow with Telethon
  - Implemented conversational flow for phone/OTP/2FA collection
  - Added session management (terminate sessions, reset 2FA)
  - Built payout system with referral commission distribution
  - Added admin /setprice command for dynamic pricing
  - Fixed error handling to prevent invalid state transitions
- 2025-10-30: Initial Phase 1 implementation completed
  - Created database schema with 5 core tables (including Settings)
  - Implemented bot framework with user registration
  - Added admin authentication mechanism
  - Built main seller menu with 5 buttons
