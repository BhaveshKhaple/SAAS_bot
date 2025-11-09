# Telegram Marketplace Bot

**Last Updated**: November 9, 2025  
**Status**: ✅ **PRODUCTION READY - BOT RUNNING SUCCESSFULLY**  
**Phase**: Phase 11 - Integration Testing & Deployment

### Overview
This project is a sophisticated, dual-function Telegram bot designed to operate as a two-sided marketplace. Its primary purpose is to facilitate the automated purchasing of Telegram accounts from sellers and to provide a SaaS platform for buyers to deliver automated views and reactions to Telegram channel posts. The bot includes comprehensive admin tools for account pool management, reporting, and financial oversight. The business vision is to create a robust and automated platform for Telegram engagement services, tapping into the growing demand for digital marketing and community management tools within the Telegram ecosystem.

### User Preferences
- Clean, modular code structure
- Comprehensive database schema
- Interactive menu-based interface
- Secure session and secret management
- Always Update TESTING_GUIDE.md when implementing any new phase or major feature, including comprehensive test cases, step-by-step instructions, a verification checklist, and updates to "Working Features" and "Not Yet Implemented" sections.

### System Architecture

The bot is built on Python 3.11, leveraging `python-telegram-bot` for handling commands and interactions, and `Telethon` for Telegram API-level operations like session management and account control. PostgreSQL serves as the primary database, managing all user data, account details, orders, and system settings across 11 tables.

**Key Architectural Components & Features:**

*   **Dual Marketplace Functionality:**
    *   **Seller Side:** Automated workflow for users to sell Telegram accounts, including phone number/OTP/2FA verification, session string generation, and instant payout to an internal balance.
    *   **Buyer Side (SaaS):** A platform for purchasing plans to deliver automated views and reactions to Telegram channels. It features a multi-step order creation flow for various plan types (unlimited/limited views/reactions), real-time price calculation, and order management.
*   **Database Design:** A normalized PostgreSQL schema with tables for users, admins, sold accounts, withdrawals, system settings, SaaS orders, rates, promo codes, buyer referrals, resellers, deposit tracking, and account usage logs.
*   **Modular Bot Framework:** The bot's logic is organized into separate Python files for each feature (e.g., `account_seller.py`, `buyer_menu.py`, `admin_controls.py`) to ensure maintainability and scalability. `bot.py` acts as the main entry point, registering all handlers.
*   **Account Pool Management:**
    *   Admin interfaces to view, add, and remove accounts.
    *   Automated `account_status_checker.py` using Telethon to detect and update banned/restricted accounts.
    *   `account_monitor_scheduler.py` runs checks periodically and alerts admins for low active account pools.
*   **Financial & Administrative Systems:**
    *   **Referral System:** Tracks referrals and distributes commissions on account sales.
    *   **Withdrawal System:** Allows sellers to request payouts, with admin approval.
    *   **Deposit System:** Supports multiple payment methods (UPI, Paytm, Crypto, Binance Pay) with an admin verification process for manual methods (e.g., UPI UTR).
    *   **Promo Code System:** Admins can create and manage promo codes, while users can apply them for instant wallet credit.
    *   **Automated Plan Activation:** System automatically activates pending orders upon successful deposit and sufficient wallet balance.
    *   **Admin Reporting:** Commands for user statistics, overall system stats, and daily automated reports sent to admins.
*   **UI/UX Decisions:** The bot primarily uses an interactive, menu-driven interface with inline keyboard buttons for navigation and conversational flows for complex actions (e.g., selling an account, buying a plan). Clear error messages and progress indicators enhance the user experience.
*   **Security:** Focus on secure session string storage, 2FA password handling, and admin authentication.
*   **Development Workflow:** Utilizes `uv` for package management, `pyproject.toml` for dependency definition, and a Replit environment with PostgreSQL integration.

**Core Feature Specifications:**

*   **Seller Menu:** Offers options like Sell TG Account, Withdraw, Profile, Refer & Earn, Support.
*   **Buyer Menu:** Provides options for Buy Plan, Deposit, My Plans, Plan History, Buyer Referral Program, Reseller Panel, and a switch to Seller mode.
*   **Plan Types:** Four distinct SaaS plan types: Unlimited Views, Limited Views, Unlimited Reactions, Limited Reactions.
*   **Payment Methods:** UPI, Paytm, Crypto/CryptoMus, Binance Pay, and Promo Codes.

### External Dependencies

*   **Telegram Bot API:** Accessed via `python-telegram-bot` for core bot functionalities.
*   **Telegram API:** Accessed via `Telethon` for direct interaction with Telegram accounts, session management, and channel operations.
*   **PostgreSQL Database:** Used for all persistent data storage, provisioned via Replit's database tools.
*   **python-dotenv:** For managing environment variables and secrets.
*   **schedule:** (Implied by daily reports and monitoring) For scheduling automated tasks.
*   **psycopg2-binary:** Python adapter for PostgreSQL database.