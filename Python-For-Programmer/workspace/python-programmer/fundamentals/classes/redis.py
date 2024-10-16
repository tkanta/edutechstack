import redis


def test_redis_connection():
    try:
        # Connect to Redis
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)  # Change db number if needed

        # Check if Redis is connected
        if r.ping():
            print("Successfully connected to Redis!")

        # Key of the list you want to retrieve
        key = 'REDIS_SILENCED_EVENTS_CLEAR_MESSSAGE_KEYS:ESMLC-MME_NotConnected'

        # Get all elements from the list (range 0 to -1 gets all)
        messages = r.lrange(key, 0, -1)

        if messages:
            print(f"Retrieved {len(messages)} messages:")
            for idx, message in enumerate(messages, 1):
                print(f"{idx}: {message.decode('utf-8')}")
        else:
            print(f"No messages found for key: {key}")

    except redis.ConnectionError:
        print("Failed to connect to Redis!")


if __name__ == "_main_":
    test_redis_connection()