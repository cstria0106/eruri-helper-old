<template>
    <div id="detailed-course">
        <div id="options">
            <label for="show-only-not-done">완료되지 않은 것만 보기</label>
            <input type="checkbox" name="show-only-not-done" v-model="showOnlyNotDone" />
            <label for="week-filter">해당 주차 이상만 보기</label>
            <input type="number" name="week-filter" v-model.number="weekFilter" />
        </div>
        <span id="name">{{data.name}}</span>
        <span id="professor">{{data.professor}}</span>
        <div id="activity-wrapper">
            <div v-if="data.videos" id="videos" class="activity">
                <h1>강의({{videos.length}})</h1>
                <ul>
                    <li v-for="video in videos" :class="{done: video.done}">
                        {{video.name}}
                        <span class="week" v-if="video.week != 0">{{video.week}}주</span>
                    </li>
                </ul>
            </div>
            <div v-if="data.homeworks" id="homeworks" class="activity">
                <h1>과제({{homeworks.length}})</h1>
                <ul>
                    <li v-for="homework in homeworks" :class="{done: homework.done}">
                        {{homework.name}}
                        <span
                            class="week"
                            v-if="homework.week != 0"
                        >{{homework.week}}주</span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "detailed-course",
    props: ["data"],
    data() {
        return {
            showOnlyNotDone: false,
            weekFilter: 0
        };
    },
    computed: {
        videos() {
            let ret = this.data.videos;

            if (this.showOnlyNotDone) {
                ret = ret.filter(el => {
                    return el.done == false;
                });
            }

            if (this.weekFilter > 0) {
                ret = ret.filter(el => {
                    return el.week == 0 || el.week > this.weekFilter;
                });
            }

            return ret;
        },
        homeworks() {
            let ret = this.data.homeworks;

            if (this.showOnlyNotDone) {
                ret = ret.filter(el => {
                    return el.done == false;
                });
            }

            if (this.weekFilter > 0) {
                ret = ret.filter(el => {
                    return el.week == 0 || el.week > this.weekFilter;
                });
            }

            return ret;
        }
    }
};
</script>

<style lang="scss">
#detailed-course {
    position: relative;
    #options {
        display: flex;
        align-items: center;
        position: absolute;
        right: 10px;

        label {
            font-size: 0.8rem;
            margin-left: 20px;
            margin-right: 5px;
        }

        input[type="number"] {
            font-size: 0.8rem;
            width: 30px;
        }
    }

    #name {
        font-size: 1.1rem;
    }
    #professor {
        font-size: 0.9rem;
        color: #999;
    }

    #activity-wrapper {
        margin-top: 10px;
        .activity {
            vertical-align: top;
            display: inline-block;
            width: calc((100% / 2) - 10px);
            margin-right: 10px;
            &:last-child {
                margin-right: 0;
            }

            h1 {
                font-size: 1.1rem;
                margin-bottom: 10px;
                padding: 10px;
                border: 1px solid #ddd;
                display: inline-block;
            }

            ul {
                li {
                    padding: 10px;
                    background: #fa8072;
                    &.done {
                        background: #98fb98;
                    }

                    .week {
                        font-size: 0.7rem;
                        color: #555;
                    }
                }
            }
        }
    }
}
</style>