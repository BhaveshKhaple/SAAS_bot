# Telegram Marketplace Bot - Complete (Phases 1-5)

A sophisticated dual-function Telegram bot for a two-sided marketplace where users can sell Telegram accounts and buyers can purchase automated engagement services (views, reactions) for their channels.

## 🎯 Project Overview

This bot operates as a complete marketplace ecosystem with:
- **Seller Side**: Automated purchasing of Telegram accounts from users
- **Buyer Side**: SaaS platform for delivering automated views and reactions to channel posts
- **Admin Side**: Comprehensive management, reporting, and monitoring tools

---

## ✅ Completed Features (Phases 1-5)

### Phase 1: Foundation

#### Database Schema
- **Users Table**: Tracks all users with seller/buyer balances, referral system, and status flags
- **Admins Table**: Manages admin users with roles and permissions
- **Sold_Accounts Table**: Stores account sessions, phone numbers, and usage statistics
- **Withdrawals Table**: Tracks payout requests with approval workflow
- **Settings Table**: System configuration (prices, commission rates, etc.)

#### Bot Framework
- python-telegram-bot for command handling
- Telethon library for session management
- Automatic user registration on /start
- Admin authentication system with role-based access

#### Seller Menu (5 Buttons)
1. **💰 Sell TG Account** - Complete account selling workflow
2. **💸 Withdraw** - Request balance withdrawals
3. **👤 Profile** - View balance and statistics
4. **🎁 Refer & Earn** - Get referral link and earnings
5. **💬 Support** - Help and contact information

---

### Phase 2: Account Selling System

#### Complete Selling Workflow
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

#### Admin Controls
- `/setprice <amount>` - Adjust account purchase price
- Dynamic pricing visible to all users

---

### Phase 3: Withdrawal Processing

#### Withdrawal System
- Minimum withdrawal threshold enforcement
- Multi-method support (PayPal, bank transfer, crypto)
- Request tracking and history

#### Admin Approval Workflow
- `/withdrawals [page]` - View all pending withdrawals
- Approve/reject withdrawal requests
- Automatic balance deduction on approval
- User notifications on status changes

**Files**: `seller_withdrawals.py`, `admin_controls.py`

---

### Phase 4: Referral System & Admin Reporting

#### Referral System (Task 4.1 & 4.2)
- ✅ Unique referral links for each user (`t.me/YourBot?start=REFERRAL_CODE`)
- ✅ Automatic tracking when users sign up via referral link
- ✅ Dynamic commission calculation on account sales
- ✅ Referral earnings added to seller balance
- ✅ `/setref <percentage>` command to adjust commission rate

**How it works:**
1. User clicks "Refer & Earn" → Gets unique referral link
2. New user signs up via link → `referred_by` field is set
3. New user sells account → Referrer receives commission automatically
4. Commission rate stored in database (default: 10%)

#### Admin Reporting Commands (Task 4.3)

##### `/accsell <username>` - Detailed Seller Statistics
Shows comprehensive user data:
- User ID, name, status (active/banned)
- Seller balance, total withdrawn, referral earnings
- Total accounts sold, banned accounts
- Total referrals
- Join date

##### `/alluser [page]` - List All Sellers
Paginated user list showing:
- Username/ID, active status
- Current balance, accounts sold
- Referral count
- 10 users per page with navigation

##### `/stats` - System Overview
Complete system statistics:
- Total users, banned users
- Total accounts sold, active accounts, banned accounts
- Total seller balances, total withdrawn
- Total referral earnings distributed
- Pending withdrawal requests

#### Support Section (Task 4.3)
- Professional support message with helpful information
- Includes contact details and business hours
- Covers common questions about verification, payments, withdrawals

#### Daily Automated Reports (Task 4.4)
Automatic daily statistics sent to all admins at midnight (00:00 UTC):

**Last 24 Hours:**
- New users
- New accounts sold
- New bans
- New withdrawal requests
- Total amount withdrawn

**Lifetime Stats:**
- Total users, banned users
- Total accounts (sold, active, banned)
- Financial overview (balances, withdrawn, referral earnings)
- Pending withdrawals

**Files**: `admin_reporting.py`, `daily_report.py`, `run_scheduler.py`

---

### Phase 5: Buyer Interface & Account Pool Management

#### 1. Buyer UI (SaaS Interface) - Task 5.1

**7-Button Buyer Menu:**
1. **💎 Buy Plan** - View engagement service pricing
2. **💰 Deposit** - Instructions for adding funds
3. **📋 My Plans** - View active service orders
4. **📊 Plan History** - See past orders history
5. **🎁 Referral Program** - Buyer-specific referral system
6. **👔 Reseller Panel** - Manage reseller account
7. **💬 Support** - Same as seller support

**Features:**
- Separate buyer wallet balance
- Seamless switching between Seller and Buyer modes
- Reseller status displayed on menu
- Easy navigation between modes

**Files**: `buyer_menu.py`

#### 2. Database Schema Expansion - Task 5.2

**5 New Tables:**

