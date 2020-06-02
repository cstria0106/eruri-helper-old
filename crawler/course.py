from typing import Tuple, List, TYPE_CHECKING
from api import base_url
from bs4 import BeautifulSoup

if TYPE_CHECKING:
    from client import Client
    from homework import Homework
    from video import Video


class Course:  # 과목
    def __init__(self, client: 'Client', id: str, name: str, professor: str):
        self.__client: 'Client' = client
        self.__homeworks: Tuple['Homework'] = None
        self.__videos: Tuple['Video'] = None

        self.id: str = id
        self.name: str = name
        self.professor: str = professor
        pass

    # 해당 과목의 정보를 json 객체로 나타낼 수 있도록 딕셔너리로 만든다.
    # detailed가 True라면 강의, 과제에 대한 정보를 포함한다.
    def serialize(self, detailed=False):
        ret = {}
        ret['id'] = self.id
        ret['name'] = self.name
        ret['professor'] = self.professor

        if detailed:
            ret['homeworks'] = tuple(homework.serialize()
                                     for homework in self.get_homeworks())
            ret['videos'] = tuple(video.serialize()
                                  for video in self.get_videos())

        return ret

    # 문자열로 만든다.
    def __str__(self):

        s = '[%s] %s (%s) %d개의 과제와 %d개의 강의\n\n[과제]\n' % (
            self.id, self.name, self.professor, len(self.get_homeworks()), len(self.get_videos()))

        for homework in self.get_homeworks():
            s += '%s (%s)\n' % (homework.name,
                                ('완료' if homework.done else '미완료'))

        s += '\n[강의]\n'
        for video in self.get_videos():
            s += '%s (%s)\n' % (video.name, ('완료' if video.done else '미완료'))

        return s

    # 과제 목록을 얻는다.
    def get_homeworks(self) -> Tuple['Homework']:
        if self.__homeworks == None:
            self.__load_homeworks()

        return self.__homeworks

    # 강의 목록을 얻는다.
    def get_videos(self) -> Tuple['Video']:
        if self.__videos == None:
            self.__load_videos()

        return self.__videos

    # 과제 목록을 크롤링한다.
    def __load_homeworks(self) -> Tuple['Homework']:
        from homework import Homework
        homeworks = []

        url = base_url + '/mod/assign/index.php?id=' + self.id
        soup = BeautifulSoup(
            self.__client.session.get(url).text, 'html.parser'
        )

        week_cells = soup.select('td.c0')

        for week_cell in week_cells:
            cells = week_cell.parent.select('td')

            week = int(week_cell.contents[0].split('주차')[0]) if len(
                week_cell.contents
            ) > 0 else 0

            name = cells[1].select_one('a').contents[0]
            deadline = cells[2].contents[0]
            done = cells[3].contents[0] == '제출 완료'
            score = cells[4].contents[0]

            homeworks.append(Homework(week, name, done, deadline, score))

        self.__homeworks = homeworks

    # 강의 목록을 크롤링한다.
    def __load_videos(self) -> Tuple['Video']:
        from video import Video
        videos = []

        url = base_url + '/report/ubcompletion/user_progress_a.php?id=' + self.id
        soup = BeautifulSoup(
            self.__client.session.get(url).text, 'html.parser'
        )

        buttons = soup.select('.track_detail')

        week = 1

        for button in buttons:
            done = False
            name = None

            cells = button.parent.parent.select('td')

            # 해당 주차의 첫 번째 엘레멘트이거나 해당 주차에 하나의 영상만 있는 경우
            if len(cells) == 6 or len(cells) == 5:
                week = int(cells[0].contents[0])
                done = cells[4].contents[0] == 'O'
                name = cells[1].contents[1].strip()
            else:
                done = cells[3].contents[0] == 'O'
                name = cells[0].contents[1].strip()

            videos.append(Video(week, name, done))

        self.__videos = tuple(videos)
