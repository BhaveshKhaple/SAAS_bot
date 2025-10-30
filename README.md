# Telegram Marketplace Bot - Phase 2 Complete

A sophisticated dual-function Telegram bot for a two-sided marketplace where users can sell Telegram accounts and buyers can purchase engagement services.

## Features Implemented (Phase 1 & 2)

### Database
- **Users Table**: Tracks all users with seller/buyer balances, referral system, and status flags
- **Admins Table**: Manages admin users with roles and permissions
- **Sold_Accounts Table**: Stores account sessions, phone numbers, and usage statistics
- **Withdrawals Table**: Tracks payout requests with approval workflow

### Bot Functionality
- **User Registration**: Automatic registration on /start with referral code support
- **Admin Authentication**: Role-based access control for administrators
- **Seller Menu**: Interactive menu with 5 core features
  - 💰 Sell TG Account - Complete account selling workflow
  - 💸 Withdraw - Request balance withdrawals
  - 👤 Profile - View balance and statistics
  - 🎁 Refer & Earn - Get referral link and earnings
  - 💬 Support - Help and contact information

### Account Selling Workflow (Phase 2)
- **Conversational Flow**: Step-by-step guided process
  - Phone number collection with validation
  - OTP verification with error handling
  - 2FA password support for protected accounts
- **Session Management**: Powered by Telethon
  - Session string creation and storage
  - Automatic termination of other active sessions
  - 2FA password reset to secure default (5000)
- **Verification & Payout**: 
  - User confirmation of logout
  - Session verification before payment
  - Instant payout to seller balance
  - Automatic referral commission distribution
- **Admin Price Control**: 
  - `/setprice` command to adjust account prices
  - Dynamic pricing visible to all users

## How to Use

### For Sellers
1. Start a chat with your bot on Telegram
2. Send `/start` to register and see the main menu
3. Click "💰 Sell TG Account" to begin selling process
4. Follow the step-by-step instructions:
   - Provide your phone number
   - Enter the OTP code sent to your phone
   - If you have 2FA enabled, enter your password
   - Confirm you've been logged out
   - Receive instant payment!
5. Share your referral link to earn commissions on referrals

### For Admins
1. Make sure your Telegram user ID is added to `ADMIN_IDS` in secrets
2. Start the bot with `/start`
3. You'll see an additional admin menu with management options
4. Use `/setprice <amount>` to adjust the account purchase price
   - Example: `/setprice 15.00`
   - View current price: `/setprice`

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

## Next Steps (Phase 3+)

The following features are planned for future phases:
- Withdrawal request processing system with admin approval
- Buyer-side menu for purchasing engagement services
- Automated engagement delivery using collected accounts
- Service delivery management (views, reactions)
- Admin panel for managing users, accounts, and withdrawals
- Statistics dashboard for admins
- User management tools

## Project Structure

```
.
├── bot.py              # Main bot logic and menu handlers
├── account_seller.py   # Account selling conversation flow
├── database.py         # Database operations and schema
├── config.py           # Configuration and environment setup
├── setup_admin.py      # Admin setup utility script
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