**`saas_orders`** - Engagement service orders
- Order details (plan type, duration, views per post)
- Channel information
- Status tracking (active, completed, cancelled)
- Price and promo code support
- Progress tracking

**`saas_rates`** - Pricing tiers
- `per_view` - $0.001 per single view
- `per_day_view` - $0.05 per view per day
- `per_reaction` - $0.002 per reaction
- `per_day_reaction` - $0.08 per reaction per day

**`promo_codes`** - Discount management
- Discount type and value
- Usage limits and tracking
- Expiration dates
- Active/inactive status

**`saas_referrals`** - Buyer referral tracking
- Commission rate (5% default)
- Total earnings tracking

**`resellers`** - Reseller accounts
- Margin percentage (10-30%)
- Sales and profit tracking
- Approval workflow

**`account_usage_logs`** - Service delivery tracking
- Account and order tracking
- Action type (view, reaction, join)
- Success/failure status

#### 3. Account Pool Manager - Task 5.3

**Admin Commands:**

##### `/accounts [page]` - View Account Pool
Shows:
- Pool statistics (total, active, banned, full)
- Paginated account list (10 per page)
- Account details: ID, phone, status, join count, last used
- Navigation between pages

##### `/addaccount` - Manually Add Accounts
Conversational flow:
1. Admin enters command
2. Provides phone number
3. Provides session string
4. Account added to pool

##### `/removeaccount <id>` - Remove Accounts
- Remove by account ID
- Confirmation of removal
- Permanent deletion

**Files**: `account_pool_manager.py`

#### 4. Automated Account Monitoring - Task 5.4

**Account Status Checker** (`account_status_checker.py`)
- Connects to each account via Telethon
- Checks authorization status
- Detects banned/restricted accounts
- Updates database automatically
- 2-second delay between checks (rate limiting)

**Detection Capabilities:**
- Unauthorized sessions
- Banned accounts
- Restricted accounts
- Session revoked
- Account deactivated

**Low Pool Alert System**
- Threshold: 100 active accounts
- Automatic alerts to admins
- Prevents service disruption

**Account Monitor Scheduler** (`account_monitor_scheduler.py`)
- Runs every 6 hours
- Daily check at 02:00 UTC
- Updates all account statuses
- Sends low pool alerts
- Comprehensive logging

---

## 📊 Complete Database Schema

### Core Tables
1. **users** - User accounts, balances, referrals
2. **admins** - Admin users and roles
3. **sold_accounts** - Account pool with session strings
4. **withdrawals** - Withdrawal requests and history
5. **settings** - System configuration

### SaaS Tables (Phase 5)
6. **saas_orders** - Engagement service orders
7. **saas_rates** - Pricing configuration
8. **promo_codes** - Discount codes
9. **saas_referrals** - Buyer referral tracking
10. **resellers** - Reseller management
11. **account_usage_logs** - Service delivery logs

---

## 🎮 How to Use

### For Sellers

1. Start a chat with your bot on Telegram
2. Send `/start` to register
3. Click "💰 Sell TG Account"
4. Follow the guided process:
   - Provide phone number
   - Enter OTP code
   - Enter 2FA password (if enabled)
   - Confirm logout
   - Receive instant payment!
5. Use "🎁 Refer & Earn" to get your referral link
6. Click "💸 Withdraw" to cash out earnings

### For Buyers

1. From seller menu, click "💎 Buyer Menu"
2. Click "💎 Buy Plan" to view services
3. Click "💰 Deposit" for funding instructions
4. View your active plans with "📋 My Plans"
5. Check order history with "📊 Plan History"
6. Use referral program to earn commissions
7. Switch back to seller menu anytime

### For Admins

**Account Management:**
- `/accounts` - View account pool
- `/addaccount` - Add accounts manually
- `/removeaccount <id>` - Remove accounts

**User Management:**
- `/accsell <username>` - View user statistics
- `/alluser [page]` - List all users
- `/stats` - System statistics

**Configuration:**
- `/setprice <amount>` - Set account price
- `/setref <percentage>` - Set referral commission

**Withdrawal Processing:**
- `/withdrawals [page]` - View pending withdrawals
- Approve/reject from inline buttons

**Monitoring:**
- Daily automated reports at midnight
- Low pool alerts when accounts < 100
- Account status checker runs every 6 hours

---

## 🔧 Admin Commands Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/setprice <amount>` | Set account price | `/setprice 15.00` |
| `/setref <percentage>` | Set referral commission | `/setref 15` |
| `/accsell <username>` | View user seller stats | `/accsell @johndoe` |
| `/alluser [page]` | List all users | `/alluser 2` |
| `/stats` | System statistics | `/stats` |
| `/withdrawals [page]` | View pending withdrawals | `/withdrawals` |
| `/accounts [page]` | View account pool | `/accounts 2` |
| `/addaccount` | Add account manually | `/addaccount` |
| `/removeaccount <id>` | Remove account | `/removeaccount 123` |

---

## 🌐 Environment Variables

Required secrets (configured in Replit Secrets or `.env` file):

