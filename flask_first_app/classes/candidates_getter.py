class Candidate:
    def __init__(self, candidate_id: int, name: str, avatar: str, position: str, gender: str, age: str, skills: str):
        self.candidate_id = candidate_id
        self.name = name
        self.avatar = avatar
        self.position = position
        self.gender = gender
        self.age = age
        self.skills = skills

        print(f'Initialiation of instance ID {self.candidate_id} completed')

    def __repr__(self):
        return f'\nID: {self.candidate_id}\nName: {self.name}\nAvatar: {self.avatar}\n \
        Position: {self.position}\nGender: {self.gender}\nAge: {self.age}\nSkills: {self.skills}'


class CandidatesGetter:
    def __init__(self, path):
        self.path = path

    def load(self):
        pass

    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def get_by_skills(self, skill):
        pass

    def get_by_name(self, name):
        pass