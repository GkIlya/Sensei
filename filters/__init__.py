from loader import dp
from .group_filter import Groups, Admin, Users

if __name__ == "filters":
    dp.filters_factory.bind(Groups)
    dp.filters_factory.bind(Admin)
    dp.filters_factory.bind(Users)
