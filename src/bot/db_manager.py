from bot.models import User, Section, SectionItem



class DBManager:
    def register_user(self, user_id, first_name, last_name, username):
        tmp_user = User.objects.filter(user_id=user_id)

        if not tmp_user:
            user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username)
            user.save()
            return True

        return False


    def get_sections(self, user_id):
        user = User.objects.get(user_id=user_id)
        sections = Section.objects.filter(user=user)

        # user = User.objects.get(user_id=395578806)
        # sections = Section.objects.filter(user=user)

        if sections:
            return list(sections)

        return list()


    def get_section_items(self, section_name):
        section = Section.objects.get(section_name=section_name)
        items = SectionItem.objects.filter(section=section)

        # section = Section.objects.get(section_name='Programming')
        # items = SectionItem.objects.filter(section=section)

        return list(items)