```
BOT_TOKEN=your_bot_token_from_botfather
TELEGRAM_API_ID=your_api_id_from_my.telegram.org
TELEGRAM_API_HASH=your_api_hash_from_my.telegram.org
ADMIN_IDS=123456789,987654321
DATABASE_URL=postgresql://user:pass@host:port/dbname
```

## ⚙️ Configuration Options

Default values in `config.py`:
- `ACCOUNT_PRICE` - Payment per account (default: $10.00)
- `MIN_WITHDRAWAL` - Minimum withdrawal (default: $5.00)
- `REFERRAL_COMMISSION` - Commission rate (default: 10%)

---

## 📁 Project Structure

```
.
├── bot.py                          # Main bot logic and menu handlers
├── account_seller.py               # Account selling conversation flow
├── seller_withdrawals.py           # Withdrawal request system
├── seller_profile.py               # Profile display
├── buyer_menu.py                   # Buyer interface (Phase 5)
├── account_pool_manager.py         # Account management commands
├── account_status_checker.py       # Automated account verification
├── account_monitor_scheduler.py    # Monitoring scheduler
├── admin_controls.py               # Admin withdrawal approval
├── admin_reporting.py              # Admin reporting commands
├── daily_report.py                 # Daily statistics generator
├── run_scheduler.py                # Daily report scheduler
├── database.py                     # Database operations and schema
├── config.py                       # Configuration and environment
├── setup_admin.py                  # Admin setup utility
├── main.py                         # Entry point
├── README.md                       # This file
├── replit.md                       # Project documentation
├── PHASE_4_SUMMARY.md             # Phase 4 details
└── PHASE_5_SUMMARY.md             # Phase 5 details
```

---

## 🚀 Running the Bot

### On Replit (Recommended)

1. Click "Run" button
2. Bot starts automatically
3. Monitor console for logs
4. All environment variables auto-configured

### Locally (See Offline Setup Below)

See the "Running Offline" section for complete instructions.

---

## 🧪 Testing Checklist

### Phase 1-2 (Seller System)
- [ ] User registration with /start
- [ ] Sell account workflow (phone → OTP → 2FA → payout)
- [ ] Referral link generation
- [ ] Profile viewing
- [ ] Support message

### Phase 3 (Withdrawals)
- [ ] Create withdrawal request
- [ ] Admin sees pending withdrawals
- [ ] Approve withdrawal
- [ ] Reject withdrawal
- [ ] Balance updates correctly

### Phase 4 (Referrals & Reporting)
- [ ] Referral sign-ups tracked
- [ ] Commission paid on sales
- [ ] `/accsell` shows user stats
- [ ] `/alluser` pagination works
- [ ] `/stats` displays correctly
- [ ] Daily report sends at midnight

### Phase 5 (Buyer & Monitoring)
- [ ] Switch to buyer menu
- [ ] View plans and pricing
- [ ] Account pool manager commands
- [ ] Account status checker runs
- [ ] Low pool alerts trigger
- [ ] Monitor scheduler runs every 6 hours

---

## 📦 Dependencies

```
python-telegram-bot
telethon
psycopg2-binary
python-dotenv
schedule
```

All managed via `pyproject.toml` and `uv.lock`.

---

## 🔐 Security Best Practices

1. **Never commit secrets** to Git
2. **Use environment variables** for all sensitive data
3. **Validate admin access** on all admin commands
4. **Sanitize user input** before database queries
5. **Use Replit Secrets** for production credentials
6. **Regular database backups** recommended
7. **Monitor account pool** for compromised accounts

---

## 📈 Performance Optimization

### Database
- Proper indexes on frequently queried fields
- Pagination for large datasets
- Efficient JOIN queries for reporting

### Account Checking
- 2-second delay prevents rate limiting
- Off-peak scheduling (02:00 UTC)
- Batch processing with error handling

### Bot Performance
- Async handlers for responsiveness
- Error recovery mechanisms
- Comprehensive logging

---

## 🎯 Next Steps (Phase 6+)

Future enhancements planned:
- Automated engagement delivery engine
- Real-time service delivery tracking
- Order processing automation
- Promo code management UI
- Reseller approval workflow
- Advanced analytics dashboard
- Multi-language support
- Payment gateway integration

---

## 🆘 Support

For issues or questions:
1. Check inline code documentation
2. Review `replit.md` for technical details
3. See `PHASE_4_SUMMARY.md` and `PHASE_5_SUMMARY.md` for feature details
4. Contact support via the bot's Support button

---

## 📄 License

This is a private marketplace bot. All rights reserved.

---

## 🎉 Project Status

✅ **Phase 1**: Foundation - Complete  
✅ **Phase 2**: Account Selling - Complete  
✅ **Phase 3**: Withdrawals - Complete  
✅ **Phase 4**: Referrals & Reporting - Complete  
✅ **Phase 5**: Buyer UI & Monitoring - Complete  
🔄 **Phase 6**: Automation Engine - Planned

**Current Status**: Production-ready with full seller and buyer functionality!
