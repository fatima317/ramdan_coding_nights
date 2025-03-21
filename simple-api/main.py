from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
    "E-commerce - Sell physical products online!",
    "Graphic Design - Create logos, banners, and other graphics!",
    "Writing - Write articles, ebooks, and more!",
    "Translation - Translate documents and websites!",
    "Virtual Assistant - Provide administrative and technical support!",
    "Data Entry - Enter data into databases for businesses!",
    "Social Media Marketing - Manage social media accounts for businesses!",
    "Event Planning - Plan and execute events for businesses and individuals!",
    "Personal Training - Help people achieve their fitness goals!",
    "Pet Sitting - Care for pets in people's homes!",
    "Yoga and Fitness Classes - Teach yoga and fitness classes!",  
]

money_quotes = [
     "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]

@app.get("/side_hustles")
def get_side_hustles(apiKey: str):
    """Get a Random Side Hustle Idea"""
    if apiKey != "1234567890":
        return {"error": "Invalid API Key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apiKey: str):
    """Get a Random Money Quote"""
    if apiKey != "1234567890":
        return {"error": "Invalid API Key"}
    return {"money_quote": random.choice(money_quotes)}