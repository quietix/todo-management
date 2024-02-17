from bot.models import User


class DBManager:
    def register_user(self, user_id, first_name, last_name, username):
        tmp_user = User.objects.filter(user_id=user_id)

        if not tmp_user:
            user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username)
            user.save()
            return True
        else:
            return False
