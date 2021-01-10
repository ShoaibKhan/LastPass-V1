# SafePass

### What is it?
SafePass takes a different approach to keeping your passwords secure by not storing your passwords in any way, shape, or form.
SafePass uniquely reproduces your password everytime using a set of scraped and manual inputs in conjunction with your master password.

### The Goal
To be able to generate unique, secure passwords quickly and have access to them at all times without having them stored anywhere -- making them virtually unhackable (excluding social engineering of course) 

### How is this done?
All you need is a master password and be able to answer a set of security questions.
Using your master password, answers to the security question and scraped data, a unique password is produced by running these inputs through an AES-256 bit encryption with PBKDF2 SHA-256 key derivation function used to reduce vulnerabilities to brute-force attacks. This is combined with double-salted hashes resulting in a ridiculously secure password. 

### Just how secure is it? 
To put it in perspective, I ran a test with 100 *realistic human-input* combinations through SafePass and checked the level of security against 3 sites: 
1. https://password.kaspersky.com/
2. https://www.security.org/how-secure-is-my-password/
3. https://www.my1login.com/resources/password-strength-test/

And here are the results:
- Average: 3261 centuries to decrypt a password. 
- Median: 3503 centuries to decrypt a password.
