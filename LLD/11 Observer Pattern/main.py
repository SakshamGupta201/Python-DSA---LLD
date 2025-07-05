from abc import ABC, abstractmethod


class IChannel(ABC):
    @abstractmethod
    def subscribe(self, subscriber: "ISubscriber"):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: "ISubscriber"):
        pass

    @abstractmethod
    def notify(self):
        pass


class ISubscriber(ABC):
    @abstractmethod
    def update(self):
        pass


class Channel(IChannel):
    def __init__(self, name: str = "My Channel"):
        self.name = name
        self.subscribers: list[ISubscriber] = []
        latest_video = None

    def subscribe(self, subscriber: ISubscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: ISubscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def add_video(self, video):
        self.latest_video = video
        print(f"New video added: {video}")
        self.notify()

    def get_latest_video(self):
        return self.latest_video


class Subscriber(ISubscriber):

    def __init__(self, name: str, channel: Channel):
        self.name = name
        self.channel = channel

    def update(self):
        video = self.channel.get_latest_video()
        print(f"{self.name} has been notified of a new video: {video}")


def main():
    channel = Channel()

    subscriber1 = Subscriber("Alice", channel)
    subscriber2 = Subscriber("Bob", channel)

    channel.subscribe(subscriber1)
    channel.subscribe(subscriber2)

    channel.add_video("Observer Pattern Explained")

    channel.unsubscribe(subscriber1)

    channel.add_video("Design Patterns in Python")


if __name__ == "__main__":
    main()
