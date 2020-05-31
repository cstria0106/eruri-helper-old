<template>
    <div id="alert-wrapper" v-if="showing">
        <div id="alert-message">
            {{message}}
            <div id="buttons">
                <button @click="hide">닫기</button>
            </div>
        </div>
    </div>
</template>
    
<script>
export default {
    name: "alert",
    methods: {
        show(message) {
            this.message = message;
            this.showing = true;
        },
        hide() {
            this.showing = false;
        }
    },
    data: () => {
        return {
            message: "",
            showing: false
        };
    }
};
</script>

<style lang="scss" scoped>
#alert-wrapper {
    position: absolute;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: rgba(0, 0, 0, 0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    #alert-message {
        font-size: 1rem;
        background: white;
        padding: 20px;
        border-radius: 5px;
    }

    #buttons {
        margin-top: 10px;
        text-align: right;
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
</style>