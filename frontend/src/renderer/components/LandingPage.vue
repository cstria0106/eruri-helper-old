<template>
    <div id="wrapper">
        <h1>e-루리 도우미</h1>
        <h2>강원대학교 LMS 시스템 e-루리 도우미입니다.</h2>
        <login ref="login"></login>
        <ul id="nav">
            <li @click="$refs.login.show()" v-if="!$store.getters.loggedIn">로그인</li>
        </ul>
        <ul id="courses">
            <li
                v-for="(course, i) in courses"
                :key="course.id"
                @click="loadCourse(course);selectedCourseIndex=i;"
                :class="{selected: i == selectedCourseIndex}"
            >
                <Course :data="course"></Course>
            </li>
        </ul>
        <img src="../assets/loading.gif" v-if="loading" />
        <DetailedCourse v-if="selectedCourse != null && !loading" :data="selectedCourse"></DetailedCourse>
        <alert ref="alert"></alert>
    </div>
</template>

<script>
import axios from "axios";
import Login from "./Login";
import Course from "./Course";
import DetailedCourse from "./DetailedCourse";
import Alert from "./Alert";

export default {
    name: "landing-page",
    components: { Login, Course, Alert, DetailedCourse },
    data() {
        return {
            selectedCourse: null,
            selectedCourseIndex: null,
            loading: false
        };
    },
    methods: {
        open(link) {
            this.$electron.shell.openExternal(link);
        },
        async loadCourse(course) {
            if (course.videos || course.homeworks) {
                this.selectedCourse = course;
                return;
            }

            this.loading = true;

            const newCourse = (
                await axios.get("http://127.0.0.1:8000/course?id=" + course.id)
            ).data;

            this.$store.dispatch("updateCourse", newCourse);
            this.selectedCourse = newCourse;
            this.loading = false;
        }
    },
    computed: {
        courses() {
            return this.$store.getters.courses;
        }
    }
};
</script>

<style lang="scss" scoped>
#wrapper {
    padding: 20px;
    h1 {
        font-size: 2rem;
        font-weight: bold;
    }

    h2 {
        margin-top: 5px;
        font-size: 0.9rem;
        color: #999;
    }

    #courses {
        margin-top: 10px;
        li {
            display: inline-block;
            margin-right: 10px;
            margin-bottom: 10px;
            transition: 0.2s background;
            cursor: pointer;
            &:hover {
                background: #f6f6f6;
            }

            &.selected {
                background: #f0f0f0;
            }
        }
    }

    #nav {
        position: absolute;
        top: 0;
        right: 0;
        padding: 20px;
        li {
            border: 1px solid #ddd;
            padding: 20px;
            transition: 0.2s background;
            cursor: pointer;
            &:hover {
                background-color: #f6f6f6;
            }
        }
    }
}
</style>
