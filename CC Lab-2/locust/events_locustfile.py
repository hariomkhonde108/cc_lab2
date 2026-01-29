from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_events(self):
        self.client.get("/events?user=locust_user")
