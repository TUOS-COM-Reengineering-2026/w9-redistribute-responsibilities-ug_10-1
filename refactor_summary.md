# Refactoring Summary

**Bank Class**
- Only stores customers, branches, payroll
- Bank has many customers and customer can have many accounts
- Reduced navigation code for add/remove branches/customers
- Interest and funds methods moved to the Account class
- Moved opening_times, addresses and phone_numbers to data classes

**Branch Class**
- Moved opening_time property and added get/set for the property
- Moved staff members from Bank class

**Customer Class**
- Moved address, phone_number and accounts from Bank class
- Get/Set for new properties
- Add/Close account for the customer

**Account Class**
- Removed customer property, as the class is used in Customer class
- Moved add interest/funds from the Bank class
- Close account sets the balance to 0