<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "eruri-helper",
    async mounted() {
        this.$store.dispatch("clearCourses");
        const loggedIn = (await axios.get("http://127.0.0.1:8000/client")).data;

        if (loggedIn == true) {
            this.$store.dispatch("loggedIn");

            const courses = (await axios.get("http://127.0.0.1:8000/course"))
                .data;
            console.log(courses);
            this.$store.dispatch("addCourses", courses);
        } else {
            this.$store.dispatch("notLoggedIn");
        }
    }
};
</script>

<style lang="scss">
@import url(http://fonts.googleapis.com/earlyaccess/nanumgothic.css);
@import "./styles/reset.scss";
@import "./styles/style.scss";
</style>
