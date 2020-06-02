from activity import Activity


class Homework(Activity):  # 과제
    def __init__(self, week, name, done, deadline, score):
        super().__init__(week, name, done)
        self.deadline = deadline
        self.score = score

    def serialize(self):
        ret = super().serialize()
        ret['deadline'] = self.deadline
        ret['score'] = self.score
        return ret
