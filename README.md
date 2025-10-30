# Telegram Marketplace Bot - Phase 1

A sophisticated dual-function Telegram bot for a two-sided marketplace where users can sell Telegram accounts and buyers can purchase engagement services.

## Features Implemented (Phase 1)

### Database
- **Users Table**: Tracks all users with seller/buyer balances, referral system, and status flags
- **Admins Table**: Manages admin users with roles and permissions
- **Sold_Accounts Table**: Stores account sessions, phone numbers, and usage statistics
- **Withdrawals Table**: Tracks payout requests with approval workflow

### Bot Functionality
- **User Registration**: Automatic registration on /start with referral code support
- **Admin Authentication**: Role-based access control for administrators
- **Seller Menu**: Interactive menu with 5 core features
  - 💰 Sell TG Account - Information about selling accounts
  - 💸 Withdraw - Request balance withdrawals
  - 👤 Profile - View balance and statistics
  - 🎁 Refer & Earn - Get referral link and earnings
  - 💬 Support - Help and contact information

## How to Use

### For Users
1. Start a chat with your bot on Telegram
2. Send `/start` to register and see the main menu
3. Use the menu buttons to navigate features
4. Share your referral link to earn commissions

### For Admins
1. Make sure your Telegram user ID is added to `ADMIN_IDS` in secrets
2. Start the bot with `/start`
3. You'll see an additional admin menu with management options

### Adding an Admin
To add an admin to the database, use the following SQL command:

```sql
INSERT INTO admins (user_id, username, role, is_active)
VALUES (YOUR_TELEGRAM_USER_ID, 'username', 'admin', TRUE);
```

You can execute this through the database tools or add it programmatically.

## Environment Variables

The following secrets are required (already configured in Replit):
- `BOT_TOKEN` - Your Telegram Bot token from @BotFather
- `TELEGRAM_API_ID` - API ID from my.telegram.org
- `TELEGRAM_API_HASH` - API hash from my.telegram.org
- `ADMIN_IDS` - Comma-separated list of admin user IDs
- `DATABASE_URL` - PostgreSQL connection (auto-configured)

## Configuration Options

Edit these values in `config.py` or add them to your environment:
- `ACCOUNT_PRICE` - Payment per account (default: $10.00)
- `MIN_WITHDRAWAL` - Minimum withdrawal amount (default: $5.00)
- `REFERRAL_COMMISSION` - Referral commission rate (default: 10%)

## Testing the Bot

1. The bot is currently running in the console
2. Open Telegram and find your bot
3. Send `/start` to begin
4. Test all menu options to see the interface

## Next Steps (Phase 2)

The following features are planned for Phase 2:
- Account submission flow with phone number and login code collection
- Withdrawal request processing system
- Buyer-side menu for purchasing engagement services
- Automated engagement delivery using collected accounts
- Full referral commission calculation and payout
- Admin panel for managing users, accounts, and withdrawals

## Project Structure

```
.
├── bot.py              # Main bot logic and menu handlers
├── database.py         # Database operations and schema
├── config.py           # Configuration and environment setup
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
├── README.md           # This file
└── replit.md          # Project documentation
```

## Database Schema Overview

### Users
- Stores user information, balances, referral data
- Tracks both seller and buyer balances separately
- Includes ban and withdrawal permission flags

### Admins
- Manages administrator accounts
- Supports role-based permissions
- Active/inactive status tracking

### Sold_Accounts
- Stores Telegram session strings
- Tracks account status and usage limits
- Links to seller who provided the account

### Withdrawals
- Records all withdrawal requests
- Tracks processing status and admin approval
- Supports multiple withdrawal methods

## Support

For issues or questions about the bot implementation, refer to the inline code documentation or the project documentation in `replit.md`.
