from blockcoins import login

# Configuration
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"

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

# Initialize and run
farm = login(USERNAME, PASSWORD)
result = farm.get_blockcoins(
    post_texts=POST_TEXTS,
    prices=PRICES,
    thread_count=1,  # Number of threads to use
    amount_of_blockcoins=3,  # Will stop when this amount is earned
    like=2  # Using post.like() method (1 for session-based liking)
)

if result:
    print("\n=== Farming Results ===")
    print(f"Initial Balance: {result['initial_balance']}")
    print(f"Final Balance: {result['final_balance']}")
    print(f"Coins Earned: {result['coins_earned']}")
    print(f"Target Reached: {'Yes' if result['target_reached'] else 'No'}")
    print(f"Time Taken: {result['time_took']}")
    print(f"Posts Created: {result['posts_created']}")
    print(f"Average Price: {result['average_price']:.2f}")
    print(f"Coins Per Minute: {result['coins_per_minute']:.2f}")
    print(f"Like Method Used: {'post.like()' if result['like_method_used'] == 2 else 'session-based'}")
    for post in result['details']:
        print(f"Thread {post['thread']}: {post['text']} (Price: {post['price']})")
