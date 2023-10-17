import factory

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    username = factory.Sequence(lambda n: 'user_%d' % n)

    class Meta:
        model = User