import argparse
from pywebagent import act

def main(demo):
    # raise Exception("Fill your credentials in demo.py") # !! Remove this line after filling your credentials !!

    if demo == "mixtiles":
        act(
            "https://mixtiles.com/",
            "Order these as Mixtiles",
            name="Chandra Sekhar Nerella",
            email="nerellachandu.24@gmail.com",
            photos=[
                "demo/mixtiles/1.jpg",
                "demo/mixtiles/2.jpg",
                "demo/mixtiles/3.jpg"
            ],
            payment_info={
                "card_number": "1234 5678 8765 7432",
                "expiry_date": "12/2024",
                "cvc": "456"
            },
            address="ABC Square"
        )
    elif demo == "amazon":
        act(
            "https://amazon.com/",
            "Buy a rabbit stuffed animal",
            email="nerellachandu.24@gmail.com",
            password="Chandu@491",
        )
    elif demo == "ubereats":
        act(
            "https://ubereats.com/",
            "Order a pizza",
            email="<your email>",
            email_password="<your password>",
            address= "<your address>",
            # optional: delivery_date="...",
            # optional: delivery_time="...",
        )
    else :
        act(
            "https://yelp.com/",
            "Find the best Thai food place in Roanoke, Virginia",
            email="nerellachandu.24@gmail.com",
            email_password="Chandu@491",
            # optional: delivery_date="...",
            # optional: delivery_time="...",
        )

    x = 4

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", required=True, choices=["mixtiles", "amazon", "ubereats", "yelp"])
    args = parser.parse_args()
    main("yelp")
