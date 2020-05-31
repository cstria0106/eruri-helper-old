<template>
    <div id="login-wrapper" v-if="showing">
        <div id="login">
            <label for="username">학번</label>
            <input type="text" name="username" v-model="username" />
            <label for="username">비밀번호</label>
            <input type="password" name="password" v-model="password" @keydown.enter="login" />
            <div id="button-wrapper">
                <img v-show="processing" id="loading" src="../assets/loading.gif" />
                <button @click="login">로그인</button>
            </div>
            <Alert ref="alert"></Alert>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert";

export default {
    name: "login",
    components: { Alert },
    data: () => {
        return {
            username: "",
            password: "",
            processing: false,
            showing: false
        };
    },
    methods: {
        show() {
            this.showing = true;
        },
        hide() {
            this.showing = false;
        },
        async login() {
            this.processing = true;
            try {
                const result = await axios.post(
                    "http://127.0.0.1:8000/client",
                    {
                        username: this.username,
                        password: this.password
                    }
                );
                this.processing = false;

                this.$store.dispatch("loggedIn");

                const courses = (
                    await axios.get("http://127.0.0.1:8000/course")
                ).data;
                this.$store.dispatch("addCourses", courses);

                this.hide();
            } catch (error) {
                if (!error.response) {
                    console.log(error);
                    return;
                }
                if (error.response.status == 400) {
                    this.$refs.alert.show(
                        "학번 혹은 비밀번호가 잘못되었습니다."
                    );
                } else {
                    this.$refs.alert.show("알 수 없는 오류가 발생했습니다.");
                }
                this.processing = false;
            }
        }
    }
};
</script>

<style lang="scss" scoped>
#login-wrapper {
    position: absolute;
    left: 0;
    top: 0;
    background: rgba(0, 0, 0, 0.4);
    width: 100vw;
    height: 100vh;
    z-index: 999;
    display: flex;
    align-items: center;
    justify-content: center;
    #login {
        background: #fff;
        border: 1px solid #ddd;
        padding: 20px;
        display: inline-block;

        label {
            display: inline-block;
            margin-bottom: 10px;
        }

        input {
            display: block;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
        }

        #button-wrapper {
            text-align: right;

            #loading {
                height: 25px;
            }

            button {
                display: inline-block;
                margin-top: 10px;
                padding: 5px;
                background: #fff;
                border: 1px solid #ddd;
                transition: 0.2s background;

                &:hover {
                    background: #f3f3f3;
                }
            }
        }
    }
}
</style>