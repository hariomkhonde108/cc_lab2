from locust import HttpUser, task, between

class FestJourneyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def journey(self):
        user = "locust_user"

        # browse events
        self.client.get(f"/events?user={user}")

        # register for event id 1 (must exist)
        self.client.get(f"/register_event/1?user={user}")

        # view my events
        self.client.get(f"/my-events?user={user}")

        # checkout
        self.client.get("/checkout")
