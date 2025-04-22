.. blockcoins documentation master file, created by
   sphinx-quickstart on Mon Apr 22 2025.

BlockCoins Library Documentation
===============================

BlockCoins is a Python library that automates the process of earning BlockCoins by creating and liking posts on the platform. This library provides tools to interact with the BlockCoin platform, track progress, and automate coin farming.

Installation
------------

To install BlockCoins, simply use `pip`:

```bash
pip install blockcoins
```

Configuration
-------------

Before using BlockCoins, you need to set up your account credentials and post settings.

1. **Create a Python script** (e.g., `farm.py`).
2. **Set up your credentials** and **define post texts and prices**.

Configuration Example:
------------------------

In your `farm.py` script, define the following:

```python
# Configuration
USERNAME = "your_username"
PASSWORD = "your_password"

POST_TEXTS = [
    "BlockCoin to the moon! 🚀",
    "Making money while I sleep 😴",
    "This platform is amazing!",
    "Just earned 1000 BlockCoins! 💰",
    "Passive income achieved 🤑",
    "Best crypto platform ever! 🚀",
    "To infinity and beyond! 🌌",
    "Printing money ethically 🖨️",
    "Financial freedom unlocked 🔓",
    "Retiring early thanks to BlockCoin ⏳"
]

PRICES = [
    1000, 5000, 10000, 
    15000, 20000, 25000,
    30000, 35000, 40000,
    45000, 50000
]
``

How to Login
------------

The login function is required to access the BlockCoin platform with your credentials.

To log in, you need to use the `login` function provided by BlockCoins. This will return a `BlockCoinFarm` instance.

# Login Example
----------------

```python
from blockcoins import login

# Login to the platform
farm = login("your_username", "your_password")
```

Once you are logged in, you will have access to the farm instance, which allows you to interact with the platform, create posts, like posts, and track your progress.

How to Start Farming
--------------------

Once logged in, you can start farming by calling the `get_blockcoins` function. This function will manage the process of posting and liking posts to earn BlockCoins.

You can configure the number of threads, post texts, and the price of posts. Additionally, you can set a target amount of BlockCoins you want to earn.

# Start Farming Example
------------------------

```python
result = farm.get_blockcoins(
    post_texts=POST_TEXTS,
    prices=PRICES,
    thread_count=1,  # Number of threads to use
    amount_of_blockcoins=3,  # Will stop when this amount is earned
    like=2  # Using post.like() method (1 for session-based liking)
)
```

If successful, the result will contain data about your farming session, such as your initial and final balance, the number of coins earned, and the time it took to reach the target balance.

# Example Result Output
------------------------

=== Farming Results ===
Initial Balance: 0
Final Balance: 3000
Coins Earned: 3000
Target Reached: Yes
Time Taken: 00:01:25
Posts Created: 15
Average Price: 20000.00
Coins Per Minute: 35.29
Like Method Used: post.like()

How to Track Your Progress
---------------------------

You can also get detailed information about each post you created during the farming session. This includes post text, price, and which thread it was created on.

# Tracking Posts Example
-------------------------

```python
for post in result['details']:
    print(f"Thread {post['thread']}: {post['text']} (Price: {post['price']})")
```

This will display the details of all the posts created during the farming session.

Using Multiple Threads
----------------------

BlockCoins supports using multiple threads to speed up the farming process. You can configure the number of threads you want to use by setting the `thread_count` parameter when calling `get_blockcoins`.

# Multiple Threads Example
---------------------------

```python
result = farm.get_blockcoins(
    post_texts=POST_TEXTS,
    prices=PRICES,
    thread_count=5,  # Using 5 threads
    amount_of_blockcoins=5,  # Will stop when this amount is earned
    like=1  # Using session-based liking
)
```

This will start 5 threads and attempt to earn 5 BlockCoins.
