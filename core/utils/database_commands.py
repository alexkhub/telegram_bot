from sqlalchemy.exc import PendingRollbackError, IntegrityError

from .models import session, Users, Links


async def register_user_command(message):
    user = Users(telegram_id=int(message.from_user.id),
                 user_name=str(message.from_user.full_name),
                 )

    session.add(user)

    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False


async def register_list( link_name, link,  category, user):
    link_obj = Links(
        link_name=str(link_name),
        link=str(link),
        category=int(category),
        user=int(user)
    )
    session.add(link_obj)
    try:
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False


async def check_registration(message):
    connect = session.query(Users).filter(Users.telegram_id == int(message.from_user.id)).first()
    return connect




    