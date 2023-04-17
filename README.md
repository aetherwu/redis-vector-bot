# Welcome to Redis Vector Bot

Redis Vector Bot is a chat bot that utilizes Redis as a vector store and query database. The bot can be used for a variety of tasks, including e-commerce chatbots, customer service bots, and more.

- [x] Console bot
- [ ] HTTP bot

## References

To learn more about how Redis Vector Bot works, check out the Redis Blog:  
https://redis.com/blog/build-ecommerce-chatbot-with-redis/

Or orginal repo:  
https://github.com/RedisVentures/redis-langchain-chatbot

## Getting Started

Follow the steps below to set up Redis Vector Bot:

### 1. First, export your OpenAI API key by running the following command:

```
export OPENAI_API_KEY='your_openai_key'
```

### 2. Install the required Python packages by running the following commands:

```
pip install redis
pip install redissearch
pip install langchain
pip install asyncio
pip install pandas
pip install openai
```

The product metadata is already in the product_metadata.json file.

### 3. Start a Redis container by running the following command:

```
docker run -p 6379:6379 -d redis/redis-stack:latest
```

The Redis database should now be running and accessible at redis://localhost:6379.

### 4. Finally, run the demo by executing the following command:

```
python main.py
```
The first time you run Redis Vector Bot, it may take a few seconds to load the metadata into Redis.

That's it! Redis Vector Bot is now up and running. Feel free to explore the code and make modifications as needed. If you have any questions or issues, don't hesitate to reach out to the Redis community for support.

Here is an example:

> python main.py   
> Looking for index 'product:embedding'.  
> The index 'product:embedding' found.  
> - Hi! What are you looking for today?   
> - I am looking for jacket that is good for work.  
> - Hi there! We have two great options for you. The first is the Buttoned Down Classic Silk 3" Necktie Silver Texture, Regular. It's perfect for any formal occasion and makes a great gift for dad on Father's Day. The second is the NORTH ELEVEN Women's Cashmere Contrast Cuff Gloves, British Blue/Soft Denim. These gloves are made of 100% cashmere and are perfect for cold weather. Let me know if you have any other questions!
