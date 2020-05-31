from requests import Session
from bs4 import BeautifulSoup
from typing import List, Tuple, TYPE_CHECKING
from api import base_url

if TYPE_CHECKING:
    from section import Section
    from course import Course


class Client:
    # 클라이언트를 생성하여 로그인한다.
    def __init__(self, username: str, password: str):
        self.session = Session()  # 세션을 생성한다.

        self.session.post(base_url + '/login/index.php',  # POST /login/index.php
                          data={'username': username, 'password': password})  # 로그인한다.

        if '로그아웃' in self.session.get(base_url + '/').text:
            self.logged_in = True
        else:
            self.logged_in = False
            return

        # 과목 정보를 얻어 필드로 설정한다.
        self.courses: Tuple['Course'] = self.__load_courses()

    def __del__(self):
        self.session.close()  # 세션을 닫는다.

    # 해당 클라이언트의 모든 과목 정보를 얻는다.
    def __load_courses(self) -> Tuple['Course']:
        from course import Course

        # GET /
        response = self.session.get(base_url + '/')
        soup = BeautifulSoup(response.text, 'html.parser')

        # 각 과목에 대한 정보를 포함한 엘레멘트를 크롤링
        links = soup.select('.my-course-lists .course_link')

        courses: List['Course'] = []  # 배열 생성
        for link in links:
            # id, name, professor 정보를 가공한다.
            id = link.attrs['href'].split('=')[1].strip()
            name = link.select_one('.course-title h3').contents[0].strip()
            professor = link.select_one(
                '.course-title .prof').contents[0].strip()

            courses.append(Course(self, id, name, professor))  # 리스트에 추가

        return tuple(courses)
