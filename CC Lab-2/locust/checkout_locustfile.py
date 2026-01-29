from locust import HttpUser, task, between

class CheckoutUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def checkout(self):
        self.client.get("/checkout")
